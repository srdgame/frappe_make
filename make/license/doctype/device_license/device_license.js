// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Device License', {
	setup: function(frm) {
		frm.fields_dict['type'].get_query  = function(){
			return {
				filters: {
					"docstatus": 1
				}
			};
		};
	},
	refresh: function(frm) {
		if(has_common(roles, ["Administrator", "Licence Manager"])){
			frm.add_custom_button(__("Update License Data"), function() {
				frm.events.update_license_data(frm);
			}).removeClass("btn-default").addClass("btn-primary");
		}
	},

	update_license_data: function(frm) {
		return frappe.call({
			doc: frm.doc,
			method: "update_license_data",
			freeze: true,
			callback: function(r) {
				if(!r.exc) {
					frm.refresh_fields();
				}
			}
		})
	},
});
