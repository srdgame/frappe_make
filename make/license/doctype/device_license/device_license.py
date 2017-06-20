# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
import time
import json
from frappe.utils.data import get_timestamp
from frappe.model.document import Document


class DeviceLicense(Document):
	def validate(self):
		if not self.source_id:
			self.license_need_update = 1
		else:
			self.license_need_update = 0

	def on_update(self):
		if self.license_need_update == 1:
			frappe.enqueue('make.license.doctype.device_license.device_license.gen_license_data',
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
		lic_type = type_doc.get_type(1, get_timestamp(self.creation), get_timestamp(self.expire_date))

		r = session.post(url, data=json.dumps({
			'type': lic_type,
			'devices': [{
				'sn': self.sn,
				'pcid': self.pcid,
				'only_pcid': self.only_pcid,
				'mac': '',
			}]
		})).json()

		lic_data = r[self.sn]
		if lic_data:
			#frappe.db.set_value("Device License", self.name, 'license_data', lic_data)
			#frappe.db.set_value("Device License", self.name, "license_need_update", 0)
			self.license_data = lic_data
			self.license_need_update = 0
			self.save()


def gen_license_data(doc_name, doc_doc=None):
	doc = doc_doc or frappe.get_doc("Device License", doc_name)
	try:
		return doc.update_license_data()
	except Exception as ex:
		return


def license_update():
	for doc in frappe.get_all("Device License", "name", filters={"license_need_update": 1}):
		frappe.enqueue('make.license.doctype.device_license.device_license.gen_license_data',
						doc_name=doc.name)