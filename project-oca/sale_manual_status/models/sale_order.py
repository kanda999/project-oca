# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

#aaa
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    #manual_status = fields.Boolean("manual_status",)

    manual_status = fields.Selection([
        ('consu', 'Consumable'),
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Product Type', default='consu', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')