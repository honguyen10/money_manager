# -*- coding: utf-8 -*-
{
    'name': "money_manager",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/money_manager_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',

        'views/money_income_views.xml',
        'views/money_expense_views.xml',
        'views/money_category_views.xml',
        'views/money_account_views.xml',
        'views/money_income_graph_views.xml',
        'views/money_expense_graph_views.xml',
        'views/reminder_views.xml',

        'wizards/report_wizard_views.xml',

        'reports/report_template.xml',

        'menu/menu_money_manager.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
