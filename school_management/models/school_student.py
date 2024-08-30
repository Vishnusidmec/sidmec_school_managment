from email.policy import default

from odoo import fields,models,api
from odoo.tools.populate import compute


class SchoolStudent(models.Model):
    _name = 'school.student'

    student_name = fields.Char(string="Full name", required=True)
    guardian_name = fields.Char(string="Guardian name", required=True)
    guardian_phone = fields.Char(string="Guardian_phone")
    date_of_birth = fields.Date(string="Date of birth" )
    age = fields.Char(string="Age")
    address = fields.Char(string="Address")
    standard= fields.Char(string="Class")
    class_teacher=fields.Many2one('school.teacher', string="class_teacher")
    fee_structure_ids = fields.One2many('fees.structure', 'student_id', string='Fees Structures',
                                        help="Related Fees Structure")
    teacher_ids = fields.Many2many(
        'school.teacher', string="Other Subject Teachers",
        help='Mention the teachers who teach other subjects.')
    select_status = fields.Selection([('not_selected', 'Not Selected'),('selected' , 'Selected')],default='not_selected')
    age_date_of_birth = fields.Boolean(compute='age_finding',store=True)

    def action_select(self):
        self.select_status = 'selected'


    @api.depends('date_of_birth','age_date_of_birth')
    def age_finding(self):
        print("working fine")