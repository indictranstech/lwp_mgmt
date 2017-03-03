# Copyright (c) 2015, Indictrans Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import date, timedelta
from datetime import date


@frappe.whitelist()
def auto_calculate_lwp(emp,month,year):
	date = year +'-' + month +'-'
	# frappe.errprint(year +'-' + month+'-')
	present_days=frappe.db.sql("""select count(name) from `tabAttendance` where status='Present' and employee='%s' and
		att_date like '%s%%' """%(emp,date),as_list=1,debug=1)
	frappe.errprint(present_days)

	leave_days = frappe.db.sql("""select count(name) from `tabLeave Application` where employee='%s' and 
		leave_type!='Leave Without Pay' and to_date like '%s%%' and status='Approved' and docstatus=1 """%(emp,date),as_list=1,debug=1)
	frappe.errprint(leave_days)

	employee_user=frappe.get_doc("Employee",emp)
	user=employee_user.user_id
	role_list = frappe.db.sql("""select name,owner,parent,idx,role from tabUserRole where parent=%s and role='Management'""", user)
	if len(role_list) > 0:
		return False

	m = frappe.get_doc('Salary Manager').get_month_details(year, month)
	total_days_in_month = m['month_days']
	frappe.errprint("dayyyysss")
	frappe.errprint(m)
	frappe.errprint(total_days_in_month)

	if present_days and leave_days:
		frappe.errprint("day")
		present = present_days[0][0]
		frappe.errprint(["Present",present])
		leave_days_lwp = leave_days[0][0]
		frappe.errprint(["leave_day",leave_days_lwp])
		present_day = present + leave_days_lwp
		frappe.errprint(["add",present_day])
		return present_days

@frappe.whitelist()
def auto_calculate_lwp2(self,method):
	employee_user=frappe.get_doc("Employee",self.employee)
	user=employee_user.user_id
	role_list = frappe.db.sql("""select name,owner,parent,idx,role from tabUserRole where parent=%s and role='Management'""", user)
	if len(role_list) == 0:
		date = self.fiscal_year +'-' + self.month +'-'
		# frappe.errprint(year +'-' + month+'-')
		present_days=frappe.db.sql("""select count(name) from `tabAttendance` where status='Present' and employee='%s' and
			att_date like '%s%%' """%(self.employee,date),as_list=1,debug=1)
		frappe.errprint(present_days)

		leave_days = frappe.db.sql("""select count(name) from `tabLeave Application` where employee='%s' and 
			leave_type!='Leave Without Pay' and to_date like '%s%%' and status='Approved' and docstatus=1 """%(self.employee,date),as_list=1,debug=1)
		frappe.errprint(leave_days)

		m = frappe.get_doc('Salary Manager').get_month_details(self.fiscal_year, self.month)
		total_days_in_month = m['month_days']
		frappe.errprint("dayyyysss")
		frappe.errprint(m)
		frappe.errprint(total_days_in_month)

		if present_days and leave_days:
			frappe.errprint("day")
			present = present_days[0][0]
			frappe.errprint(["Present",present])
			leave_days_lwp = leave_days[0][0]
			frappe.errprint(["leave_day",leave_days_lwp])
			present_day = present + leave_days_lwp
			frappe.errprint(["add",present_day])
			self.leave_without_pay=self.total_days_in_month-present_days[0][0]
			self.days_absent=self.total_days_in_month-present_days[0][0]
			self.payment_days=self.total_days_in_month-self.leave_without_pay
			self.calculate_earning_total()
			return present_days

	def calculate_earning_total(self):
		self.gross_pay = flt(self.arrear_amount) + flt(self.leave_encashment_amount)
		for d in self.get("earnings"):
			if cint(d.e_depends_on_lwp) == 1:
				d.e_modified_amount = rounded(flt(d.e_amount) * flt(self.payment_days)
					/ cint(self.total_days_in_month), 2)
			elif not self.payment_days:
				d.e_modified_amount = 0
			elif not d.e_modified_amount:
				d.e_modified_amount = d.e_amount
			self.gross_pay += flt(d.e_modified_amount)


	def after_install():
		frappe.get_doc({'doctype': "Role", "role_name": "Management"}).insert()
		frappe.db.commit()