# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from make.mac import mac_add

class MACZone(Document):
	def on_submit(self):
		self.current_address = self.start_address

	def __get_one_mac(self):
		mac = self.current_address
		if mac == self.end_address:
			return None

		self.set("current_address", mac_add(self.current_address, 1))
		self.save()
		return mac

	def get_mac(self, num=1):
		l = []
		for i in range(num):
			l.append(self.__get_one_mac())
		return l

	def is_empty(self):
		print('is_empty', self.current_address, self.end_address)
		return self.current_address == self.end_address
