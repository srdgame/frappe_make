# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DeviceLicenseType(Document):
	def get_type(self, time_limit=None, time_limit_start=None, time_limit_end=None):
		tr = {
			"time_limit": time_limit,
			"time_limit_start": time_limit_start,
			"time_limit_end": time_limit_end,
			"io_tag_count": self.io_tag_count,
			"device_count": self.device_count,
			"serial_count": self.serial_count,
			"ioplugin_count": self.ioplugin_count,
			"dsplugin_count": self.dsplugin_count,
			"features": {
				"data_cache": self.data_cache,
				"history_data": self.history_data,
				"script_calc": self.script_calc,
				"ds_channel": self.ds_channel,
				"opc_server": self.opc_server,
				"opc_client": self.opc_client,
				"opc_api": self.opc_api,
				"gprs_router": self.gprs_router,
				"trigger": self.trigger,
				"levent": self.levent,
				"swr_data": self.swr_data,
				"swr_sms": self.swr_sms,
				"cloud_data": self.cloud_data,
				"cloud_virtual_port": self.cloud_virtual_port,
				"cloud_remote_manage": self.cloud_remote_manage,
			}
		}

		if self.io_plugin_limit != 0 or self.ds_plugin_limit != 0:
			limit = {}

			if self.io_plugin_limit != 0:
				l = []
				for p in self.io_plugin_list:
					l.append({
						"enable": p.enabled == 1,
						"name": p.plugin
					})
				limit["io_list"] = l

			if self.ds_plugin_limit != 0:
				l = []
				for p in self.ds_plugin_list:
					l.append({
						"enable": p.enabled == 1,
						"name": p.plugin
					})
				limit["ds_list"] = l

			tr["driver_limit"] = limit

		return tr
#
# @frappe.whitelist()
# def query_plugin_list(type):
# 	plugins = [d.name for d in frappe.get_list("Device License Plugin", fields=["name"], filters={"plugin_type": type})]
# 	return "\n".join(str(plugin) for plugin in plugins)
