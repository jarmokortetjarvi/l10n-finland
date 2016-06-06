# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountFinancialReport(models.Model):
    
    # Constants:
    # Use underscore uppercase notation for global variables or constants.

    # 1. Private attributes
    _inherit = 'account.financial.report'

    # 2. Fields declaration
    code = fields.Char('Unique code')
    company = fields.Many2one('res.company', 'Company')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods

    @api.model
    def _init_income_statement_reports(self):
        # When the module is installed,
        # fetch all companies and create income statements
        companies = self.company.search([])
        
        for company in companies:
            self._delete_internal_income_statement_report(company)
            self._create_internal_income_statement_report(company)
            
            self._delete_external_income_statement_report(company)
            self._create_external_income_statement_report(company)
            
            self._delete_balance_sheet_report(company)
            self._create_balance_sheet_report(company)
     
    def _delete_internal_income_statement_report(self, company):
        reports = self.search([
            ('company', '=', company.id),
            '|', '|',
            ('code', '=', 'STU'),
            ('parent_id.code', '=', 'STU'),
            ('parent_id.parent_id.code', '=', 'STU')
        ])
        
        # Remote related accounting reports
        self.env['accounting.report'].search([
            ('account_report_id', 'in', reports.ids)
        ]).unlink()
        
        reports.unlink()

    def _delete_external_income_statement_report(self, company):
        reports = self.search([
            ('company', '=', company.id),
            '|', '|',
            ('code', '=', 'UTU'),
            ('parent_id.code', '=', 'UTU'),
            ('parent_id.parent_id.code', '=', 'UTU')
        ])
        
        # Remote related accounting reports
        self.env['accounting.report'].search([
            ('account_report_id', 'in', reports.ids)
        ]).unlink()
        
        reports.unlink()
        
    def _delete_balance_sheet_report(self, company):
        reports = self.search([
            ('company', '=', company.id),
            '|', '|',
            ('code','=', 'TASE'),
            ('parent_id.code', '=', 'TASE'),
            ('parent_id.parent_id.code', '=', 'TASE')
        ])
        
        # Remote related accounting reports
        self.env['accounting.report'].search([
            ('account_report_id', 'in', reports.ids)
        ]).unlink()
        
        reports.unlink()
     
    ## CREATE METHODS
        
    def _create_internal_income_statement_report(self, company):
        account = self.env['account.account'].search([
            ('company_id', '=', company.id),
            ('code', 'in', ['TULOS'])
        ])

        self.create({
            'company': company.id,
            'code': 'STU',
            'name': 'Sisäinen Tuloslaskelma',
            'type': 'accounts',
            'sequence': '10',
            'display_detail': 'detail_with_hierarchy',
            'sign': -1,
            'account_ids': [(6, 0, account.ids)]
        })

    def _create_external_income_statement_report(self, company):
        # The report header
        report_header = self.create({
            'company': company.id,
            'code': 'UTU',
            'name': 'Ulkoinen Tuloslaskelma'
        })
        
        ## Profit / Loss
        report_profit = self.create({
            'company': company.id,
            'code': 'UTULOS',
            'name': 'Tulos',
            'type': 'sum',
            'sequence': '10',
            'sign': -1,
            'parent_id': report_header.id,
        })
        
        ## Turnover
        report_turnover = self.create({
            'company': company.id,
            'code': 'UTUT',
            'name': 'Liikevaihto',
            'type': 'sum',
            'sequence': '10',
            'display_detail': 'detail_flat',
            'sign': -1,
            'parent_id': report_profit.id,
        })
        
        ### Sales
        accounts = self.env['account.account'].search([
            ('company_id', '=', company.id),
            ('code', 'in', ['TUMT', 'TULT'])
        ])

        for account in accounts:
            self.create({
                'company': company.id,
                'code': 'U%s' % account.code,
                'name': account.name,
                'type': 'accounts',
                'sequence': '10',
                'display_detail': 'detail_flat',
                'sign': -1,
                'parent_id': report_turnover.id,
                'account_ids': [(6, 0, account.ids)]
            })
        
        ## Expenses
        report_expenses = self.create({
            'company': company.id,
            'code': 'UTUE',
            'name': 'Kulut',
            'type': 'sum',
            'sequence': '100',
            'display_detail': 'detail_flat',
            'sign': -1,
            'parent_id': report_profit.id,
        })
        
        accounts = self.env['account.account'].search([
            ('company_id', '=', company.id),
            ('code', 'in', [
                'TUHK',  # Henkilöstökulut
                'TULK',  # Liiketoiminnan muut kulut
                'TULT',  # Liiketoiminnan muut tuotot
                'TUMP',  # Materiaalit ja palvelut
                'TUOV',  # Osuus osakkuuyritysten voitosta (tappiosta)
                'TUPA',  # Poistot ja arvonalentumiset
                'TUES',  # Tulos ennen satunnaisia eriä
                'TUET',  # Tulos ennen tilinpäätössiirtoja ja veroja
                'TURR',  # Rahoitustuotot ja -kulut
            ])
        ])

        for account in accounts:
            self.create({
                'company': company.id,
                'code': 'U%s' % account.code,
                'name': account.name,
                'type': 'accounts',
                'sequence': '110',
                'display_detail': 'detail_flat',
                'sign': -1,
                'parent_id': report_expenses.id,
                'account_ids': [(6, 0, account.ids)]
            })
            
    def _create_balance_sheet_report(self, company):
        ## ASSETS AND LIABILITIES
        report_header = self.create({
            'company': company.id,
            'code': 'TASE',
            'name': 'Tase',
            'type': 'sum',
            'sequence': '10',
            'display_detail': 'detail_flat',
        })

        tavv = self.env['account.account'].search([
            ('company_id', '=', company.id),
            ('code', 'in', ['TAVV'])
        ])
        self.create({
            'company': company.id,
            'code': 'TAVV',
            'name': 'VASTAAVAA',
            'type': 'accounts',
            'sequence': '10',
            'display_detail': 'detail_with_hierarchy',
            'parent_id': report_header.id,
            'account_ids': [(6, 0, tavv.ids)]
        })

        tavt = self.env['account.account'].search([
            ('company_id', '=', company.id),
            ('code', 'in', ['TAVT'])
        ])
        self.create({
            'company': company.id,
            'code': 'TAVT',
            'name': 'VASTATTAVAA',
            'type': 'accounts',
            'sequence': '20',
            'display_detail': 'detail_with_hierarchy',
            'parent_id': report_header.id,
            'account_ids': [(6, 0, tavv.ids)]
        })
