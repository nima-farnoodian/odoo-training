from dataclasses import field

from pkg_resources import require
from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property "
    name=fields.Char(required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date()
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
        string="Orientation",
        selection=[("north","North"),("south","South"),("east","East"),("west","West")],
        help="The orientation of the place."
    )
