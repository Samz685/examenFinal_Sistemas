# -*- coding: utf-8 -*-
# from odoo import http


# class Videojuegos(http.Controller):
#     @http.route('/videojuegos/videojuegos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videojuegos/videojuegos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('videojuegos.listing', {
#             'root': '/videojuegos/videojuegos',
#             'objects': http.request.env['videojuegos.videojuegos'].search([]),
#         })

#     @http.route('/videojuegos/videojuegos/objects/<model("videojuegos.videojuegos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videojuegos.object', {
#             'object': obj
#         })
