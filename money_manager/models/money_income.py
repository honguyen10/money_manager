from odoo import models, fields, api

class MoneyIncome(models.Model):
    _name = 'money.income'
    _description = 'Income'
    _rec_name = 'category'

    partner_id = fields.Many2one('res.partner', string='User Name')
    amount = fields.Float(string='Amount')
    category = fields.Char(string='Category')
    date = fields.Date(string='Date')
    comment = fields.Char(string='Comment')
