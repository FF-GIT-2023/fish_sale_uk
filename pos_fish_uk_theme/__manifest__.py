# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: ASWIN A K (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
    'name': 'POS Fish Theme',
    'version': '17.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'The POS Theme Sapphire Is A Responsive And Ultimate '
               'Theme For Your Odoo V17.This Theme Will Give You '
               'A New Experience With Odoo.',
    'description': '''Minimalist and elegant backend POS theme for Odoo 17''',
    'author': 'Forefront Technologies',
    'company': 'Forefront Technologies',
    'maintainer': 'Forefront Technologies',
    'depends': ['point_of_sale', 'pos_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_fish_uk_theme/static/src/js/ProductsWidget.js',
            'pos_fish_uk_theme/static/src/js/ProducScreen.js',
            'pos_fish_uk_theme/static/src/xml/**/*.xml',
            'pos_fish_uk_theme/static/src/css/custom.css',
        ],
    },
    'images': [
        'static/description/banner.jpg',
        'static/description/theme_screenshot.jpg',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
