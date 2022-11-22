from odoo import models, fields, api
from datetime import datetime

class MoneyIncome(models.Model):
    _name = 'money.income'
    _description = 'Income'
    _rec_name = 'category'

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    account_id = fields.Many2one('money.account', string='Account',
        domain="[('partner_id', '=', partner_id)]")
    amount = fields.Float(string='Amount', required=True)
    category = fields.Many2one('money.category', string='Category',
        domain="[('type', '=', 'income')]", required=True)
    date = fields.Date(string='Date', default=datetime.today(), required=True)
    comment = fields.Char(string='Comment')
