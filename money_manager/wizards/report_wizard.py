
from odoo import api, fields, models, _
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ReportWizard(models.TransientModel):
    _name = "report.wizard"

    partner_id = fields.Many2one('res.partner', string='User Name')
    account_ids = fields.Many2many('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]")
    date_from = fields.Date(string='From',
        default=datetime.today().replace(day=1))
    date_to = fields.Date(string='To',
        default=datetime.today().replace(day=1) + \
            relativedelta(months=1) - relativedelta(days=1))
    type = fields.Selection(
        [
            ('income', 'Income'),
            ('expense', 'Expense')
        ], string='Type'
    )

    def show_income_graph_view(self):
        domain = [
            ('partner_id', '=', self.partner_id.id),
            ('account_id', 'in', self.account_ids.ids),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
            ]
        return {
            'name': 'Income Report',
            'view_mode': 'graph',
            'view_id': self.env.ref(
                'money_manager.money_income_graph_view').id,
            'res_model': 'money.income',
            'type': 'ir.actions.act_window',
            'domain': domain,
        }

    def show_expense_graph_view(self):
        domain = [
            ('partner_id', '=', self.partner_id.id),
            ('account_id', 'in', self.account_ids.ids),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to)
            ]
        return {
            'name': 'Expense Report',
            'view_mode': 'graph',
            'view_id': self.env.ref(
                'money_manager.money_expense_graph_view').id,
            'res_model': 'money.expense',
            'type': 'ir.actions.act_window',
            'domain': domain,
        }

    @api.onchange('partner_id')
    def onchange_accounts(self):
        self.account_ids = self.env['money.account'].search(
            [('partner_id', '=', self.partner_id.id)]).ids

    def button_print_money_report(self):
        return self.env.ref(
            'money_manager.action_print_money_report').report_action(self)

    def get_money_data(self):
        if self.type == 'income':
            data = self.env['money.income'].search([
                ('partner_id', '=', self.partner_id.id),
                ('account_id', 'in', self.account_ids.ids),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to)
                ])
        else:
            data = self.env['money.expense'].search([
                ('partner_id', '=', self.partner_id.id),
                ('account_id', 'in', self.account_ids.ids),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to)
                ])
        return data
