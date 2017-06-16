# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
from frappe.model.document import Document


class DeviceLicense(Document):
	def validate(self):
		if not self.source_id:
			self.license_need_update = 1

	def on_update(self):
		if self.license_need_update == 1:
			frappe.enqueue('make.license.doctype.device_license.device_license.get_license_data',
							doc_name=self.name, doc_doc=self)

	def update_license_data(self):
		url = frappe.db.get_single_value("Device License Settings", "server_url")
		username = frappe.db.get_single_value("Device License Settings", "username")
		passwd = frappe.db.get_single_value("Device License Settings", "password")

		session = requests.session()
		session.auth = (username, passwd)
		session.headers['Content-Type'] = 'application/json'
		session.headers['Accept'] = 'application/json'
		type_doc = frappe.get_doc('Device License Type', self.type)

		r = session.post(url, data= {
			'type': type_doc.get_type(),
			'devices': [{
				'sn': self.sn,
				'pcid': 'from_web',
				'mac': '',
			}]
		}).json()

		if r[self.sn]:
			self.set('license_data', r.json()[self.sn])
			self.set('license_need_update', 0)
			self.save()


def get_license_data(doc_name, doc_doc=None):
	doc = doc_doc or frappe.get_doc("Device License", doc_name)
	return doc.update_license_data()


def license_update():
	for doc in frappe.get_all("Device License", "name", filters={"license_need_update": 1}):
		frappe.enqueue('make.license.doctype.device_license.device_license.get_license_data',
						doc_name=doc.name)