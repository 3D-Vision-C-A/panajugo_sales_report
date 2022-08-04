from odoo import fields, models, api

class AccountMove(models.Model):

    _inherit = 'account.move'

    def print_pj_account_move_report(self):
        return self.env.ref('panajugo_sales_report.action_pj_report').report_action(self)
