# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import PoolMeta


class MoveLine(metaclass=PoolMeta):
    __name__ = 'account.move.line'

    @fields.depends('analytic_lines', 'debit')
    def on_change_debit(self):
        if len(self.analytic_lines) == 1:
            for line in self.analytic_lines:
                line.debit = self.debit

    @fields.depends('analytic_lines', 'credit')
    def on_change_credit(self):
        if len(self.analytic_lines) == 1:
            for line in self.analytic_lines:
                line.credit = self.credit


class Line(metaclass=PoolMeta):
    __name__ = 'analytic_account.line'

    party = fields.Function(fields.Many2One('party.party', 'Party'),
        'get_party', searcher='search_party')
    invoice = fields.Function(fields.Many2One('account.invoice', 'Invoice'),
        'get_invoice', searcher='search_invoice')

    @classmethod
    def get_party(self, lines, name=None):
        parties = {}
        for line in lines:
            party = None
            if (line.move_line and line.move_line.origin
                    and line.move_line.origin.__name__ == 'account.invoice'):
                party = line.move_line.origin.party.id
            parties[line.id] = party
        return parties

    @classmethod
    def search_party(cls, name, clause):
        return [('move_line.origin.party', clause[1], clause[2],
            'account.invoice')]

    @classmethod
    def get_invoice(self, lines, name=None):
        invoices = {}
        for line in lines:
            invoice = None
            if (line.move_line and line.move_line.origin
                    and line.move_line.origin.__name__ == 'account.invoice'):
                invoice = line.move_line.origin.id
            invoices[line.id] = invoice
        return invoices

    @classmethod
    def search_invoice(cls, name, clause):
        return [('move_line.origin.rec_name', clause[1], clause[2],
            'account.invoice')]
