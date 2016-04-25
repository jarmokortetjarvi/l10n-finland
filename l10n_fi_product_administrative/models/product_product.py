# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductProduct(models.Model):

    # 1. Private attributes
    _inherit = 'product.product'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def init_taxes(self):
        # Get the taxes
        taxes_id = self.env['account.tax'].search(
            [('name', '=', 'Myynti ALV 24%')],
            limit=1
        )
        supplier_taxes_id = self.env['account.tax'].search(
            [('name', '=', 'Osto ALV 24%')],
            limit=1,
        )

        # Get all products in the category
        products = self.search([('categ_id.name', '=', 'Hallinnolliset')])

        for product in products:
            product.taxes_id = taxes_id
            product.supplier_taxes_id = supplier_taxes_id
