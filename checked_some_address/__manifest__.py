# -*- coding: utf-8 -*-
{
    'name': 'Check send to the some address in e-commerce',
    'version': '16.0.1',
    'summary': """ Odoo by default always marks that field as checked. With this module you choose if you want to mark it.""",
    'author': 'Grupo Hernandez S.U.R.L',
    'website': 'www.grupohernandez.cu',
    'category': 'Website/Website',
    'depends': ['base', 'website_sale'],
    'data': [
        'views/templates.xml',
        'views/res_config_setting.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
