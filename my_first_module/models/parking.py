from odoo import models, fields

class parking(models.Model):
    _name = 'parking'
    _description = 'parking'

    name = fields.Char()
    car_ids = fields.One2many('car.car')