# SPDX-License-Identifier: Apache-2.0
"""Finite exact checks of rational-base denominator clearing.

These checks support the rational-base clearing calculation in paper.tex.
They do not certify the geometric interpolation theorem or exponent two.
"""
from pathlib import Path
import json
from fractions import Fraction as F
from math import comb, lcm
from itertools import product

S = 6


def constant(x):
    return [F(x)] + [F(0)] * S


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def mul(x, y):
    return [sum(x[k] * y[n-k] for k in range(n+1)) for n in range(S+1)]


def scale(x, a):
    return [a * b for b in x]


def power(x, n):
    y = constant(1)
    for _ in range(n):
        y = mul(y, x)
    return y


G = [[F(0)] + [F((-1)**(k+1), k) if k < cutoff else F(0)
                for k in range(1, S+1)] for cutoff in [3, 5]]
qs, ps, K = (7, 11), (5, -3), 4
count = 0
for base in [F(2, 3), F(3, 2), F(1, 5), F(5), F(101, 103)]:
    u, v = base.numerator, base.denominator
    for h, j, a0, a1 in product(range(4), range(K), range(4), range(4)):
        alpha = (a0, a1)
        for b0, b1 in product(range(a0+1), range(a1+1)):
            beta = (b0, b1)
            entry = scale(power([F(1), F(1)] + [F(0)]*(S-1), h), base**(j*h))
            for i in range(2):
                entry = scale(mul(entry, power(add(constant(F(j*ps[i], qs[i])),
                                                       G[i]), alpha[i]-beta[i])),
                              comb(alpha[i], beta[i]))
            denom_clearing = (lcm(1, 2)**(alpha[0]-beta[0]) *
                              lcm(1, 2, 3, 4)**(alpha[1]-beta[1]))
            multiplier = (v**((K-1)*h) * qs[0]**(alpha[0]-beta[0]) *
                          qs[1]**(alpha[1]-beta[1]) * denom_clearing)
            assert all((coef*multiplier).denominator == 1 for coef in entry)
            count += len(entry)

print('Exact rational-base column clearing passed:', count,
      'coefficients across 5 bases, including bases below 1 and '
      'negative approximation numerators.')

result = {
    'status': 'passed',
    'arithmetic': 'exact rational coefficients',
    'coefficients_checked': count,
    'bases': ['2/3', '3/2', '1/5', '5', '101/103'],
    'K': K,
    'h_range': [0, 3],
    'alpha_ranges': [[0, 3], [0, 3]],
    'Taylor_coefficient_range': [0, S],
    'approximation_denominators': list(qs),
    'approximation_numerators': list(ps),
    'truncation_cutoffs': [3, 5],
    'scope': 'Finite denominator-clearing test only; does not certify interpolation or exponent two.'
}
certificate = Path(__file__).resolve().parents[1] / 'certificates' / 'rational_base_denominators.json'
certificate.parent.mkdir(parents=True, exist_ok=True)
certificate.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
