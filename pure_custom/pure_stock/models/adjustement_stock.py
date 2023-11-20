from odoo import api,fields, models


class AdjustementStock(models.Model):
    _inherit = "stock.quant"