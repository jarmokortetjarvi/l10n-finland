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

    filter = fields.Selection(
        [
            ('filter_no', _('No Filters')),
            ('filter_date', _('Date')),
            ('filter_period', _('Periods')),
            ('filter_analytic', _('Analytic account')),
        ],
        "Filter by",
        required=True
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
    @api.onchange('filter')
    def onchange_filter(self):
        used_filter = self.filter
        if self.filter == 'filter_analytic':
            # Use filter_no to get default values
            used_filter = 'filter_no'

        res = super(AccountingReport, self).onchange_filter(used_filter, self.fiscalyear_id.id)

        if self.filter == 'filter_analytic':
            res['analytic_account'] = self.analytic_account

        return res

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.multi
    def check_report(self):
        res = super(AccountingReport, self).check_report()

        if res['data']['form']['filter'] == 'filter_analytic':
            res['data']['form']['analytic_account'] = self.analytic_account.name
            res['data']['form']['used_context']['analytic_account_ids'] = [self.analytic_account.id]

        return res
