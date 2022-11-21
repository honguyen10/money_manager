from odoo import models, fields, api

class MoneyCategory(models.Model):
    _name = 'money.category'
    _description = 'Categories'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    type = fields.Selection(
        [
            ('income', 'Income'),
            ('expense', 'Expense')
        ], string='Type', required=True
    )
