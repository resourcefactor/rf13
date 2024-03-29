# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rf13"
app_title = "RF13"
app_publisher = "RF"
app_description = "Redesign Login Page"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sales@resourcefactors.com"
app_license = "MIT"
app_logo_url = '/assets/rf13/images/rflogo.png'

# Includes in <head>
# ------------------

app_include_css = "/assets/rf13/css/whitelabel_app.css"
# app_include_js = "/assets/whitelabel/js/whitelabel.js"

# include js, css files in header of web template
# web_include_css = "/assets/rf13/css/whitelabel_web.css"
# web_include_js = "/assets/rf13/js/whitelabel.js"


website_context = {
    "favicon": "/assets/rf13/images/rflogo.png",
    "splash_image": "/assets/rf13/images/rflogo.png"
}
after_migrate = ['rf13.api.whitelabel_patch']

boot_session = "rf13.api.boot_session"
# include js, css files in header of desk.html
# app_include_css = "/assets/rf13/css/rf13.css"
# app_include_js = "/assets/rf13/js/rf13.js"

# include js, css files in header of web template
# web_include_css = "/assets/rf13/css/rf13.css"
# web_include_js = "/assets/rf13/js/rf13.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rf13/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"Issue": "public/js/issue.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Issue" : "public/js/issue.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rf13.install.before_install"
# after_install = "rf13.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rf13.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rf13.tasks.all"
# 	],
# 	"daily": [
# 		"rf13.tasks.daily"
# 	],
# 	"hourly": [
# 		"rf13.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rf13.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rf13.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rf13.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rf13.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rf13.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

