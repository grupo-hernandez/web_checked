# -*- coding: utf-8 -*-
{
    'name': 'Check terms and conditions in e-commerce',
    'version': '16.0.1',
    'summary': """ Odoo by default always unmarks that field terms and conditions in e-commerce. With this module you choose if you want to mark it. """,
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