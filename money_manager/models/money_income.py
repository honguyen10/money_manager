from odoo import models, fields, api
from datetime import datetime

class MoneyIncome(models.Model):
    _name = 'money.income'
    _description = 'Income'
    _rec_name = 'category'

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    amount = fields.Float(string='Amount', required=True)
    category = fields.Char(string='Category', required=True)
    date = fields.Date(string='Date', default=datetime.today(), required=True)
    comment = fields.Char(string='Comment')
