// Copyright (c) 2023, RF and contributors
// For license information, please see license.txt

frappe.ui.form.on('Delete Company Transaction', {
	 refresh: function(frm) {
         frm.disable_save();
         let label = __('Delete Transaction');
         frm.page.set_primary_action(label, () => frm.events.delete_transaction(frm));
	 },
	 delete_transaction(frm){
	    if (!frm.doc.company){
	        frappe.throw(__("Please select Company"))
	    }

        frappe.confirm('Are you sure you want to delete transaction?',
            () => {
               frappe.call({
                    method: "delete_transaction",
                    doc: frm.doc,
                    freeze: true,
                    callback: function(r) {
                        frappe.msgprint(__('Added in Background Job'));
                    }
                });
            }, () => {
                // action to perform if No is selected
            })
	 }
});
