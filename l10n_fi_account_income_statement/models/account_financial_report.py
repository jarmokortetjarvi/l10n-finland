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


class AccountFinancialReport(models.Model):
    
    # Constants:
    # Use underscore uppercase notation for global variables or constants.

    # 1. Private attributes
    _inherit = 'account.financial.report'

    # 2. Fields declaration
    code = fields.Char('Unique code')
    company = fields.Many2one('res.company', 'Company')

    # 3. Default methods

    # 4. compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    ''' When the module is installed,
    fetch all companies and create income statements '''
    @api.model
    def _init_income_statement_reports(self):
        companies = self.company.search([])
        
        for company in companies:
            self._delete_internal_income_statement_report(company)
            self._create_internal_income_statement_report(company)
    
    def _delete_internal_income_statement_report(self, company):
        reports = self.search([
            ('company', '=', company.id),
            '|', 
            ('code','=','STU'),
            ('parent_id.code','=','STU')
        ])
        reports.unlink()
    
    def _create_internal_income_statement_report(self, company):
        # The report header
        internal_statement_report = self.create({
            'company': company.id,
            'code': 'STU',
            'name': 'Sisäinen Tuloslaskelma (%s)' % company.name
        })
        
        # Turnover
        self.create({
            'company': company.id,
            'code': 'STUMT',
            'name': 'Liikevaihto',
            'type': 'accounts',
            'display_detail': 'detail_with_hierarchy',
            'parent_id': internal_statement_report.id,
        })