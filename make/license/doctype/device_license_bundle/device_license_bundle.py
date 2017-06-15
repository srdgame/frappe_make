# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
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
		sn_list = [d.sn for d in self.devices]
		for d in frappe.db.get_values("Device License", {"source_id": self.name}, "sn"):
			if d[0] not in sn_list:
				frappe.delete_doc("Device License", d[0])
			else:
				frappe.set_value("Device License", d[0], "expire_date", self.expire_date)
				frappe.set_value("Device License", d[0], "type", self.type)
				frappe.set_value("Device License", d[0], "enabled", self.enabled)

		for dev in self.devices:
			if not frappe.get_value("Device License", dev.sn):
				doc = frappe.get_doc({
					"doctype": "Device License",
					"sn": dev.sn,
					"type": self.type,
					"enabled": self.enabled,
					"expire_date": self.expire_date,
					"source_type": self.doctype,
					"source_id": self.name
				}).insert()

		frappe.enqueue('make.license.doctype.device_license_bundle.device_license_bundle.get_license_data',
						doc_name=self.name, doc_doc=self)

	def on_trash(self):
		for dev in self.devices:
			frappe.delete_doc("Device License", dev.sn)

	def update_license_data(self):
		url = frappe.db.get_single_value("Device License Settings", "server_url")
		username = frappe.db.get_single_value("Device License Settings", "username")
		passwd = frappe.db.get_single_value("Device License Settings", "password")
		session = requests.session()
		session.auth = (username, passwd)
		session.headers['Content-Type'] = 'application/json'
		session.headers['Accept'] = 'application/json'
		type_doc = frappe.get_doc('Device License Type', self.type)
		devices = []
		for dev in self.devices:
			devices.append({
				'sn': self.sn,
				'pcid': 'from_web',
				'mac': '',
			})
		r = session.post(url, data= {
			'type': type_doc.get_type(),
			'devices': devices
		}).json()
		for dev in self.devices:
			frappe.set_value("Device License", dev, 'license_data', r[dev])


def get_license_data(doc_name, doc_doc=None):
	doc = doc_doc or frappe.get_doc("Device License Bundle", doc_name)
	return doc.update_license_data()
#
#
# def license_update():
# 	for doc in frappe.get_all("Device License Bundle", "name", filters={"license_need_update": 1}):
# 		frappe.enqueue('make.license.doctype.device_license_bundle.device_license_bundle.get_license_data',
# 						doc_name=doc.name)