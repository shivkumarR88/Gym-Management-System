// Copyright (c) 2024, Shiv Kumar R and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Members", {
    refresh(frm) {
        
        let name1 = frm.doc.name1;
        let dob = frm.doc.dob;

    
        console.log('Name:', name1);
        console.log('DOB:', dob);

        frappe.call({
            method: 'gymmanagementsystem.gymmanagementsystem.doctype.gym_members.gym_members.my_method',
            args: {
                name1: name1,
                dob: dob
            },
            callback: function(response) {
                if (response.message) {
                    console.log('Server Response:', response.message);
                }
            }
        });




        // frm.add_custom_button("Gym Trainer", function(){
        //     frappe.new_doc("Gym Trainer",{})
        // },("Create"));
    }
});

