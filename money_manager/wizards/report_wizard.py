from odoo import api, fields, models, _
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ReportWizard(models.TransientModel):
    _name = "report.wizard"

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    account_ids = fields.Many2many('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]", required=True)
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

    def get_records(self):
        domain = [
            ('partner_id', '=', self.partner_id.id),
            ('account_id', 'in', self.account_ids.ids)
            ]
        if self.date_from:
            domain.append(('date', '>=', self.date_from))
        if self.date_to:
            domain.append(('date', '<=', self.date_to))
        return domain

    def show_income_graph_view(self):
        return {
            'name': 'Income Report',
            'view_mode': 'graph',
            'view_id': self.env.ref(
                'money_manager.money_income_graph_view').id,
            'res_model': 'money.income',
            'type': 'ir.actions.act_window',
            'domain': self.get_records()
        }

    def show_expense_graph_view(self):
        return {
            'name': 'Expense Report',
            'view_mode': 'graph',
            'view_id': self.env.ref(
                'money_manager.money_expense_graph_view').id,
            'res_model': 'money.expense',
            'type': 'ir.actions.act_window',
            'domain': self.get_records()
        }

    @api.onchange('partner_id')
    def onchange_accounts(self):
        self.account_ids = self.env['money.account'].search(
            [('partner_id', '=', self.partner_id.id)]).ids

    def button_print_money_report(self):
        return self.env.ref(
            'money_manager.action_print_money_report').report_action(self)

    def get_money_data(self):
        data = {}
        if self.type == 'income':
            res = self.env['money.income'].search(self.get_records())
        else:
            res = self.env['money.expense'].search(self.get_records())
        for rec in res:
            if rec.account_id not in data.keys():
                data[rec.account_id] = [rec]
            else:
                data[rec.account_id].append(rec)
        return data
