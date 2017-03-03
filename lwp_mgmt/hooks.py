# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "lwp_mgmt"
app_title = "Lwp Mgmt"
app_publisher = "New Indictrans Technologies pvt ltd."
app_description = "this app is to calculate lwp from attendance"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lwp_mgmt/css/lwp_mgmt.css"
# app_include_js = "/assets/lwp_mgmt/js/lwp_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/lwp_mgmt/css/lwp_mgmt.css"
# web_include_js = "/assets/lwp_mgmt/js/lwp_mgmt.js"

fixtures = ["Custom Script"]
fixtures = ["Custom Field"]

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

# before_install = "lwp_mgmt.install.before_install"
# after_install = "lwp_mgmt.install.after_install"
#after_install = "lwp_mgmt.config.lwp_calculate.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lwp_mgmt.notifications.get_notification_config"

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

doc_events = {
	"Salary Slip": {
		"validate": "lwp_mgmt.config.lwp_calculate.auto_calculate_lwp2"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lwp_mgmt.tasks.all"
# 	],
# 	"daily": [
# 		"lwp_mgmt.tasks.daily"
# 	],
# 	"hourly": [
# 		"lwp_mgmt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lwp_mgmt.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lwp_mgmt.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lwp_mgmt.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lwp_mgmt.event.get_events"
# }

