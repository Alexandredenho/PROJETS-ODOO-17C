import math
import pytz

from collections import defaultdict
from datetime import datetime, time, timedelta
from textwrap import dedent

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import float_round

from odoo.addons.base.models.res_partner import _tz_get


class LunchSupplier(models.Model):
    _inherit = 'lunch.supplier'

    def _send_auto_email(self):
        """ Send an email to the supplier with the order of the day """
        # Called daily by cron
        self.ensure_one()

        if not self.available_today:
            return

        if self.send_by != 'mail':
            raise UserError(_("Cannot send an email to this supplier!"))

        orders = self._get_current_orders()
        if not orders:
            return

        order = {
            'company_name': orders[0].company_id.name,
            'currency_id': orders[0].currency_id.id,
            'supplier_id': self.partner_id.id,
            'supplier_name': self.name,
            'email_from': self.responsible_id.email_formatted,
            'amount_total': sum(order.price for order in orders),
        }

        sites = orders.mapped('user_id.last_lunch_location_id').sorted(lambda x: x.name)
        orders_per_site = orders.sorted(lambda x: x.user_id.last_lunch_location_id.id)

        email_orders = [{
            'product': order.product_id.name,
            'note': order.note,
            'quantity': order.quantity,
            'price': order.price,
            'toppings': order.display_toppings,
            'username': order.user_id.name,
            'site': order.user_id.last_lunch_location_id.name,
        } for order in orders_per_site]

        email_sites = [{
            'name': site.name,
            'address': site.address,
        } for site in sites]

        self.env.ref('madata_custom_email_template.lunch_order_mail_supplier').with_context(
            order=order, lines=email_orders, sites=email_sites
        ).send_mail(self.id)

        orders.action_send()