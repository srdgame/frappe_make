# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document


class DeviceLicenseBundle(Document):
	def validate(self):
		for dev in self.devices:
			if frappe.get_value("Device License", dev.sn):
				sid = frappe.get_value("Device License", dev.sn, "source_id")
				if sid != self.name:
					throw(_("Device SN {0} is licensed by {1}").format(dev.sn, sid))

	def on_update(self):
		type_value = frappe.get_value("Device License Type", self.type, "value")
		sn_list = [d.sn for d in self.devices]
		for d in frappe.db.get_values("Device License", {"source_id": self.name}, "sn"):
			if d[0] not in sn_list:
				frappe.delete_doc("Device License", d[0])
			else:
				frappe.set_value("Device License", d[0], "expire_date", self.expire_date)
				frappe.set_value("Device License", d[0], "type", self.type)
				frappe.set_value("Device License", d[0], "type_value", type_value)
				frappe.set_value("Device License", d[0], "enabled", self.enabled)

		for dev in self.devices:
			if not frappe.get_value("Device License", dev.sn):
				doc = frappe.get_doc({
					"doctype": "Device License",
					"sn": dev.sn,
					"type": self.type,
					"type_value": type_value,
					"enabled": self.enabled,
					"expire_date": self.expire_date,
					"source_type": self.doctype,
					"source_id": self.name
				}).insert()

	def on_trash(self):
		for dev in self.devices:
			frappe.delete_doc("Device License", dev.sn)

