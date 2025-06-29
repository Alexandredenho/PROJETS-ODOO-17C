from odoo import api, fields, models, _

class PortalWizardUser(models.TransientModel):
    """
        A model to configure users in the portal wizard.
    """

    _inherit = 'portal.wizard.user'
    _description = 'Portal User Config'

    def _send_email(self):
        """ send notification email to a new portal user """
        self.ensure_one()

        # determine subject and body in the portal user's language
        template = self.env.ref('madata_custom_email_template.mail_template_data_portal_welcome')
        if not template:
            raise UserError(_('The template "Portal: new user" not found for sending email to the portal user.'))

        lang = self.user_id.sudo().lang
        partner = self.user_id.sudo().partner_id

        portal_url = partner.with_context(signup_force_type_in_url='', lang=lang)._get_signup_url_for_action()[partner.id]
        partner.signup_prepare()

        template.with_context(dbname=self._cr.dbname, portal_url=portal_url, lang=lang).send_mail(self.id, force_send=True)

        return True
