from openerp.osv import osv, fields
from openerp.tools.translate import _

    
class Partner(osv.Model):      

    _inherit = "res.partner"
    _name = "res.partner"
    
    _columns = {
        'business_industry':  fields.many2one('business_industry.industry', string='Business industry'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
