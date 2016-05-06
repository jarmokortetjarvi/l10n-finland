# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountMoveLine(models.Model):

    # 1. Private attributes
    _inherit = 'account.move.line'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def _query_get(self, obj='l'):
        res = super(AccountMoveLine, self)._query_get(obj)

        if self._context.get('analytic_account_ids'):
            params = ','.join(str(e) for e in self._context['analytic_account_ids'])

            query = ' AND l.analytic_account_id IN (%s)' % params

            res += query

        return res
