# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class BadgeUser(models.Model):
    """User having received a badge"""

    _inherit = 'gamification.badge.user'


    def _send_badge(self):
        """Send a notification to a user for receiving a badge

        Does not verify constrains on badge granting.
        The users are added to the owner_ids (create badge_user if needed)
        The stats counters are incremented
        :param ids: list(int) of badge users that will receive the badge
        """
        template = self.env.ref(
            'madata_custom_email_template.email_template_badge_received',
            raise_if_not_found=False
        )
        if not template:
            return

        for badge_user in self:
            template.send_mail(
                badge_user.id,
            )

        return True
