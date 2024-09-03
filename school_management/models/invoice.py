from odoo import models,fields


class InvoiceInherit(models.Model):
    _inherit = "account.move"

    parent_name = fields.Char(string="Parent Name")
    parent_mob_num = fields.Char(string="Parent Mob Num")





