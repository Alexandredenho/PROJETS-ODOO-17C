from odoo import fields, models, api

class ReaderReader(models.Model):
    _name = 'library.reader'
    _description = 'Reader'

    name = fields.Char(string="Nom du lecteur", required=True)
    surname = fields.Char(string="Prénom du lecteur", required=True)
    email = fields.Char(string="Email du lecteur", required=True)
    phone = fields.Char(string="Téléphone du lecteur", required=True)
    register_date = fields.Date(string="Date d'inscription", default=fields.Date.today)
    books_borrowed = fields.One2many('library.loan', 'borrower_id', string="Livres empruntés")