{
    'name': "Eprocurment",
    'version': '13.0.1.0.0',
    'depends': ['base', 'mail', 'website'],
    'sequence': '30',
    'author': "rhamoud",
    'category': 'Extra Tools',
    'summary': "Module for calculating the financial score of a company",
    # data files always loaded at installation
    'data': [
            'security/security.xml',
            'security/ir.model.access.csv',
            'views/configuration.xml',
            'views/users_inherit.xml',
            'views/register_inherit.xml',
            'views/proposal.xml',
            'views/offer.xml',
            'views/rfp_page.xml',
            'views/login_inherit.xml',
            'views/sequence.xml',
            'views/menu_items.xml',
            'data/category.xml'],

    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
