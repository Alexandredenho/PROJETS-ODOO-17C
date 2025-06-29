# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Loan'

    book_id = fields.Many2one('library.book', string="Livre", required=True)
    borrower_id = fields.Many2one("library.reader", string="Emprunteur", required=True)
    loan_date = fields.Datetime(string="Date d'emprunt", default=fields.Datetime.now, required=True)
    return_due_date = fields.Datetime(string="Date de retour prévue")
    return_date = fields.Datetime(string="Date de retour effective")
    loan_duration = fields.Integer(string="Durée de l'emprunt", compute="compute_loan_duration", store=True)

    @api.depends('loan_date', 'return_date')
    def compute_loan_duration(self):
        for rec in self:
            if rec.loan_date and rec.return_date:
                rec.loan_duration = (rec.return_date - rec.loan_date).days
            else:
                rec.loan_duration = 0
