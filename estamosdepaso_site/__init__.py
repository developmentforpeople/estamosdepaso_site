# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import frappe

__version__ = '0.0.1'


# def http_request_customization():
# 	"""
# 	Executed with `bench start` too, so do not use site/db methods.
# 	"""
# 	print("PASA!")

# import copy
# from frappe.app import init_request
# HTTPRequest_set_lang = copy.copy(init_request)
# def aef_HTTPRequest_set_lang(request):
# 	# print(request.path)
# 	if (request.path.startswith('/pwa/js/') or request.path.startswith('/pwa/css/')
# 		or request.path.startswith('/pwa/img/')):
# 		import os
# 		file_path = frappe.get_app_path('estamosdepaso_site', 'www') + request.path
# 		if os.path.exists(file_path):
# 			try:
# 				f = open(file_path, 'rb')
# 			except IOError:
# 				raise NotFound
# 			from werkzeug.wrappers import Response
# 			from werkzeug.wsgi import wrap_file
# 			import mimetypes
# 			response = Response(wrap_file(request.environ, f))#, direct_passthrough=True)
# 			response.mimetype = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
# 			return response
# 	HTTPRequest_set_lang(request)
# frappe.app.init_request = aef_HTTPRequest_set_lang
