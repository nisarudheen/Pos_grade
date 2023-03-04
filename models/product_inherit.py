from odoo import models, fields


class ProductGrade(models.Model):
    _inherit = 'product.template'

    grade = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')], default='A')
