// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Make Batch', {
	setup: function(frm) {
	},
	refresh: function(frm) {
		me = this;
		frm.add_custom_button(__("Create Batch Serial NO"), function() {
			me.batch_create = new frappe.ui.Dialog({
				'title': 'Batch Create',
				fields: [
					{
						"label": __("Count of Serial NO"),
						"fieldname": "count",
						"fieldtype": "Int",
						"reqd": 1
					}
				]
			});

			me.batch_create.show();
			me.batch_create.set_primary_action(__("Create"), function () {
				frm.events.batch_create(frm, me.batch_create.get_values().count);
			});
		}).removeClass("btn-default").addClass("btn-primary");
	},
	batch_create: function(frm, count) {
		return frappe.call({
			doc: frm.doc,
			method: "batch_create",
			args: {"count": count},
			freeze: true,
			callback: function(r) {
				me.batch_create.hide();
				if(!r.exc) {
					frm.refresh_fields();
					msgprint(r.message);
				} else {
					msgprint(r._server_message);
				}
			}
		})
	}
});
