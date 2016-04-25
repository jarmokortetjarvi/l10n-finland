# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountingReport(models.TransientModel):

    # 1. Private attributes
    _inherit = 'accounting.report'

    # 2. Fields declaration
    analytic_account = fields.Many2one(
        'account.analytic.account',
        string="Analytic account",
        domain=[('type', '=', 'normal')],
    )

    # 3. Default methods
    @api.model
    def default_get(self, fields):
        # Get the correct financial report as default
        res = super(AccountingReport, self).default_get(fields)

        if 'report_code' in self._context:
            user =  self.env['res.users'].browse(self._uid)

            report = self.env['account.financial.report'].search([
                ('company', '=', user.company_id.id),
                ('code', '=', self._context['report_code'])
            ])

            res['account_report_id'] = report.id

        return res

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.one
    @api.onchange('analytic_account')
    def onchange_analytic_account(self):
        res = {}

        if self.analytic_account:
            res['analytic_account'] = self.analytic_account

        return res

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.multi
    def check_report(self):
        for record in self:
            res = super(AccountingReport, record).check_report()

            # Set an empty variable for parsing
            res['data']['form']['analytic_account'] = ''

            if record.analytic_account:
                res['data']['form']['analytic_account'] = record.analytic_account.name

                analytic_accounts = record._get_analytic_accounts_recursive(record.analytic_account)
                analytic_accounts.append(record.analytic_account.id)

                res['data']['form']['used_context']['analytic_account_ids'] = analytic_accounts

            return res

    def _get_analytic_accounts_recursive(self, analytic_account):
        child_ids = []

        for child in analytic_account.search([('parent_id', '=', analytic_account.id)]):
            child_ids.append(child.id)

            if analytic_account.search([('parent_id', '=', child.id)]):
                child_ids += self._get_analytic_accounts_recursive(child)

        return child_ids
