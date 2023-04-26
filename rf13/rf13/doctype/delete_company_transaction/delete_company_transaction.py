# Copyright (c) 2023, RF and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DeleteCompanyTransaction(Document):

    @frappe.whitelist()
    def delete_transaction(self):
        frappe.enqueue(delete_company_transaction, doc=self, queue='long', timeout=3600)

def delete_company_transaction(doc):
    tdr = frappe.get_doc({"doctype": "Transaction Deletion Record", "company": doc.company})
    tdr.insert()
    tdr.submit()