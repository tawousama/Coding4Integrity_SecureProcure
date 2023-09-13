from odoo import http
from odoo.http import request


class Eproc(http.Controller):

    @http.route('/offer-request', type='http', auth="public", website=True, csrf=True)
    def offer_form(self, **kwargs):
        print('*******************heeeereeee******************')
        offers = request.env['eprocurement.offer'].search([])
        values = {
            'offers': offers
        }
        print(offers)
        return request.render("eprocurment.offer_list", values)

    @http.route('/signup-customer-request', type='http', auth="public", website=True, csrf=True)
    def signup_customer(self, **kwargs):

        return request.render("eprocurment.register_customer", {})

    @http.route('/signup-supplier-request', type='http', auth="public", website=True, csrf=True)
    def signup_customer(self, **kwargs):

        return request.render("eprocurment.register_supplier", {})
