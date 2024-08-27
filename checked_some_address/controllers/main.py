from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request

class WebsiteSaleAddressInherit(WebsiteSale):
    
    @http.route()
    def address(self, **post):
        response = super(WebsiteSaleAddressInherit, self).address(**post)
        checked_some_address = request.env['ir.config_parameter'].sudo().get_param('checked_some_address.checked_some_address')
        
        response.qcontext['checked_some_address'] = checked_some_address
        
        return response