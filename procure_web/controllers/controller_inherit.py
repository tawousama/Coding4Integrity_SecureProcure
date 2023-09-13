from odoo import api, fields, models, _
from odoo import http
from odoo.addons.website.controllers.main import Website


class CustomWebsite(Website):
    @http.route('/web/login', type='http', auth="public", website=True)
    def web_login(self, *args, **kw):
        # Fetch the list of user types
        response = super(CustomWebsite, self).web_login(*args, **kw)

        # Fetch the list of user types
        user_types = [('customer', 'Customer'),
                      ('supplier', 'Supplier')]

        # Add your custom data to the response
        response.qcontext['user_types'] = user_types

        return response
