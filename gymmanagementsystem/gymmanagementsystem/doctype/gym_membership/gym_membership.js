// Copyright (c) 2024, Shiv Kumar R and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
        is_subscribed:function(frm){
            frappe.call({
                method: 'gymmanagementsystem.gymmanagementsystem.doctype.gym_membership.gym_membership.frappe_call',
                args:{
                    msg:`Hello ${frm.doc.name1} has been the Added to the Gym and Subscribed the Locker `
                },
                freeze:true,
                freeze_message:__("Calling frappe Call Method by Shiva"),
                callback: function(r){
                    frappe.msgprint(r.message)
                }
            });

        }

    
});

frappe.ui.form.on('Gym Membership', {
	refresh(frm) {
		frm.set_intro("To Confirm your Membership fill this form Correctly ")
	}
})