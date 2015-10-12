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
    
    # Variable names:
    # Use underscore lowercase notation for common variable (snake_case)
    # since new API works with record or recordset instead of id list, 
    # don't suffix variable name with _id or _ids if they do not contain 
    # an id or a list of ids.
   
    # Constants:
    # Use underscore uppercase notation for global variables or constants.

    # 1. Private attributes
    _name = 'account.financial.report'

    # 2. Fields declaration
    company = fields.Many2one('res.company', 'Company')

    # 3. Default methods

    # 4. compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    ''' When module is installed, fetch all companies and create income statements '''
    def _init_income_statement_reports(self):
        
        companies = self.company.search()
        
        for company in companies:
            print company.name
        
        return True
    