from odoo import models,fields

class FeesStructure(models.Model):
    _name = "fees.structure"

    name = fields.Char(string="Name",required=True)
    fees_amount =fields.Float(string = "Fees Amount")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    tax_amount = fields.Float(string = "Tax Amount")
    student_id = fields.Many2one('school.student',string="Teacher")
