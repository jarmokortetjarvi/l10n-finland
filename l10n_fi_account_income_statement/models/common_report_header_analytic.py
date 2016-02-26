

class common_report_header_analytic(object):

    def get_analytic_account(self, data):
        if data.get('form', False) and data['form'].get('analytic_account', False):
            return self.pool.get('account.analytic.account').browse(self.cr,self.uid,data['form']['analytic_account']).name
        return ''
