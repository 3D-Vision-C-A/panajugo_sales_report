# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'PJ Report',
    'version': '1.0.0',
    'depends': ['base','account'],
    'description': 'Report module for Pana Jugo',
    'summary': 'Sales Report',
    'license' : 'LGPL-3',
    'application' : True,
    'installable' : True,
    'data': [
        'report/pj_report.xml',
        'report/pj_report_view.xml',
        'views/account_out_invoice.xml',
    ]
}