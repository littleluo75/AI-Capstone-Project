# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    gender = fields.Selection([('male', 'Male'),
                              ('female', 'Female')], string='Giới tính')

    detailed_type = fields.Selection(selection_add=[
        ('model', 'Models'),
        ('cloth', 'Clothes')],
        ondelete={
            'model': 'set service',
            'cloth': 'set service',
        }
    )

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['model'] = 'service'
        type_mapping['cloth'] = 'service'
        return type_mapping
