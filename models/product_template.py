# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductTemplate(models.Model):

    # 1. Private attributes
    _inherit = 'product.template'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def init_attributes(self):
        # Get taxes
        self.taxes = self._get_taxes()

        # Get all products in the category
        products = self.search([('categ_id.name', '=', 'Viranomaistuotteet')])

        for product in products:
            self._update_product_attributes(product)

    def _get_taxes(self):
        taxes = dict()

        taxes['tax_purchase_0'] = 'Osto ALV 0%'
        taxes['tax_purchase_14'] = 'Osto ALV 14%'
        taxes['tax_purchase_24'] = 'Osto ALV 24%'

        return taxes

    def _search_tax(self, code, company):
        name = self.taxes[code]

        tax = self.env['account.tax'].search(
            [
                ('name', '=', name),
                ('company_id', '=', company.id),
            ],
            limit=1)

        return tax

    def _search_account(self, code, company):
        # TODO: Should this be more strict?

        account = self.env['account.account'].search(
            [
                ('code', 'like', code),
                ('company_id', '=', company.id),
            ],
            limit=1)

        return account

    def _update_product_attributes(self, product):
        external_id_dict = product.get_external_id()

        if product.id in external_id_dict:
            external_id = external_id_dict[product.id]
        else:
            return False

        if external_id == 'l10n_fi_product_authority.product_template_ammattikirjallisuus':
            product.property_account_expense = self._search_account('8460', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)
