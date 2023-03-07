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

    # Sirve para validar.
    @api.constrains('pvp')
    def _verificador(self):
        for record in self:
            if record.pvp < 2:
                raise ValidationError("El precio recomendado tiene que ser mayor que 2")
