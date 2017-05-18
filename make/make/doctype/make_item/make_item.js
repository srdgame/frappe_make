// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Make Item', {
	setup: function(frm){
		frm.fields_dict['zones'].grid.get_field("zone").get_query  = function(){
			return {
				filters: {
					"docstatus": 1
				}
			};
		};
	},
	refresh: function(frm) {

	}
});
