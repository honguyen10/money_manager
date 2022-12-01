
from odoo import api, fields, models, _
from datetime import datetime


class ReportWizard(models.TransientModel):
    _name = "report.wizard"

    partner_id = fields.Many2one('res.partner', string='User Name')
    account_id = fields.Many2one('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]")
    date_from = fields.Date(string='From', default=datetime.today())
    date_to = fields.Date(string='To', default=datetime.today())

    def select_income_report_wizard(self):
        domain = [
            ('partner_id', '=', self.partner_id.id),
            ('account_id', '=', self.account_id.id),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
            ]
        return {
            'name': 'Income Report',
            'view_mode': 'graph',
            'view_id': self.env.ref('money_manager.money_income_graph_view').id,
            'res_model': 'money.income',
            'type': 'ir.actions.act_window',
            'domain': domain,
        }
