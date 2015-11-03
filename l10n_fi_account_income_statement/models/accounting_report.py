# -*- coding: utf-8 -*-

# 1. Standard library imports:
#	import base64

# 2. Known third party imports (One per line sorted and splitted in python stdlib):
#	import lxml

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules (rarely, and only if necessary):
#	from openerp.addons.website.models.website import slug

# 5. Local imports in the relative form:
#	from . import utils

# 6. Unknown third party imports (One per line sorted and splitted in python stdlib):
#	_logger = logging.getLogger(__name__)


class AccountingReport(models.TransientModel):
    _inherit='accounting.report'
    
    @api.model
    def default_get(self, fields):
        ''' Get the correct financial report as default '''
        res = super(AccountingReport, self).default_get(fields)

        if 'report_code' in self._context:
            user =  self.env['res.users'].browse(self._uid)
            
            report = self.env['account.financial.report'].search([
                ('company', '=', user.company_id.id),
                ('code', '=', self._context['report_code'])
            ])
        
            res['account_report_id'] = report.id

        return res
