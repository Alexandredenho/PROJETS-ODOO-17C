{
    'name': 'Remove all powered by Odoo',
    'summary': 'Summery',
    'sequence': -100,
    'version': '1.0.0',
    'description': """Suppression automatique du texte Généré par Odoo dans tous les modèles d'e-mails "
                    Modification du portail pour retirer la mention dans le pied de page 
                    Personnalisation facile pour adapter à ton branding""",
    'category': 'service',
    'author': 'ALEXANDRE LE GRAND',
    'maintainer': 'ALEXANDRE LE GRAND , support: saintkoffakk@gmail.com',
    'depends': [
        'base',
        'web',
        'mail'
    ],

    'data': [
        'data/remove_mail_template_data.xml',
        'views/mail_template_remove_odoo_views.xml',
        'views/website_footer_brand_promotion.xml',
    ],
    'icon': '/custom_debranding_odoo/static/description/icon.png',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
