from odoo import models,fields


class StudentSuggestion(models.TransientModel):
    _name = 'school.student.suggestion'
    _rec_name = "name"

    name = fields.Many2one('school.student', string="Student Name",readonly = True)
    suggestion = fields.Char(string="Your Suggestions")
    standard = fields.Char(string="class")

    def action_create_suggestion(self):
        student_sug = self.env['suggestions.main'].create({
            'name_student': self.name.student_name,
            'standard': self.standard,
            'suggestions': self.suggestion
        })