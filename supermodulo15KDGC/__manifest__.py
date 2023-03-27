# -*- coding: utf-8 -*-
{
    'name': "supermodulo15KDGC",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends':[
'account_edi_facturx',
'account_edi_ubl_cii',
'account_edi',
'account_qr_code_sepa',
'account',
'analytic',
'auth_signup',
'auth_totp_mail',
'auth_totp_portal',
'auth_totp',
'auto_backup',
'base_address_city',
'base_iban',
'base_import',
'base_location_geonames_import',
'base_location',
'base_setup',
'base_technical_features',
'base_vat',
'base',
'bus',
'calendar_sms',
'calendar',
'contacts',
'crm_iap_enrich',
'crm_iap_mine',
'crm_sms',
'crm',
'digest',
'fetchmail',
'http_routing',
'iap_crm',
'iap_mail',
'iap',
'knowledge',
'l10n_es_toponyms',
'l10n_es',
'link_tracker',
'login_user_detail',
'mail_bot',
'mail',
'mass_mailing_crm',
'mass_mailing_sale',
'mass_mailing',
'partner_autocomplete',
'payment_transfer',
'payment',
'phone_validation',
'portal',
'product',
'resource',
'sale_crm',
'sale_management',
'sale_sms',
'sale',
'sales_team',
'show_db_name',
'sms',
'snailmail_account',
'snailmail',
'social_media',
'uom',
'utm',
'web_editor',
'web_kanban_gauge',
'web_no_bubble',
'web_responsive',
'web_tour',
'web_unsplash',
'web',


    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
