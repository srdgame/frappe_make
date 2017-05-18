// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Make Serial NO', {
	setup: function(frm) {
		frm.fields_dict['batch'].get_query  = function(){
			return {
				filters: {
					"docstatus": 1
				}
			};
		};
	},
	refresh: function(frm) {
		frm.add_custom_button(__("Get MAC"), function() {
			frm.events.get_mac(frm);
		}).removeClass("btn-default").addClass("btn-primary");
	},
	get_mac: function(frm) {
		return frappe.call({
			doc: frm.doc,
			method: "get_mac",
			freeze: true,
			callback: function(r) {
				if(!r.exc) frm.refresh_fields();
			}
		})
	}
});
