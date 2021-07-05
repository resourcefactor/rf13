# Copyright (c) 2021, RF and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, get_time, today, flt
from erpnext.stock.stock_ledger import update_entries_after
from erpnext.accounts.utils import update_gl_entries_after
from frappe.utils.background_jobs import enqueue
from frappe.model.document import Document
from erpnext.stock.get_item_details import get_conversion_factor
from erpnext.stock.utils import get_incoming_rate

class CorrectItemValuationRate(Document):
	@frappe.whitelist()
	def reposted_entries(self):
		sle_gle_reposting_start_date = self.reposting_start_date

		for doctype in ('repost_item_valuation', 'stock_entry_detail', 'purchase_receipt_item',
						'purchase_invoice_item', 'delivery_note_item', 'sales_invoice_item', 'packed_item'):
			frappe.reload_doc('stock', 'doctype', doctype)

		frappe.reload_doc('buying', 'doctype', 'purchase_receipt_item_supplied')

		if not sle_gle_reposting_start_date:
			frappe.throw(_("SLE GLE Reposting Start Date not set in {0}").format(
				frappe.utils.get_url_to_form("CSF TZ Settings", "CSF TZ Settings")))
		reposting_project_deployed_on = sle_gle_reposting_start_date + " 00:00:00"
		posting_date = sle_gle_reposting_start_date
		posting_time = '00:00:00'

		if posting_date == today():
			return

		frappe.clear_cache()
		frappe.flags.warehouse_account_map = {}

		company_list = []

		data = frappe.db.sql('''
				SELECT
					name, item_code, warehouse, voucher_type, voucher_no, posting_date, posting_time, company
				FROM
					`tabStock Ledger Entry`
				WHERE
					creation > %s
					and is_cancelled = 0
				ORDER BY timestamp(posting_date, posting_time) asc, creation asc
			''', reposting_project_deployed_on, as_dict=1)

		frappe.db.auto_commit_on_many_writes = 1
		print("Reposting Stock Ledger Entries...")
		total_sle = len(data)
		i = 0
		for d in data:
			if d.company not in company_list:
				company_list.append(d.company)

			update_entries_after({
				"item_code": d.item_code,
				"warehouse": d.warehouse,
				"posting_date": d.posting_date,
				"posting_time": d.posting_time,
				"voucher_type": d.voucher_type,
				"voucher_no": d.voucher_no,
				"sle_id": d.name
			}, allow_negative_stock=True)

			i += 1
			if i % 100 == 0:
				print(i, "/", total_sle)

		print("Reposting General Ledger Entries...")

		if data:
			for row in frappe.get_all('Company', filters={'enable_perpetual_inventory': 1}):
				if row.name in company_list:
					update_gl_entries_after(posting_date, posting_time, company=row.name)

		frappe.db.auto_commit_on_many_writes = 0

	@frappe.whitelist()
	def enqueue_reposting_sle_gle(self):
		if not self.reposting_start_date:
			frappe.throw(_("Please set Repost start date"))
		frappe.msgprint(_("Reposting of SLE and GLE started"), alert=True)
		enqueue(method=self.reposted_entries,queue='long', timeout=10000, is_async=True)

	@frappe.whitelist()
	def correct_supplier_rate(self):
		if not self.reposting_start_date:
			frappe.throw(_("Please set Repost start date"))
		purchase_receipt = frappe.get_list("Purchase Receipt", filters={'posting_date': ['>=', self.reposting_start_date],'docstatus': 1}, fields=['name'])
		for res in purchase_receipt:
			doc = frappe.get_doc("Purchase Receipt", res.name)
			total_qty = doc.get('total_qty')
			total_raw_cost = 0
			for d in doc.get("supplied_items"):
				if d.rm_item_code:
					if frappe.db.get_value('Item', d.rm_item_code, 'is_stock_item'):
						rate = get_incoming_rate({
							"item_code": d.rm_item_code,
							"warehouse": doc.supplier_warehouse,
							"posting_date": doc.posting_date,
							"posting_time": doc.posting_time,
							"qty": -1 * d.consumed_qty,
							"serial_no": d.serial_no
						})

						if rate > 0:
							d.rate = rate

					amount = flt(flt(d.consumed_qty) * flt(d.rate), d.precision("amount"))
					d.amount = amount
					d.db_update()
					total_raw_cost += amount
			for item in doc.get('items'):
				qty_in_stock_uom = flt(item.qty * item.conversion_factor)
				item.rm_supp_cost += flt((total_raw_cost / total_qty) * item.qty)
				item.valuation_rate = ((item.base_net_amount + item.item_tax_amount + item.rm_supp_cost
										+ flt(item.landed_cost_voucher_amount)) / qty_in_stock_uom)
				item.db_update()