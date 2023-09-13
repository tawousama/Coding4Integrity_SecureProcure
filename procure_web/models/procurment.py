import datetime
from odoo import api, fields, models, _
from random import randint


class Proposal(models.Model):
    _name = 'eprocurement.proposal'
    _description = 'Details of proposals'

    def _get_default_color(self):
        return randint(1, 11)
    name = fields.Char(string='Name')
    date_creation = fields.Date(string='Creation Date')
    date_submission = fields.Date(string='Submission Date')
    title = fields.Char(string='Title', related='offer_id.title')
    detail = fields.Text(string='Details')
    offer_id = fields.Many2one('eprocurement.offer', string='Offer')
    customer = fields.Many2one('res.users', 'Customer', readonly=True, related='offer_id.customer')
    supplier = fields.Many2one('res.users', string='Supplier', default=lambda self: self.env.uid)

    stage_id = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'),
                                ('rejected', 'Rejected'), ('accepted', 'Accepted')],
                                string='Status', default='draft', track_visibility='always')

    color = fields.Integer(string='Color', default=_get_default_color)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('eprocurement.proposal') or _('New')
        res = super(Proposal, self).create(vals)
        return res

    def confirm_proposal(self):
        for rec in self:
            if rec.stage_id == 'draft':
                rec.stage_id = 'submitted'
                rec.date_submission = datetime.date.today()

