from odoo import models, fields

class ShipdaySyncQueue(models.Model):
    _name = 'shipday.sync.queue'
    _description = 'Cola de sincronización Shipday'

    sale_order_id = fields.Many2one('sale.order', string='Pedido de Venta', required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('pending', 'Pendiente'),
        ('done', 'Hecho'),
        ('failed', 'Fallido'),
    ], string='Estado', default='draft')
    error_message = fields.Text(string='Mensaje de Error')
