# Copyright (c) 2024, Shiv Kumar R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMembers(Document):
    # pass
    
    def validate(self):
        self.new_document()
        
        
    def new_document(self):
        doc=frappe.new_doc("Gym Membership")
        doc.name1=self.name1

        doc.insert()




