// Copyright (c) 2021, RF and contributors
// For license information, please see license.txt

frappe.ui.form.on('Correct Item Valuation Rate', {
	 refresh: function(frm) {
//	    frm.save_disabled = 1;
        frm.fields_dict.reposted_entries.$input.addClass("btn-primary");
        frm.fields_dict.correct_supplier_rate.$input.addClass("btn-primary");
	 },
	 reposted_entries: function(frm){
	     frappe.call({
            method: "enqueue_reposting_sle_gle",
            doc: frm.doc,
            callback: function(data) {
                 console.log(data);
            }
        });
	 },
	 correct_supplier_rate: function(frm){
	     frappe.call({
            method: "correct_supplier_rate",
            doc: frm.doc,
            freeze: true,
            freeze_message: __("Recalculate Amount"),
            callback: function(data) {
                 console.log(data);
            }
        });
	 }
});
