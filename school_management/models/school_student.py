from email.policy import default

from odoo import fields,models,api,_
from odoo.addons.test_convert.tests.test_env import record
from odoo.tools.populate import compute
from datetime import datetime
from odoo.exceptions import ValidationError



class SchoolStudent(models.Model):
    _name = 'school.student'
    _rec_name = "student_name"
    _inherit = ['mail.thread']

    student_name = fields.Char(string="Full name", required=True,tracking =True)
    guardian_name = fields.Char(string="Guardian name", required=True,tracking =True)
    guardian_phone = fields.Char(string="Guardian_phone",tracking =True)
    date_of_birth = fields.Date(string="Date of birth",tracking =True)
    age = fields.Char(string="Age",compute='_compute_age',store=True,tracking =True)
    email = fields.Char(string="email")
    password = fields.Char(string="password")
    address = fields.Char(string="Address",tracking =True)
    standard = fields.Char(string="Class",tracking =True)
    teacher_mob = fields.Char(string="Teacher Mobile",tracking =True)
    class_teacher = fields.Many2one('school.teacher', string="class_teacher",tracking =True)

    fee_structure_ids = fields.One2many('fees.structure', 'student_id', string='Fees Structures',
                                        help="Related Fees Structure")
    total_amount = fields.Float(string="Total Fees Amount", compute='_compute_total_amount', store=True,tracking =True)
    un_taxed_amount = fields.Float(string="Total Un Taxed Amount",compute='_compute_total_amount', store=True,tracking =True)
    total_tax_amount = fields.Float(string="Total Tax Amount",compute='_compute_total_amount', store=True,tracking =True)

    teacher_ids = fields.Many2many(
        'school.teacher', string="Other Subject Teachers",
        help='Mention the teachers who teach other subjects.')

    select_status = fields.Selection([('draft', 'Draft'), ('admitted', 'Admitted')],
                                     default='draft')
    suggestion_count = fields.Integer(string="Suggestion Count", compute='compute_suggestion_count')
    user_id = fields.Many2one('res.users',string="Login User")

    @api.depends('fee_structure_ids.total_amount','fee_structure_ids.tax_amount','fee_structure_ids.untaxed_amount','total_amount','un_taxed_amount')
    def _compute_total_amount(self):
        for student in self:
            student.total_amount = sum(fee_structure.total_amount for fee_structure in student.fee_structure_ids)
            student.un_taxed_amount = sum(fee_structure.untaxed_amount for fee_structure in student.fee_structure_ids)
            student.total_tax_amount = student.total_amount - student.un_taxed_amount





    def action_select(self):
        self.select_status = 'admitted'
        template = self.env.ref("school_management.student_create_email_template")
        for rec in self:
            template.send_mail(rec.id)





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
            (print("Hai"))
            student_exist = self.env["school.student"].search([('guardian_phone', "=", vals['guardian_phone'])])
            if student_exist:
                raise ValidationError("There is already a student with the same phone number")
            return super(SchoolStudent, self).create(vals)


    def action_suggestion(self):
        template = self.env.ref("school_management.student_create_email_template")

        return {
            'name': _('Suggestions'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'school.student.suggestion',
            'target' : 'new',
        }





    def create_user(self):
        user_vals = {
            'name':self.student_name,
            'login': self.student_name,
            'email':self.email,
            'password': self.student_name,

        }

        new_user = self.env['res.users'].create(user_vals)
        for rec in self:
            rec.user_id = new_user.id


    def action_open_suggestion(self):
        return {
            'name': _('Suggestion'),
            'type': 'ir.actions.act_window',
            'res_model': 'suggestions.main',
            'view_mode': 'tree,form',
            'domain': [('name', '=', self.student_name)],
            # 'target': 'new',
        }


    def compute_suggestion_count(self):
        for rec in self:
            suggestion_count = self.env['suggestions.main'].search_count([('name', '=', rec.student_name)])
            rec.suggestion_count = suggestion_count



