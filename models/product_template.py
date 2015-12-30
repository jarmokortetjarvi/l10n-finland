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
    def init_taxes(self):
        # Get all products in the category
        products = self.search([('categ_id.name', '=', 'Viranomaistuotteet')])

        tax_purchase_0 = self._search_tax('Osto ALV 0%')
        tax_purchase_14 = self._search_tax('Osto ALV 14%')
        tax_purchase_24 = self._search_tax('Osto ALV 24%')

        for product in products:
            external_id_dict = product.get_external_id()

            if product.id in external_id_dict:
                external_id = external_id_dict[product.id]
            else:
                continue

    def _search_tax(self, name):
        tax = self.env['account.tax'].search(
            [
                ('name', '=', name),
                ('company_id', '=', self.company_id.id),
            ],
            limit=1)

        return tax
