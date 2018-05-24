# -*- coding: utf-8 -*-
# Copyright (c) 2018, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import throw, msgprint, _


def get_post_json_data():
	if frappe.request.method != "POST":
		throw(_("Request Method Must be POST!"))
	ctype = frappe.get_request_header("Content-Type")
	if "json" not in ctype.lower():
		throw(_("Incorrect HTTP Content-Type found {0}").format(ctype))
	data = frappe.request.get_data()
	if not data:
		throw(_("JSON Data not found!"))
	return json.loads(data)


@frappe.whitelist(allow_guest=True)
def hello():
	return "Hello World!"


@frappe.whitelist(allow_guest=True)
def get_mac(sn):
	doc = frappe.get_doc("Make Serial NO", sn)
	return [d.mac for d in doc.mac]


@frappe.whitelist(allow_guest=True)
def get_mac_list():
	data = get_post_json_data()
	mac_list = {}
	for sn in data.get('sn'):
		doc = frappe.get_doc("Make Serial NO", sn)
		mac_list[sn] = [d.mac for d in doc.mac]

	return mac_list