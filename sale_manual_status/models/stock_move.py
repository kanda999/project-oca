# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        vals = super()._get_new_picking_values()
        vals["manual_status"] = self.sale_line_id.order_id.manual_status
        return vals
