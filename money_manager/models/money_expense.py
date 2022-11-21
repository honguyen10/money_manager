from odoo import models, fields, api
from datetime import datetime

class MoneyExpense(models.Model):
    _name = 'money.expense'
    _description = 'Expense'
    _rec_name = 'category'

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    amount = fields.Float(string='Amount', required=True)
    category = fields.Char(string='Category', required=True)
    date = fields.Date(string='Date', default=datetime.today(), required=True)
    comment = fields.Char(string='Comment')
