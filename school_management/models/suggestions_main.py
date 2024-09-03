from odoo import models,fields


class SuggestionMain(models.Model):
    _name = "suggestions.main"
    _rec_name = "name"

    name = fields.Many2one('school.student', string="Student Name")
    name_student = fields.Char(string="Student")
    standard = fields.Char(string="Class")
    suggestions = fields.Char(string="Suggestions")