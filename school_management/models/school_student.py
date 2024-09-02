from email.policy import default

from odoo import fields,models,api
from odoo.tools.populate import compute
from datetime import datetime
from odoo.exceptions import ValidationError



class SchoolStudent(models.Model):
    _name = 'school.student'
    _rec_name = "student_name"
    _inherit = ['mail.thread']

    student_name = fields.Char(string="Full name", required=True)
    guardian_name = fields.Char(string="Guardian name", required=True)
    guardian_phone = fields.Char(string="Guardian_phone")
    date_of_birth = fields.Date(string="Date of birth" )
    age = fields.Char(string="Age",compute='_compute_age',store=True)
    address = fields.Char(string="Address")
    standard = fields.Char(string="Class")
    teacher_mob = fields.Char(string="Teacher Mobile")
    class_teacher = fields.Many2one('school.teacher', string="class_teacher")

    fee_structure_ids = fields.One2many('fees.structure', 'student_id', string='Fees Structures',
                                        help="Related Fees Structure")
    teacher_ids = fields.Many2many(
        'school.teacher', string="Other Subject Teachers",
        help='Mention the teachers who teach other subjects.')

    select_status = fields.Selection([('draft', 'Draft'), ('admitted', 'Admitted')],
                                        default='draft')

    def action_select(self):
        self.select_status = 'admitted'




#function for teacher mobile automatically update when student select the teacher
    @api.onchange('class_teacher')
    def _onchange_class_teacher(self):
        if self.class_teacher:
            self.teacher_mob = self.class_teacher.mobile

#function for calculating age automatically when DOB entered
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = datetime.today()
                dob = fields.Date.from_string(record.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = age

    def create(self, vals):
        if vals['guardian_phone']:
            print("entered details", vals)
            student_exist = self.env["school.student"].search([('guardian_phone', "=", vals['guardian_phone'])])
            if student_exist:
                raise ValidationError("There is already a student with the same phone number")
            return super(SchoolStudent, self).create(vals)