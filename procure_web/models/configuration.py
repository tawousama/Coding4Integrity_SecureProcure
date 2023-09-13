from odoo import api, fields, models, _


class Condition(models.Model):
    _name = 'eprocurement.condition'
    _description = 'Condition of proposals'

    name = fields.Char(string='Condition')
    proposal_id = fields.Many2one('eprocurement.proposal', string='Proposal')


class Activity(models.Model):
    _name = 'eprocurement.activity'
    _description = 'Activity of proposals'

    name = fields.Char(string='Category')
    proposal_id = fields.Many2one('eprocurement.offer', string='Proposal')
    subcategories = fields.One2many('eprocurement.activity.sub', 'cat_id', string='Sub categories')


class SubCategory(models.Model):
    _name = 'eprocurement.activity.sub'
    _description = 'Activity of proposals'

    name = fields.Char(string='Sub Category')
    cat_id = fields.Many2one('eprocurement.activity', string='Category')
    brands = fields.One2many('eprocurement.brand', 'subcat_id', string='Brands')


class Brand(models.Model):
    _name = 'eprocurement.brand'
    _description = 'Brand'

    name = fields.Char(string='Brand')
    subcat_id = fields.Many2one('eprocurement.activity.sub', string='Sub Category')
    model = fields.One2many('eprocurement.model', 'brand_id', string='Models')


class Model(models.Model):
    _name = 'eprocurement.model'
    _description = 'Model'

    name = fields.Char(string='Model')
    brand_id = fields.Many2one('eprocurement.brand', string='Brand')


class DetailCategory(models.Model):
    _name = 'eprocurement.detail'
    _description = 'Detail of proposals'

    brand = fields.Many2one('eprocurement.brand', string='Brand')
    model = fields.Many2one('eprocurement.model', string='Model')
    offer_id = fields.Many2one('eprocurement.offer', string='Offer')


class Stage(models.Model):
    _name = 'eprocurement.offer.stage'
    _description = 'Stages of RFPs'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='La description')
    is_won = fields.Boolean('Is Won Stage?')
    sequence = fields.Integer('Séquence', default=1, help="Used to order stages. Lower is better.")
    sessions_ids = fields.One2many('eprocurement.offer', 'stage_id', string='Séances')


class User(models.Model):
    _inherit = 'res.users'

    public_user = fields.Selection([('customer', 'Customer'),
                                    ('supplier', 'Supplier')], string='Type')

