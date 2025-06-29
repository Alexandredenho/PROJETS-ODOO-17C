{
    'name': 'Madata Custom Email Template',
    'version': '0.1',
    'summary': '',
    'description': 'Description',
    'category': 'Notification',
    'author': 'MADATA',
    'website': '',
    'depends': ['base', 'mail', 'auth_signup','sale','lunch','gamification','im_livechat','portal','web'],
    'data': [
        'views/mail_template_inherit_views.xml',
        'views/custom_mail_template_views.xml',
    ],
    'post_init_hook': 'update_mail_compose_actions',

    # 'assets': {
    #     'web.assets_backend': [
    #         '/madata_custom_email_template/static/src/js/mail_compose_message.js',
    #     ],
    # },
    'demo': [''],
    'installable': True,
    'auto_install': False
}
