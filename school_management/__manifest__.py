{
    'name': "School Managemet",
    'summary': "Helps to manage the school details",
    'version': '2.0',
    'depends': ["sale", "mail", "account",

                ],
    'auto_install': [],
    'data': ["security/ir.model.access.csv",
             "security/school_security.xml",
             "views/student_view.xml",
             "data/school_email_template.xml",
             "records/reports.xml",
             "records/school_student_report.xml",
             "views/teacher_view.xml",
             "views/query_view.xml",
             "views/sale_view.xml",
             "views/inovice_view.xml",
             "views/invoice_line.xml",
             "views/suggestions_main_view.xml",
             "wizard/student_suggestion_view.xml",
             "views/school_menu.xml",

             ],

    'license': 'LGPL-3',
}
