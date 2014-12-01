# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2014- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Finnish industry classification',
    'category': 'CRM',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',    
    'depends': ['crm'],
    'description': '''
- Adds the finnish industry classification hierarchy
- Allows partner to have an industry
- TODO: category hierarcy, industry categories
''',
    'data': [
        'data/industry_class.xml',
        'data/industry_category.xml',
        'data/industry_industry.xml',
        'view/res_partner.xml',
        'view/business_industry_class.xml',
        'view/business_industry_category.xml',
        'view/business_industry_industry.xml',
        'view/industry_menu.xml',
        #'security/ir.model.access.csv',
    ],
}
