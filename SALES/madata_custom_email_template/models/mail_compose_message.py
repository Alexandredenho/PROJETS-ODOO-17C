from odoo import models, fields, api


class CustomMailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.model
    def default_get(self, fields):
        print("jesuis passé par là")
        # Inherit default_get to modify the default values
        res = super(CustomMailComposeMessage, self).default_get(fields)
        return res
