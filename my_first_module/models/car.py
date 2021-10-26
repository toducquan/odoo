from odoo import models, fields, api


class Feature(models.Model):
    name = fields.Char()

class car(models.Model):
    _name = 'car'
    _description = 'car'

    name = fields.Char()
    horse_power = fields.Integer()
    door_number = fields.Integer()
    driver_id = fields.Many2one('res.partner')
    feature_ids = fields.Many2one('car.feature')
    total_speed = fields.Float(compute="_val", store=True)
    status = fields.Selection(selection=[('type1', 'new'),('type2', 'used'),('type3', 'sold')], string='Type', default='type1')
    car_sequence = fields.Char(string='Sequence')

    @api.depends('horse_power')
    def _val(self):
        for record in self:
            record.total_speed = record.horse_power * 5

