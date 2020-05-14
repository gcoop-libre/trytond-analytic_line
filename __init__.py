# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import line

__all__ = ['register']


def register():
    Pool.register(
        line.Line,
        module='analytic_line', type_='model')
