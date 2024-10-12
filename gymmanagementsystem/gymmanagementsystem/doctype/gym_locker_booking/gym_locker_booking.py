# Copyright (c) 2024, Shiv Kumar R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymLockerBooking(Document):
	pass

def book_locker(doc, method):
    locker = frappe.get_doc("Locker", doc.locker_number)
    if locker.status == "Available":
        locker.status = "Booked"
        locker.save()
        gym_membership = frappe.get_doc("GymMembership", doc.gym_membership_id)
        gym_membership.locker_number = doc.locker_number
        gym_membership.save()
    else:
        frappe.throw(_("Locker is already occupied"))

