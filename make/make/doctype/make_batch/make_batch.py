# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document

class MakeBatch(Document):
	def validate(self):
		if len(self.batch_no) != 6:
			throw(_("Batch NO length must be six!"))
		serial_code = frappe.get_value("Make Item", self.item, "serial_code")
		self.serial_code = "{0}-{1}".format(serial_code, self.batch_no)

	def batch_create(self, count):
		for i in range(count):
			doc = frappe.get_doc({
				"doctype": "Make Serial NO",
				"item": self.item,
				"batch": self.name,
			}).insert()
		return "{0} Serial NO has been created!".format(count)