from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    record_transaction_reminder = fields.Boolean(
        string='Record Transaction Reminder')
    report_notification = fields.Boolean(string='Report Notification')
