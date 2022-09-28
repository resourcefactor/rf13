
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Website Settings": [
            dict(
                fieldname="container_section",
                label="View Container",
                fieldtype="Section Break",
                insert_after="banner_html",
                collapsible= 1
            ),
            dict(
                fieldname="container_image",
                label="Image",
                fieldtype="Attach Image",
                insert_after="container_section"
            ),
            dict(
                fieldname="cont_content",
                label="Content",
                fieldtype="Code",
                insert_after="container_image",
                options="HTML"
            ),
        ]
    }

    create_custom_fields(custom_fields)