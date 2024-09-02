from odoo import fields,models
from odoo.exceptions import ValidationError

class SchoolQuery(models.Model):
    _name = 'school.query'
    _rec_name = "child_name"
    child_name = fields.Char(string="Child Name")
    parent_mob = fields.Char(string="Parent Mobile")
    parent_name = fields.Char(string="Parent Name")
    child_date_of_birth = fields.Date(string="Child DOB")
    child_class = fields.Char(string="Class")
    admission_status = fields.Selection([('draft', 'Draft'), ('admitted', 'Admitted')],
                                     default='draft')

    #function for admission status
    def action_admit(self):
        self.admission_status = 'admitted'


#function for creating a student through query using a button
    def student_creation(self):
        student_ids = self.env['school.student'].search([('guardian_phone','=',self.parent_mob)])
        print(student_ids)
        if student_ids:
            raise ValidationError("there is a student with the same mobile number")

        student = self.env['school.student'].create({
         'student_name':self.child_name,
        'guardian_name':self.parent_name,
        'select_status':self.admission_status,
        'date_of_birth':self.child_date_of_birth
        })



#merg two functions into one

    def combined(self):
        self.action_admit()
        self.student_creation()
