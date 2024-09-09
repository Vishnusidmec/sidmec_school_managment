from odoo import models,fields,api
from odoo.fields import Float


class FeesStructure(models.Model):
    _name = "fees.structure"
    _rec_name = "name"
    name = fields.Char(string="Name",required=True)
    fees_amount =fields.Float(string = "Fees Amount")
    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    # tax_percentage = fields.Float(string="Tax")
    tax_ids = fields.Many2many('account.tax',string="Tax")

    tax_amount = fields.Float(string="Tax Amount",  compute='_compute_tax', store=True)
    total_amount = fields.Float(string="Total Amount", compute='_compute_total_amount', store=True)
    student_id = fields.Many2one('school.student',string="Teacher")
    untaxed_amount = fields.Float(string="Untaxed Amount", compute='_compute_total_amount', store=True)



    @api.depends('fees_amount', 'tax_amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.fees_amount + record.tax_amount
            record.untaxed_amount = record.fees_amount



    @api.depends('fees_amount','tax_ids')
    def _compute_tax(self):
        for record in self:
            record.total_amount = record.fees_amount + record.tax_amount
            record.untaxed_amount = record.fees_amount
            total_tax = 0.0
            for rec in record.tax_ids:
                tax_amount = rec.amount/100 * record.fees_amount
                total_tax += tax_amount
            record.tax_amount = total_tax
