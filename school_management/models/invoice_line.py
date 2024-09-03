from odoo import models,fields


class InvoiceLineInherit(models.Model):
    _inherit = "account.move.line"

    fees_structure = fields.Many2one('fees.structure', string="Fees structure")