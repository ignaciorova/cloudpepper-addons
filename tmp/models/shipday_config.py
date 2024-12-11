from odoo import models, fields

class ShipdayConfig(models.Model):
    _name = 'shipday.config'
    _description = 'Configuración de Shipday'

    name = fields.Char(string='Nombre', default='Configuración Shipday')
    api_key = fields.Char(string='Clave API', required=True)
    endpoint_url = fields.Char(string='URL de la API', default='https://api.shipday.com')
    active = fields.Boolean(string='Activo', default=True)
