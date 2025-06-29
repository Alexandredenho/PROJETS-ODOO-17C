from odoo import fields, models, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    GENDER = [
        ('M', 'Homme'),
        ('F', 'Femme'),
    ]

    title = fields.Char(string="Titre du livre", required=True)
    author = fields.Char(string="Auteur", required=True)
    genre = fields.Selection(selection=GENDER, string="Genre", required=True)
    editor = fields.Char(string="Éditeur", required=True)
    page_nbr = fields.Integer(string="Nombre de pages", required=True)
    publication_date = fields.Date(string="Date de publication", required=True)
    responsible_id = fields.Many2one("hr.employee", string="Responsable du livre")