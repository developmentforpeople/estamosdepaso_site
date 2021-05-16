# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "estamosdepaso_site"
app_title = "EstamosDePaso Site"
app_publisher = "DFP"
app_description = "EstamosDePaso Site"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developmentforpeople@gmail.com"
app_license = "MIT"

# # TODO: check with future Frappe versions because with 12 is not yet implemented!!!
# override_doctype_class = {
# 	"Blog": "aef_site2.overrides.todo.CustomToDo",
# }

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/estamosdepaso_site/css/estamosdepaso_site.css"
# app_include_js = "/assets/estamosdepaso_site/js/estamosdepaso_site.js"

# include js, css files in header of web template
# web_include_css = "/assets/estamosdepaso_site/css/estamosdepaso_site.css"
# web_include_js = "/assets/estamosdepaso_site/js/estamosdepaso_site.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "estamosdepaso_site/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Redirects / Rewrites
# website_route_rules = [
#     {"from_route": "/pwa/<name>", "to_route": "app/projects/project"},
# ]

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

# before_install = "estamosdepaso_site.install.before_install"
# after_install = "estamosdepaso_site.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "estamosdepaso_site.notifications.get_notification_config"

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
# 		"estamosdepaso_site.tasks.all"
# 	],
# 	"daily": [
# 		"estamosdepaso_site.tasks.daily"
# 	],
# 	"hourly": [
# 		"estamosdepaso_site.tasks.hourly"
# 	],
# 	"weekly": [
# 		"estamosdepaso_site.tasks.weekly"
# 	]
# 	"monthly": [
# 		"estamosdepaso_site.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "estamosdepaso_site.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "estamosdepaso_site.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "estamosdepaso_site.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

