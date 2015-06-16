# -*- coding: utf-8 -*-
from openerp import models, api, fields

class PaymentTerm(models.Model):
    
    _inherit = 'account.payment.term'
    _order = 'sequence, name'
    
    sequence = fields.Integer('Sequence')