# -*- coding: utf-8 -*-
# from odoo import http


# class LibaryManagement(http.Controller):
#     @http.route('/libary_management/libary_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libary_management/libary_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libary_management.listing', {
#             'root': '/libary_management/libary_management',
#             'objects': http.request.env['libary_management.libary_management'].search([]),
#         })

#     @http.route('/libary_management/libary_management/objects/<model("libary_management.libary_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libary_management.object', {
#             'object': obj
#         })

