# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class MakeSerialNO(Document):
	def autoname(self):
		serial_code = frappe.get_value("Make Batch", self.batch, "serial_code")
		self.name = make_autoname(serial_code + '-.#####')
