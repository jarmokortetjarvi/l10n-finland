# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

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
            ('filter_no', 'No Filters'),
            ('filter_date', 'Date'),
            ('filter_period', 'Periods'),
            ('filter_analytic', 'Analytic account'),
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
        filter = self.filter
        if self.filter == 'filter_analytic':
            # Use filter_no to get default values
            filter = 'filter_no'

        res = super(AccountingReport, self).onchange_filter(filter, self.fiscalyear_id.id)

        return res

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods