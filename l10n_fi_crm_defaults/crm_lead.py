# -*- coding: utf-8 -*-
from openerp import models, api, fields


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    @api.model
    def default_get(self, fields):
        res = super(CrmLead, self).default_get(fields)

        country_id = self.country_id.search([('code', '=', 'FI')]).id

        res['country_id'] = country_id

        return res
