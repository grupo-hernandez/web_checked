from odoo import fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    
    checked_terms = fields.Boolean(
        string=_('Check terms and conditions in checkout form'), 
        config_parameter='checked_terms.checked_terms',
        )
    