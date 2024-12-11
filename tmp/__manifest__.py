{
    'name': 'Shipday Connector',
    'version': '18.0.1.0.0',
    'author': 'Tu Nombre',
    'license': 'LGPL-3',
    'category': 'Shipping',
    'depends': ['connector', 'sale_management'],
    'data': [
        'views/shipday_settings_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
