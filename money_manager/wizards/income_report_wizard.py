
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class IncomeReportWizard(models.TransientModel):
    _name = "income.report.wizard"

    partner_id = fields.Many2one('res.partner', string='User Name')
    account_id = fields.Many2one('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]")

    def select_income_report_account(self):
        domain = [('partner_id', '=', self.partner_id.id), ('account_id', '=', self.account_id.id)]
        return {
            'name': 'Income Report',
            'view_mode': 'graph',
            'view_id': self.env.ref('money_manager.money_income_graph_view').id,
            'res_model': 'money.income',
            'type': 'ir.actions.act_window',
            'domain': domain,
            'context': {},
        }
