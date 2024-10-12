# Copyright (c) 2024, Shiv Kumar R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMembership(Document):


	def book_locker(gym_membership_id, locker_number):
		locker = frappe.get_doc("Locker", locker_number)
		if locker.status == "Available":
			locker.status = "Booked"
			locker.save()
			gym_membership = frappe.get_doc("GymMembership", gym_membership_id)
			gym_membership.locker_number = locker_number
			gym_membership.save()
		else:
			frappe.throw("Locker is already occupied")
   
   
#    Frappe call Method 
@frappe.whitelist()
def frappe_call(msg):
    import time
    time.sleep(2)
    frappe.msgprint(msg)
    return"Hi This is a Message from Frappe Call Method By Shiva "		


