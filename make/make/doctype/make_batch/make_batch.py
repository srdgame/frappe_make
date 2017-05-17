# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MakeBatch(Document):
	def validate(self):
		serial_code = frappe.get_value("Make Item", self.item, "serial_code")
		self.serial_code = "{0}-{1}".format(serial_code, self.batch_no)
