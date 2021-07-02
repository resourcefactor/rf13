// Copyright (c) 2021, RF and contributors
// For license information, please see license.txt

frappe.ui.form.on('Correct Item Valuation Rate', {
	 refresh: function(frm) {
//	    frm.save_disabled = 1;
        frm.fields_dict.reposted_entries.$input.addClass("btn-primary");
	 },
	 reposted_entries: function(frm){
	     frappe.call({
            method: "enqueue_reposting_sle_gle",
            doc: frm.doc,
            callback: function(data) {
                 console.log(data);
            }
        });
	 }
});
