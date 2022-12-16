from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    record_transaction_remind = fields.Boolean(
        string='Record Transaction Remind')
    report_notification = fields.Boolean(string='Report Notification')

    @api.model
    def cron_send_record_transaction_remind(self):
        for partner in self.env['res.partner'].search(
            [('record_transaction_remind', '=', True)]):
            template = self.env.ref(
                    'money_manager.record_transaction_remind_template')
            template.send_mail(
                    partner.id,
                    email_layout_xmlid='mail.mail_notification_light',
                    force_send=True)
