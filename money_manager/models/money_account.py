from odoo import models, fields, api

class MoneyAccount(models.Model):
    _name = 'money.account'
    _description = 'Accounts'
    _rec_name = 'name'

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    name = fields.Char(string='Name', required=True)
