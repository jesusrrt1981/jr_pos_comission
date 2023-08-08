# -*- coding: utf-8 -*-


{
    'name': "Jr POS Commission",
    'license': 'AGPL-3',
    'description': """
""",
    'version': '16.0.1.0',
    'depends': ['base', 'point_of_sale', 'hr'],
    'data': [
        'views/hr_employee.xml',
        'views/pos_order_line.xml',
        'views/reporte_pos.xml',
        'security/ir.model.access.csv',
    ],

    'assets': {
        'point_of_sale.assets': [
            'jr_pos_comission/static/src/js/db.js',
            'jr_pos_comission/static/src/js/models.js',
            'jr_pos_comission/static/src/js/OrderLine.js',
            'jr_pos_comission/static/src/xml/OrderLine.xml',
        ],

    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
