// Copyright (c) 2024, Shiv Kumar R and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Child Table for Dummy", {
// 	number_1: function(frm, cdt, cdn) {
//         let row = frappe.get_doc(cdt, cdn);
//         frappe.model.set_value(cdt, cdn, 'total_addition', row.number_1 + row.number_2);
//     },
//     number_2: function(frm, cdt, cdn) {
//         let row = frappe.get_doc(cdt, cdn);
//         frappe.model.set_value(cdt, cdn, 'total_addition', row.number_1 + row.number_2);
//     }
// });
// frappe.ui.form.on("Dummy", {
//     refresh(frm){
//         frappe.call({
//             method: 'gymmanagementsystem.gymmanagementsystem.doctype.dummy.dummy.frappe_call',
//             args:{
//                 msg:`Hello ${frm.doc.name1} ,and Your total amount is ${frm.doc.total} `
//             },
//             freeze:true,
//             freeze_message:__("Calling frappe Call Method by Shiva"),
//             callback: function(r){
//                 frappe.msgprint(r.message)
//             }
//         });

//     }

// }
// );