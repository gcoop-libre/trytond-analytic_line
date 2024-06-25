# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import line


def register():
    Pool.register(
        line.MoveLine,
        line.Line,
        module='analytic_line', type_='model')
