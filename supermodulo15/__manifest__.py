# -*- coding: utf-8 -*-
{
    'name': "supermodulo15",

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
'account_asset_management',
'account_balance_line',
'account_banking_mandate',
'account_banking_pain_base',
'account_banking_sepa_credit_transfer',
'account_banking_sepa_direct_debit',
'account_due_list',
'account_edi_facturx',
'account_edi',
'account_financial_report',
'account_invoice_refund_link',
'account_invoice_search_by_reference',
'account_lock_date_update',
'account_move_force_removal',
'account_move_line_menu',
'account_payment_mode',
'account_payment_order',
'account_payment_partner',
'account_payment_sale',
'account_payment_term_extension',
'account_qr_code_sepa',
'account_reconciliation_widget',
'account_statement_import',
'account_tax_balance',
'account_usability',
'account',
'analytic',
'attachment_indexation',
'auth_password_policy_portal',
'auth_password_policy_signup',
'auth_password_policy',
'auth_signup',
'auth_totp_mail',
'auth_totp_portal',
'auth_totp',
'barcodes',
'base_address_city',
'base_bank_from_iban',
'base_iban',
'base_import_module',
'base_import',
'base_location_geonames_import',
'base_location',
'base_partner_sequence',
'base_setup',
'base_technical_features',
'base_user_role',
'base_vat',
'base',
'board',
'bus',
'calendar_sms',
'calendar',
'contacts',
'contract_sale',
'contract',
'crm_iap_enrich',
'crm_iap_mine',
'crm_sms',
'crm',
'date_range',
'digest',
'disable_odoo_online',
'document_page_tag',
'document_page',
'fetchmail_gmail',
'fetchmail',
'gamification_sale_crm',
'gamification',
'google_account',
'google_drive',
'google_gmail',
'google_spreadsheet',
'hr_attendance',
'hr_contract',
'hr_expense',
'hr_gamification',
'hr_holidays_attendance',
'hr_holidays',
'hr_org_chart',
'hr',
'http_routing',
'iap_crm',
'iap_mail',
'iap',
'knowledge',
'l10n_es_account_asset',
'l10n_es_account_banking_sepa_fsdd',
'l10n_es_account_statement_import_n43',
'l10n_es_aeat_mod111',
'l10n_es_aeat_mod115',
'l10n_es_aeat_mod123',
'l10n_es_aeat_mod303',
'l10n_es_aeat_mod347',
'l10n_es_aeat_mod349',
'l10n_es_aeat_mod390',
'l10n_es_aeat',
'l10n_es_dua',
'l10n_es_mis_report',
'l10n_es_partner',
'l10n_es_toponyms',
'l10n_es_vat_book',
'l10n_es',
'link_tracker',
'mail_bot_hr',
'mail_bot',
 #'mail_debrand',
'mail',
'mass_editing',
'mass_mailing_crm',
'mass_mailing_sale',
'mass_mailing',
'mis_builder_budget',
'mis_builder_cash_flow',
'mis_builder',
'note',
'partner_autocomplete',
'payment_transfer',
'payment',
'phone_validation',
'portal_odoo_debranding',
'portal_rating',
'portal',
'product',
'project_account',
'project_hr_expense',
'project_purchase',
'project_task_default_stage',
'project',
'purchase_stock',
'purchase',
'rating',
'remove_odoo_enterprise',
'report_xlsx_helper',
'report_xlsx',
'resource',
'sale_crm',
'sale_expense',
'sale_force_invoiced',
'sale_management',
'sale_project',
'sale_purchase_stock',
'sale_purchase',
'sale_sms',
'sale_stock',
'sale',
'sales_team',
'sms',
'snailmail_account',
'snailmail',
'social_media',
'stock_account',
'stock_sms',
'stock',
'survey',
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
