from . import models
from . import controllers
from . import wizards

from odoo.tools import config
from odoo import api, fields, models, SUPERUSER_ID


def update_mail_compose_actions(env):
    # Recherche toutes les actions de type ir.actions.act_window qui ont pour modèle mail.compose.message
    actions = env['ir.actions.act_window'].search([('type', '=', 'ir.actions.act_window'), ('res_model', '=', 'mail.compose.message'), ('view_mode', '=', 'form')])
    print(f"je suis passer par la {len(actions)}")

    # Boucle sur les actions trouvées et ajoute un nom dans le contexte
    for action in actions:
        ctx = action.context or {}
        ctx['name'] = 'Madata'
        action.context = ctx
        print("je suis passé par la")

    # Enregistre les modifications
    actions.flush()