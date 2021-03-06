# -*- encoding: utf-8 -*-
##############################################################################
#
#    LaMaisonDub - Custom module for Odoo
#    Copyright (C) 2015-Today SCI LaMaisonDub (http://lamaisondub.potager.org/)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'La Maison Dub - Custom Module',
    'summary': 'Custom Settings for La Maison Dub',
    'version': '0.1',
    'category': 'Custom',
    'license': 'AGPL-3',
    'author': 'La Maison Dub',
    'website': 'http://lamaisondub.potager.org',
    'depends': [
        'base',
        'account',
        'web_tree_image',
        'hr_expense',
        'base_vat',
        'document',
        'knowledge',
    ],
    'data': [
        'security/ir_model_access.yml',
        'views/qweb.xml',
        'views/views.xml',
    ],
}
