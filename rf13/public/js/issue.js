frappe.ui.form.on('Issue', {
    refresh: function(frm){
        if (frm.doc.status == 'Closed' && !frappe.user.has_role("Issue Manager"))
        {
            frm.set_df_property('status', 'read_only', 1);
            frm.set_df_property('subject', 'read_only', 1);
            frm.set_df_property('customer', 'read_only', 1);
            frm.set_df_property('priority', 'read_only', 1);
            frm.set_df_property('issue_type', 'read_only', 1);
            frm.set_df_property('description', 'read_only', 1);
            frm.set_df_property('first_responded_on', 'read_only', 1);
            frm.set_df_property('resolution_details', 'read_only', 1);
            frm.set_df_property('lead', 'read_only', 1);
            frm.set_df_property('contact', 'read_only', 1);
            frm.set_df_property('project', 'read_only', 1);
            frm.set_df_property('email_account', 'read_only', 1);
            frm.set_df_property('company', 'read_only', 1);
            frm.set_df_property('via_customer_portal', 'read_only', 1);
        }
        else{
            frm.set_df_property('status', 'read_only', 0);
            frm.set_df_property('subject', 'read_only', 0);
            frm.set_df_property('customer', 'read_only', 0);
            frm.set_df_property('priority', 'read_only', 0);
            frm.set_df_property('issue_type', 'read_only', 0);
            frm.set_df_property('description', 'read_only', 0);
            frm.set_df_property('first_responded_on', 'read_only', 0);
            frm.set_df_property('resolution_details', 'read_only', 0);
            frm.set_df_property('lead', 'read_only', 0);
            frm.set_df_property('contact', 'read_only', 0);
            frm.set_df_property('project', 'read_only', 0);
            frm.set_df_property('email_account', 'read_only', 0);
            frm.set_df_property('company', 'read_only', 0);
            frm.set_df_property('via_customer_portal', 'read_only', 0);
        }
    }
})