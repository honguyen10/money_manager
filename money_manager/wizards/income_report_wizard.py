
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class IncomeReportWizard(models.TransientModel):
    _name = "income.report.wizard"

    partner_id = fields.Many2one('res.partner', string='User Name')
    account_id = fields.Many2one('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]")

    def select_income_report_account(self):
        return {
            'name':'Update Quantity',
            'view_mode': 'graph',
            'view_id': self.env.ref('money_manager.money_income_report_action').id,
            # 'view_type': 'graph',
            'res_model': 'money.income',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'domain': [],
            # 'context': {'default_book_id': self.id}
        }
