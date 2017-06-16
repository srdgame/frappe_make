# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "make"
app_title = "Make"
app_publisher = "Dirk Chang"
app_description = "SymLink Manufacture"
app_icon = "octicon octicon-rocket"
app_color = "blue"
app_email = "dirk.chang@symid.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/make/css/make.css"
# app_include_js = "/assets/make/js/make.js"

# include js, css files in header of web template
# web_include_css = "/assets/make/css/make.css"
# web_include_js = "/assets/make/js/make.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "make.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "make.install.before_install"
# after_install = "make.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "make.notifications.get_notification_config"

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
# 		"make.tasks.all"
# 	],
# 	"daily": [
# 		"make.tasks.daily"
# 	],
# 	"hourly": [
# 		"make.tasks.hourly"
# 	],
# 	"weekly": [
# 		"make.tasks.weekly"
# 	]
# 	"monthly": [
# 		"make.tasks.monthly"
# 	]
# }

scheduler_events = {
	"hourly": [
		"make.license.doctype.device_license.device_license.license_update",
		"make.license.doctype.device_license_bundle.device_license_bundle.license_update",
	],
}

# Testing
# -------

# before_tests = "make.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "make.event.get_events"
# }

