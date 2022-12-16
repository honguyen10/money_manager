from odoo import models, fields, api
from datetime import datetime


class MoneyIncome(models.Model):
    _name = 'money.income'
    _description = 'Income'
    _rec_name = 'category_id'
    _order = 'date DESC'

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    account_id = fields.Many2one('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]")
    amount = fields.Float(string='Amount', required=True)
    category_id = fields.Many2one('money.category', string='Category',
        domain="[\
            ('type', '=', 'income'),\
            ('partner_id', '=', partner_id),\
            ]",
        required=True)
    date = fields.Date(string='Date', default=datetime.today(), required=True)
    description = fields.Char(string='Description')
    currency_id = fields.Many2one('res.currency', compute='_get_company_currency', readonly=True,
        string="Currency")

    def _get_company_currency(self):
        for income in self:
            if income.partner_id.company_id:
                income.currency_id = income.sudo().partner_id.company_id.currency_id
            else:
                income.currency_id = self.env.company.currency_id
