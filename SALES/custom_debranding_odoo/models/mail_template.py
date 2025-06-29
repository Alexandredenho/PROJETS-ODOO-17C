# -*- coding: utf-8 -*-
from odoo import fields, models,api, _
from bs4 import BeautifulSoup


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    def ag_remove_powered_by_odoo(self):
        powered_by = "<!-- POWERED BY -->"
        count_template = 0
        for record in self:
            if powered_by in str(record.body_html):
                body_html = record.body_html
                soup = BeautifulSoup(body_html, 'html.parser')
                powered_element = soup.select_one(
                    "tr td table[style='min-width: 590px; background-color: #F1F1F1; color: #454748; padding: 8px; border-collapse:separate;']")
                powered_element.string = ''
                record.write({'body_html': str(soup)})
                count_template += 1

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'message': _(f'{count_template} Templates have been updated successfully'),
                'next': {
                    'type': 'ir.actions.client',
                    'tag': 'reload'
                }
            }
        }
