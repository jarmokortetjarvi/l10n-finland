from openerp.osv import osv, fields
from openerp.tools.translate import _

class Business_industry_category(osv.Model):
    
    _name = "business_industry.category"
    _order = "industry_class, code"
    
    def name_get(self, cr, uid, ids, context=None):
        res = []
        for record in self.browse(cr, uid, ids, context):
            name ='[%s] %s' % (record.code, record.name)
            res.append((record.id, name))
        
        return res
    
    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=20):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            ids = self.search(cr, uid, ['|',('name', operator, name),('code', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)
    
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