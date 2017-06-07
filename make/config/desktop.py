# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Make",
			"color": "blue",
			"icon": "octicon octicon-rocket",
			"type": "module",
			"label": _("Make")
		},
		{
			"module_name": "License",
			"color": "blue",
			"icon": "octicon octicon-rocket",
			"type": "module",
			"label": _("License")
		}
	]
