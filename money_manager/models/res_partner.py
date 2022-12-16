from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    record_transaction_remind = fields.Boolean(
        string='Record Transaction Remind')
    report_notification = fields.Boolean(string='Report Notification')
