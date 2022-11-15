from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'
	
    municipality_id = fields.Many2one('res.country.state.municipality', 'Municipio')



