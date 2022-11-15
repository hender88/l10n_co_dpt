# -*- coding: utf-8 -*-
#


from odoo import api, fields, models



class CountryState(models.Model):
    _name = "res.country.state"
    _inherit = "res.country.state"


    municipality_id = fields.One2many('res.country.state.municipality', 'state_id', 'Municipios de este departamento')


class StateMunicipality(models.Model):
    _name = "res.country.state.municipality"
    _description = "State municipalities"

    state_id = fields.Many2one('res.country.state', 'Departamento', placeholder="Departamento", required=True, help='Nombre del Departamento')
    name = fields.Char('Municipio', required=True, help='Nombre del Municipio')
    code = fields.Char('Codigo', size=3, required=True, help='Abreviatura de departamento')




