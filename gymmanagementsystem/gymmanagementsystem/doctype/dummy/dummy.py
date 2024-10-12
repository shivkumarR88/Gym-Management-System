# Copyright (c) 2024, Shiv Kumar R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Dummy(Document):
    pass

# @frappe.whitelist()
# def frappe_call(msg):
#     import time
#     # time.sleep(2)
#     frappe.msgprint(msg)
#     return"Hi This is a Message from Frappe Call Method By Shiva "	

# def validate_dummy(doc, method):
#     if doc.total >1000:
#         frappe.throw("The Total Amount has been exceeded")
    
#     else:
#         frappe.throw("Total Below 1000")


    # def before_save(doc):
    #     total_amount = 0
    #     for row in doc.table:
    #         row.total_addition = row.number_1 + row.number_2
    #         total_amount += row.total_addition
        
    #     doc.total = total_amount
  



