# -*- coding: utf-8 -*-
from openerp import models, api, fields

class ResPartner(models.Model):
    
    _inherit = 'res.partner'
    
    country_id = fields.Many2one('res.country', default=lambda self: self.country_id.search([('code', '=', 'FI')]))