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
        taxes['tax_purchase_10'] = 'Osto ALV 10% (sis. hintaan)'
        taxes['tax_purchase_14'] = 'Osto ALV 14% (sis. hintaan)'
        taxes['tax_purchase_24'] = 'Osto ALV 24% (sis. hintaan)'

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

        # Kirjallisuus
        if external_id == 'l10n_fi_product_authority.product_template_ammattikirjallisuus':
            product.property_account_expense = self._search_account('8460', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # ATK
        elif external_id == 'l10n_fi_product_authority.product_template_atk_tarvikkeiden_pienhankinnat':
            product.property_account_expense = self._search_account('7690', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Auton huolto ja tarvikkeet
        elif external_id == 'l10n_fi_product_authority.product_template_auton_huolto_ja_korjaus':
            product.property_account_expense = self._search_account('7540', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_autotarvikkeet_24':
            product.property_account_expense = self._search_account('7550', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Edustus
        elif external_id == 'l10n_fi_product_authority.product_template_edustuskulut':
            product.property_account_expense = self._search_account('7994', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_edustuslahjat':
            product.property_account_expense = self._search_account('7964', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Internet
        elif external_id == 'l10n_fi_product_authority.product_template_internetkulut_24':
            product.property_account_expense = self._search_account('8530', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Kahvitarvikkeet
        elif external_id == 'l10n_fi_product_authority.product_template_kahvitarvikkeet_14':
            product.property_account_expense = self._search_account('7111', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_14', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_kahvitarvikkeet_24':
            product.property_account_expense = self._search_account('7110', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Kalusto ja kalusteet
        elif external_id == 'l10n_fi_product_authority.product_template_kalusto_24':
            product.property_account_expense = self._search_account('1170', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_kaytetyt_kalusteet_0':
            product.property_account_expense = self._search_account('1201', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Kilometrikorvaukset
        elif external_id == 'l10n_fi_product_authority.product_template_kilometrikorvaus_2015':
            product.property_account_expense = self._search_account('7874', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_kilometrikorvaus_2016':
            product.property_account_expense = self._search_account('7874', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_kilometrikorvauksen_korotus_1':
            product.property_account_expense = self._search_account('7874', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_kilometrikorvauksen_korotus_perakarry':
            product.property_account_expense = self._search_account('7874', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Päivärahat
        elif external_id == 'l10n_fi_product_authority.product_template_kotimaan_osapaivaraha_2015':
            product.property_account_expense = self._search_account('7884', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)
        elif external_id == 'l10n_fi_product_authority.product_template_kotimaan_osapaivaraha_2016':
            product.property_account_expense = self._search_account('7884', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_kotimaan_paivaraha_2015':
            product.property_account_expense = self._search_account('7884', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)
        elif external_id == 'l10n_fi_product_authority.product_template_kotimaan_paivaraha_2016':
            product.property_account_expense = self._search_account('7884', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Lahjat hlökunnalle
        elif external_id == 'l10n_fi_product_authority.product_template_lahja_henkilokunnalle':
            product.property_account_expense = self._search_account('7160', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Mainostarvikkeet
        elif external_id == 'l10n_fi_product_authority.product_template_mainostarvikkeet':
            product.property_account_expense = self._search_account('8120', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Marjoitus
        elif external_id == 'l10n_fi_product_authority.product_template_majoitus_10':
            product.property_account_expense = self._search_account('7822', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_10', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_majoitus_ulkomaat':
            product.property_account_expense = self._search_account('7824', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Matkaliput
        elif external_id == 'l10n_fi_product_authority.product_template_matkaliput_0':
            product.property_account_expense = self._search_account('7804', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_matkaliput_10':
            product.property_account_expense = self._search_account('7802', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_10', product.company_id)

        # Neuvottelukulut
        elif external_id == 'l10n_fi_product_authority.product_template_neuvottelukulut_0':
            product.property_account_expense = self._search_account('8654', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_neuvottelukulut_14':
            product.property_account_expense = self._search_account('8651', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_14', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_neuvottelukulut_24':
            product.property_account_expense = self._search_account('8650', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Paikoituskulut
        elif external_id == 'l10n_fi_product_authority.product_template_paikoituskulut_0':
            product.property_account_expense = self._search_account('7854', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_paikoituskulut_24':
            product.property_account_expense = self._search_account('7850', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Polttoaine
        elif external_id == 'l10n_fi_product_authority.product_template_polttoaine':
            product.property_account_expense = self._search_account('7534', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Posti
        elif external_id == 'l10n_fi_product_authority.product_template_postikulut_0':
            product.property_account_expense = self._search_account('8544', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_postikulut_24':
            product.property_account_expense = self._search_account('8540', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Puhelin
        elif external_id == 'l10n_fi_product_authority.product_template_puhelinkulu_24':
            product.property_account_expense = self._search_account('8500', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Sis. palaveri
        elif external_id == 'l10n_fi_product_authority.product_template_sisaisen_palaverin_kulut':
            product.property_account_expense = self._search_account('7010', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)

        # Taksi
        elif external_id == 'l10n_fi_product_authority.product_template_taksikulut_0':
            product.property_account_expense = self._search_account('7814', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        elif external_id == 'l10n_fi_product_authority.product_template_taksikulut_10':
            product.property_account_expense = self._search_account('7812', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_10', product.company_id)

        # Toimilupien rekisteröinnit
        elif external_id == 'l10n_fi_product_authority.product_template_toimiluvat_rekisteroinnit_0':
            product.property_account_expense = self._search_account('8444', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_0', product.company_id)

        # Toimistotarvikkeet
        elif external_id == 'l10n_fi_product_authority.product_template_toimistotarvikkeet_24':
            product.property_account_expense = self._search_account('8620', product.company_id)
            product.supplier_taxes_id = self._search_tax('tax_purchase_24', product.company_id)
