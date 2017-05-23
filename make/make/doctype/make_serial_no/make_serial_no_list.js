/**
 * Created by cch on 17-5-23.
 */

frappe.listview_settings['Make Serial NO'] = {
	refresh: function(doclist){
		me = this;
		dlist = doclist;
		if (has_common(roles, ["Administrator", "Make Manager", "Make User"])){
			doclist.page.clear_inner_toolbar();
			doclist.page.add_inner_button(__("Batch Create"), function() {
				me.batch_create = new frappe.ui.Dialog({
					'title': 'Batch Create',
					fields: [
						{
							"label": __("Make Batch"),
							"fieldname": "batch",
							"fieldtype": "Link",
							"options": "Make Batch",
							"reqd": 1
						},
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
					return frappe.call({
						method: 'make.make.doctype.make_serial_no.make_serial_no.batch_create',
						args: {
							"batch": me.batch_create.get_values().batch,
							"count": me.batch_create.get_values().count
						},
						freeze: true,
						callback: function(r) {
							me.batch_create.hide();
							if(!r.exc) {
								msgprint(r.message);
								dlist.refresh();
							} else {
								msgprint(r._server_message);
							}
						}
					})
				});
			}).removeClass("btn-default").addClass("btn-primary");
		}
	}
};
