from odoo import models, fields, api
from datetime import datetime


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
            ('once_a_month', 'Once a month')
        ], string='Reminder Frequency', required=True
    )
    date = fields.Date(default=datetime.today(), required=True)
    time = fields.Float(required=True)

    @api.model
    def _cron_send_reminder_email(self):
        template = self.env.ref(
                'money_manager.reminder_template_data')
        template.send_mail(
                self.partner_id.id,
                notif_layout='mail.mail_notification_light',
                force_send=True)

    def set_reminder_interval(self, cr, uid, context=None):
        try:
            cron = self.sudo().env.ref('my_module.my_cron_external_id')
            cron.sudo().write({'nextcall': datetime.now()})
        except Exception as e:
            pass