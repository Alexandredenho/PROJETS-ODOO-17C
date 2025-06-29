from odoo import fields, models, api, _
import contextlib
import logging
import re

from ast import literal_eval
from collections import defaultdict
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools.misc import ustr
from odoo.http import request

from odoo.addons.base.models.ir_mail_server import MailDeliveryException
from odoo.addons.auth_signup.models.res_partner import SignupError, now

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _action_reset_password(self):
        print("je vais acheter mar")
        """ create signup token for each user, and send their signup url by email """
        if self.env.context.get('install_mode') or self.env.context.get('import_file'):
            return
        if self.filtered(lambda user: not user.active):
            raise UserError(_("You cannot perform this action on an archived user."))
        # prepare reset password signup
        create_mode = bool(self.env.context.get('create_user'))

        # no time limit for initial invitation, only for reset password
        expiration = False if create_mode else now(days=+1)

        self.mapped('partner_id').signup_prepare(signup_type="reset", expiration=expiration)

        # send email to users with their signup url
        account_created_template = None
        if create_mode:
            print("je suis passé parlà")
            account_created_template = self.env.ref('madata_custom_email_template.set_password_email',
                                                    raise_if_not_found=False)
            print(f'faccount_created_template {account_created_template}')
            if account_created_template and account_created_template._name != 'mail.template':
                _logger.error("Wrong set password template %r", account_created_template)
                return

        email_values = {
            'email_cc': False,
            'auto_delete': True,
            'message_type': 'user_notification',
            'recipient_ids': [],
            'partner_ids': [],
            'scheduled_date': False,
        }

        for user in self:
            if not user.email:
                raise UserError(_("Cannot send email: user %s has no email address.", user.name))
            email_values['email_to'] = user.email.strip()  # Strip to remove any potential whitespace
            with contextlib.closing(self.env.cr.savepoint()):
                try:
                    if account_created_template:
                        account_created_template.send_mail(
                            user.id, force_send=True,
                            raise_exception=True, email_values=email_values)
                    else:
                        body = self.env['mail.render.mixin']._render_template(
                            self.env.ref('madata_custom_email_template.reset_password_email'),
                            model='res.users', res_ids=user.ids,
                            engine='qweb_view', options={'post_process': True})[user.id]

                        # Ensure subject doesn't contain newlines
                        subject = _('Password reset').replace('\n', ' ').replace('\r', '')

                        # Ensure email_from doesn't contain newlines
                        email_from = (user.company_id.email_formatted or user.email_formatted or '').replace('\n',
                                                                                                             ' ').replace(
                            '\r', '')

                        mail = self.env['mail.mail'].sudo().create({
                            'subject': subject,
                            'email_from': email_from,
                            'body_html': body,
                            **email_values,
                        })
                        mail.send()
                    _logger.info("Password reset email sent for user <%s> to <%s>", user.login, user.email)
                except ValueError as e:
                    _logger.error("Failed to send password reset email for user <%s>: %s", user.login, str(e))
                    # You might want to raise an exception here or handle it in some way
