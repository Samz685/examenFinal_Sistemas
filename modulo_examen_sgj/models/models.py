# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Cliente(models.Model):
    _name = 'cliente'
    _description = 'Datos del cliente'

    name = fields.Char(required=True, string='Nombre')
    street = fields.Char(string='Dirección')
    city = fields.Char(string='Ciudad')
    state = fields.Char(string='Estado')
    zip = fields.Char(string='Código Postal')
    country = fields.Char(string='País')


class Factura(models.Model):
    _name = 'factura'
    _description = 'Datos de la factura'

    name = fields.Char(required=True, string='Número de factura')
    date_issued = fields.Date(default=fields.Date.today(), string='Fecha de emisión')
    date_due = fields.Date(string='Fecha de vencimiento')
    total_amount = fields.Float(string='Monto total')
    cliente_id = fields.Many2one('cliente', string='Cliente')


class Producto(models.Model):
    _name = 'producto'
    _description = 'Datos del producto'

    name = fields.Char(required=True, string='Nombre')
    description = fields.Text(string='Descripción')
    pvp = fields.Float(string='Precio')
    cantidad = fields.Integer(string='Cantidad')
    precio_total = fields.Float(string='Precio Total', compute='_compute_precio_total')

    def zero_price_when_no_stock(func):
        def wrapper(producto):
            if producto.cantidad == 0:
                producto.pvp = 0
            return func(producto)

        return wrapper

    @api.depends('pvp', 'cantidad')
    def _compute_precio_total(self):
        for record in self:
            record.precio_total = record.pvp * record.cantidad

    @api.model
    @zero_price_when_no_stock
    def create(self, vals):
        return super(Producto, self).create(vals)

    @api.multi
    @zero_price_when_no_stock
    def write(self, vals):
        return super(Producto, self).write(vals)
