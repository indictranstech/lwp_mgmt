# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	frappe.get_doc({
		"doctype":"Role",
		'role': "Management",
	}).insert(
	# commit is required so that we don't lose these changes because of an error in next loop's ddl
	frappe.db.commit()

)