from odoo import fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    
    checked_some_address = fields.Boolean(
        string=_('Check send to the some address in address form'), 
        config_parameter='checked_some_address.checked_some_address',
        )
    