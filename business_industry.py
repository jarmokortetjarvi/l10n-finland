from openerp.osv import osv, fields
from openerp.tools.translate import _

class Business_industry_class(osv.Model):
    
    _name = 'business_industry.class'
    _order = "code"
    
    _columns = {
        'name': fields.char(string='Class name', size=512),
        'code': fields.char(string='Class code', size=1),
    }
    
    _sql_constraints = [
        ('code_unique', 'unique(code)', _('The business industry main class code has to be unique'))
    ]

class Business_industry_category(osv.Model):      
    _name = "business_industry.category"
    _order = "code, name"
    
    _columns = {
        'name': fields.char(string='Category name', size=512),
        'code': fields.char(string='Category code', size=4),
        'industry_class':  fields.many2one('business_industry.class', string='Main class'),
        
        'parent_id': fields.many2one('business_industry.category', 'Parent Role', select=True, ondelete='cascade'),
        'child_ids': fields.one2many('business_industry.category', 'parent_id', 'Child Roles'),
        'parent_left': fields.integer('Left parent', select=True),
        'parent_right': fields.integer('Right parent', select=True),
    }
    _constraints = [
        (osv.osv._check_recursion, 'Error ! You can not create recursive categories.', ['parent_id'])
    ]
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'
    

class Business_industry(osv.Model):      

    _name = "business_industry.industry"
    _order = "code"
    
    _columns = {
        'name': fields.char(string='Industry name', size=512),          
        'code': fields.char(string='Industry code', size=6),          
        'category':  fields.many2one('business_industry.category', string='Industry category'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
