# -*- coding: utf-8 -*-

# 1. Standard library imports:
#    import base64

# 2. Known third party imports (One per line sorted and splitted in python stdlib):
#    import lxml

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules (rarely, and only if necessary):
#    from openerp.addons.website.models.website import slug

# 5. Local imports in the relative form:
#    from . import utils

# 6. Unknown third party imports (One per line sorted and splitted in python stdlib):
#    _logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    
    # 1. Private attributes
    _inherit = 'account.move.line'

    # 2. Fields declaration
    account_order = fields.Integer(
        'Account order',
        compute='_get_account_order',
        store=True
    )
    account_code = fields.Char(
        'Account code',
        compute='_get_account_code',
        store=True
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends('account_id')
    def _get_account_order(self):
        for record in self:
            record.account_order = record.account_id.parent_left
            
    @api.depends('account_id')
    def _get_account_code(self):
        for record in self:
            record.account_code = record.account_id.code

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
