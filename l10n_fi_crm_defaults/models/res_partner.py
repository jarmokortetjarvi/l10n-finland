# -*- coding: utf-8 -*-
from openerp import models, api, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    country_id = fields.Many2one(
        default=lambda self:
        self.country_id.search([('code', '=', 'FI')]))
    lang = fields.Selection(default='fi_FI')

    @api.model
    def default_get(self, fields):
        res = super(ResPartner, self).default_get(fields)

        payment_term = self.env['account.payment.term'].\
            search([('code', '=', '14_days')], limit=1).id

        res['property_payment_term'] = payment_term
        res['property_supplier_payment_term'] = payment_term

        return res
