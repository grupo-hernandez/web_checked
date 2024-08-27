from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request

class WebsiteSaleInherit(WebsiteSale):
    
    @http.route()
    def shop_payment(self, **post):
        response = super(WebsiteSaleInherit, self).shop_payment(**post)
        checked_terms = request.env['ir.config_parameter'].sudo().get_param('checked_terms.checked_terms')
        
        response.qcontext['checked_terms'] = checked_terms
        
        return response