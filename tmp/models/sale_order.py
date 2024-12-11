from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            self.env['shipday.sync.queue'].create({
                'sale_order_id': order.id,
                'state': 'pending',
            })
        return res
