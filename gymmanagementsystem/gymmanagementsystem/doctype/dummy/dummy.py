# Copyright (c) 2024, Shiv Kumar R and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Dummy(Document):
    pass
    # def before_save(doc):
    #     total_amount = 0
    #     for row in doc.table:
    #         row.total_addition = row.number_1 + row.number_2
    #         total_amount += row.total_addition
        
    #     doc.total = total_amount



