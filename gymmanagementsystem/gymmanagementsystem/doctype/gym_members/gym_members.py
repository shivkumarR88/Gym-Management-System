# Copyright (c) 2024, Shiv Kumar R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMembers(Document):
    pass

@frappe.whitelist()
def my_method(name1, dob):
    message = f'Hello, {name1}. Your Date of birth is {dob} .'
    return message



