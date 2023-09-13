from odoo import api, fields, models, _
from random import randint
import datetime

class Offer(models.Model):
    _name = 'eprocurement.offer'
    _description = 'Details of offers'

    def _get_default_color(self):
        return randint(1, 11)
    name = fields.Char(string='Name')
    title = fields.Char(string='Title')
    date_creation = fields.Date(string='Creation Date')
    date_publish = fields.Date(string='Publication Date')
    conditions = fields.One2many('eprocurement.condition', 'proposal_id', string='Conditions')
    customer = fields.Many2one('res.users', string='Customer', readOnly=True, default=lambda self: self.env.uid)
    stage_id = fields.Selection([('draft', 'Draft'), ('shared', 'Shared'),
                                 ('ongoing', 'Ongoing'), ('completed', 'Completed')],
                                 string='Status', default='draft', track_visibility='always')

    color = fields.Integer(string='Color', default=_get_default_color)

    activity = fields.Many2one('eprocurement.activity', string='Category')
    subcategory = fields.Many2one('eprocurement.activity.sub', string='Sub Category',  domain="[('cat_id.id', '=', activity)]")
    detail_ids = fields.One2many('eprocurement.detail', 'offer_id', string='Details')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('eprocurement.offer') or _('New')
        res = super(Offer, self).create(vals)
        return res

    def confirm_rfp(self):
        for rec in self:
            if rec.stage_id == 'draft':
                rec.stage_id = 'shared'
                rec.date_publish = datetime.date.today()

    def open_proposals(self):
        for rec in self:
            view_id = self.env.ref('eprocurment.proposal_tree_view').id
            domain = [('offer_id', '=', rec.id)]
            return {
                'type': 'ir.actions.act_window',
                'name': _('Proposals for this RFP'),
                'res_model': 'eprocurement.proposal',
                'view_mode': 'tree',
                'view_id': view_id,
                'domain': domain
            }
