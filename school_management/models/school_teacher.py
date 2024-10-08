from odoo import fields,models


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _rec_name = "name"
    name = fields.Char(string="Full name", required=True)
    mobile = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address")
    date_of_birth = fields.Date(string="Date of birth")
    is_a_teacher =fields.Boolean()
    add_student = fields.One2many('school.student','class_teacher',string="Add Student")
    permanent= fields.Selection([('temporary', 'Temporary'), ('permanent', 'Permanent')],
                                     default='temporary')
    user_id = fields.Many2one('res.users', string="Login User")

    def action_permanent(self):
        self.permanent = 'permanent'


    def create_user(self):
        user_vals = {
            'name':self.name,
            'login': self.name,
            'email':self.name,
            'password': self.name,

        }
        user = self.env['res.users'].create(user_vals)
        return user