# -*- coding: utf-8 -*-

##############################################################################
#
#    OdooERP
#    Copyright (C) 2022-2023 
#    Ingeniero de Sistemas. Henderson Zambrano Aguilera
#    
#
##############################################################################

{
    'name': 'División Político-Administrativa de Colombia: Departamentos y Municipios',
    'version': '15.0',
    'author': 'Ing. Henderson Zambrano',
    'license': 'AGPL-3',
    'category': 'Localization',
    "description":
        """
División Político-Administrativa de Colombia
================================================

Informacion obtenida del Ministerio de Tecnologías de La Información y Las Comunicaciones. Con Fecha del 15 de julio de 2022
     """,
    "maintainer": "Ing. Henderson Zambrano",
    "website": "https://github.com/hender88/",
	'images': ['static/description/icon.png'],
    "depends": ['base' ],

    'data': [
        'data/res.country.state.municipality.xml',
        'views/l10n_co_dpt_view.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv'
    ],
    'update_xml': ['views/l10n_co_dpt_view.xml'],
    'installable': True,

}
