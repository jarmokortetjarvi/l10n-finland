# -*- coding: utf-8 -*-
from openerp import models, api, fields

class ResPartner(models.Model):
    
    _inherit = 'res.partner'
    
    country_id = fields.Many2one(default=lambda self: self.country_id.search([('code', '=', 'FI')]))
    lang = fields.Selection(default='fi_FI')
    #property_payment_term = fields.Many2one(default=lambda self: self.env['account.payment.term'].search([('name', '=', '14 Days')]))
    #property_supplier_payment_term = fields.Many2one(default=lambda self: self.env['account.payment.term'].search([('name', '=', '14 Days')]))
    
    @api.onchange('lang')
    def lang_onchange(self):
        ''' We are updating these with lang onchange (because its always set on create), 
            as the preceding field defaults (commented out) aren't working for some reason '''

        if not self.property_payment_term:
            self.property_payment_term = self.env['account.payment.term'].search([('code', '=', '14_days')])
        
        if not self.property_supplier_payment_term:
            self.property_supplier_payment_term = self.env['account.payment.term'].search([('code', '=', '14_days')])