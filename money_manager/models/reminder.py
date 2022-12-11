from odoo import models, fields, api


class Reminder(models.Model):
    _name = 'reminder'
    _description = 'Reminder'
    _rec_name = 'name'

    partner_id = fields.Many2one('res.partner', string='User Name',
        required=True)
    name = fields.Char(string='Reminder Name', required=True)
    description = fields.Char(string='Description')
    frequency = fields.Selection(
        [
            ('once', 'Once'),
            ('daily', 'Daily'),
            ('once_a_week', 'Once a week'),
            ('once_a_month', 'Once a month'),
            ('once_a_year', 'Once a year')
        ], string='Reminder Frequency', required=True
    )
    date = fields.Date()
    time = fields.Float()