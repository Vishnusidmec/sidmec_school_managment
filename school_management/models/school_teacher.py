from odoo import fields,models

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    name = fields.Char(string="Full name", required=True)
    mobile = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address")
    date_of_birth = fields.Date(string="Date of birth")
    is_a_teacher =fields.Boolean()
    add_student = fields.One2many('school.student','class_teacher',string="Add Student")