# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document
from frappe.model.naming import make_autoname


class MakeSerialNO(Document):
	def validate(self):
		count = frappe.get_value("Make Item", self.item, "mac_count")
		if count <= 0:
			return
		zones = [d[0] for d in frappe.db.get_values("MAC UseZone", {"parent": self.item}, "zone")]
		has_zone = False
		for zone in zones:
			doc = frappe.get_doc("MAC Zone", zone)
			if not doc.is_empty():
				has_zone = True
				break
		if not has_zone:
			throw(_("MAC Zone is empty!"))

	def autoname(self):
		serial_code = frappe.get_value("Make Batch", self.batch, "serial_code")
		self.name = make_autoname(serial_code + '-.#####')

	def on_update(self):
		self.get_mac()

	def get_mac(self):
		count = frappe.get_value("Make Item", self.item, "mac_count")
		if len(self.mac) >= count:
			return
		zones = [d[0] for d in frappe.db.get_values("MAC UseZone", {"parent": self.item}, "zone")]
		mac_list = []
		for zone in zones:
			doc = frappe.get_doc("MAC Zone", zone)
			if doc.is_empty():
				continue
			for mac in doc.get_mac(count):
				mac_list.append(mac)
			if len(mac_list) >= count:
				break
		for mac in mac_list:
			self.append("mac", {"mac": mac})
		self.save()