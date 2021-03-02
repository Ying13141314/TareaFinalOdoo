# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Módulo de gestión de un hospital """,

    'description': """
        Un establecimiento destinado para la atención y asistencia a enfermos por medio de personal médico, 
        enfermería, personal auxiliar y de servicios técnicos durante 24 horas, 365 días del año y disponiendo de tecnología, 
        aparatología, instrumental y farmacología adecuadas.
    """,

    'author': "Ying Lin",
    'website': "https://ciclo.iespablopicasso.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
