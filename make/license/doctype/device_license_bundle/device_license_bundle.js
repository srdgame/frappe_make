// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Device License Bundle', {
	setup: function(frm) {
		frm.fields_dict['type'].get_query  = function(){
			return {
				filters: {
					"docstatus": 1
				}
			};
		};
	},
	setup: function(frm) {
		frm.fields_dict["source_type"].get_query = function(){
			return {
				filters: {
					"name": ["in","Stock Order,Cloud Company,User"]
				}
			}
		};
	},
	refresh: function(frm) {

	}
});
