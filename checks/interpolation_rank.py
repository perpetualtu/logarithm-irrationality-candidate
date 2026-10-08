# SPDX-License-Identifier: Apache-2.0
"""Independent exact-arithmetic probes of separated-weight log interpolation.

All matrices are built after the invertible filtered substitution z=log(1+t).
Rows are multiplied by s!, so integral y and c give an integral matrix.
A full row rank modulo a prime certifies full row rank over Q and C. A
deficient modular rank is inconclusive until an exact Q rank is computed.
This program is a finite probe, not a proof of any eventual-surjectivity claim.
"""
from fractions import Fraction
from math import comb, gcd, factorial, prod
from pathlib import Path
import argparse
import json
import time


def lattice(weights, bound, strict=False):
    """Integer exponent tuples in the indicated weighted simplex."""
    weights = tuple(map(Fraction, weights))
    bound = Fraction(bound)
    out = []
    def visit(i, prefix, used):
        if i == len(weights):
            if used < bound if strict else used <= bound:
                out.append(tuple(prefix))
            return
        q = (bound-used) / weights[i]
        top = q.numerator // q.denominator
        if strict and q.denominator == 1:
            top -= 1
        for n in range(top+1):
            visit(i+1, prefix+[n], used+weights[i]*n)
    visit(0, [], Fraction(0))
    return out


def poly_product(alpha, beta, center):
    """Product_i (c_i+z)^(alpha_i-beta_i), exact rational coefficients."""
    p = [Fraction(1)]
    for a, b, c in zip(alpha, beta, center):
        n = a-b
        q = [Fraction(comb(n, r))*Fraction(c)**(n-r) for r in range(n+1)]
        new = [Fraction(0)]*(len(p)+len(q)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                new[i+j] += x*y
        p = new
    return p


def coeff(h, alpha, beta, s, y, center):
    if any(b > a for a, b in zip(alpha, beta)):
        return Fraction(0)
    p = poly_product(alpha, beta, center)
    value = Fraction(0)
    for q, x in enumerate(p[:s+1]):
        value += x * (factorial(s)//factorial(s-q)) * h**(s-q)
    return Fraction(y)**h * prod(comb(a,b) for a,b in zip(alpha,beta)) * value


def q_to_mod(x, prime):
    x = Fraction(x)
    if x.denominator % prime == 0:
        raise ValueError("Prime divides an entry denominator")
    return x.numerator % prime * pow(x.denominator, -1, prime) % prime


def rows_for(V, H, centers):
    exponents = lattice(V, H, True)
    return [(j, e[1:], e[0]) for j in range(len(centers)) for e in exponents]


def column_stream(W, V, H, centers, prime=None, parity=None):
    # Enumerate cheap source degrees first to reach a spanning set sooner.
    sources = lattice(W, H)
    sources.sort(key=lambda e: (sum(e[1:]), e[1:], e[0]))
    if parity is not None:
        sources = [e for e in sources if e[0] % 2 == parity]
        rows = rows_for(V,H,[centers[0]])
        actual_centers = [centers[0]]
    else:
        rows = rows_for(V,H,centers)
        actual_centers = centers
    # Reuse powers and falling factorials in the faster integral modular path.
    if prime is not None:
        beta_groups = {}
        for index, (j,beta,s) in enumerate(rows):
            beta_groups.setdefault((j,beta), []).append((index,s))
        max_s = max((r[2] for r in rows), default=0)
        max_q = max((sum(e[1:]) for e in sources), default=0)
        falling = [[1] for _ in range(max_s+1)]
        for s in range(max_s+1):
            f=1
            for q in range(1, min(s,max_q)+1):
                f=f*(s-q+1)%prime
                falling[s].append(f)
        for e in sources:
            h,alpha = e[0],e[1:]
            power = [1]
            for s in range(max_s):
                power.append(power[-1]*h%prime)
            out = [0]*len(rows)
            for (j,beta), indices in beta_groups.items():
                if any(b>a for a,b in zip(alpha,beta)):
                    continue
                y, *c = actual_centers[j]
                multiplicity = pow(q_to_mod(y,prime),h,prime)*prod(comb(a,b) for a,b in zip(alpha,beta))%prime
                if all(x == 0 for x in c):
                    q = sum(alpha)-sum(beta)
                    for index,s in indices:
                        if q<=s:
                            out[index] = multiplicity*falling[s][q]*power[s-q]%prime
                else:
                    poly = [q_to_mod(x,prime) for x in poly_product(alpha,beta,c)]
                    for index,s in indices:
                        out[index] = multiplicity*sum(x*falling[s][q]*power[s-q] for q,x in enumerate(poly[:s+1]))%prime
            yield e,out
    else:
        for e in sources:
            h, alpha = e[0],e[1:]
            out = [coeff(h,alpha,beta,s,actual_centers[j][0],actual_centers[j][1:]) for j,beta,s in rows]
            if prime is not None:
                out = [q_to_mod(x,prime) for x in out]
            yield e,out


def column_rank(columns, row_count, prime=None):
    basis = {}
    chosen=[]
    tried=0
    for exponent, original in columns:
        tried+=1
        v=original
        for pivot, b in basis.items():
            x=v[pivot]
            if not x:
                continue
            if prime is None:
                v=[a-x*c for a,c in zip(v,b)]
            else:
                # Leading entries already equal one.
                v=[(a-x*c)%prime for a,c in zip(v,b)]
        pivot=next((i for i,x in enumerate(v) if x),None)
        if pivot is None:
            continue
        inv=1/v[pivot] if prime is None else pow(v[pivot],-1,prime)
        v=[x*inv for x in v] if prime is None else [x*inv%prime for x in v]
        basis[pivot]=v
        chosen.append(exponent)
        if len(basis)==row_count:
            break
    return len(basis),tried,chosen


def test(case, prime=1000003):
    start=time.monotonic()
    W=case['W']; V=case['V']; H=case['H']; centers=case['centers']
    rows=len(rows_for(V,H,centers)); sources=len(lattice(W,H))
    parity = (len(centers)==2 and centers[0][0]==1 and centers[1][0]==-1
              and centers[0][1:]==centers[1][1:])
    arithmetic = case.get('arithmetic','modular')
    p=None if arithmetic=='rational' else prime
    certificates=[]
    if parity:
        rank=0;tried=0
        for parity_index in (0,1):
            block_rows=rows//2
            r,n,pivots=column_rank(column_stream(W,V,H,centers,p,parity_index),block_rows,p)
            rank+=r;tried+=n
            certificates.append({'parity':parity_index,'rows':block_rows,'rank':r,'columns_examined':n,'pivot_source_exponents':pivots})
    else:
        rank,tried,pivots=column_rank(column_stream(W,V,H,centers,p),rows,p)
        certificates.append({'rows':rows,'rank':rank,'columns_examined':tried,'pivot_source_exponents':pivots})
    status = ('full_row_rank_over_Q_and_C' if rank==rows else
              'exact_rank_deficiency_over_Q_and_C' if p is None else
              'modular_deficiency_inconclusive_over_Q')
    return {**case,'rows':rows,'source_columns':sources,'rank':rank,
            'prime':p,'columns_examined':tried,'status':status,
            'elapsed_seconds':round(time.monotonic()-start,3),
            'certificates':certificates}


CASES=[
    {'name':'m1_smallH_actual_weights_boundary','W':[1,21],'V':[1,210],'H':21,
     'centers':[[1,0],[-1,0]],'arithmetic':'rational','scope':'actual separated weights; H too small and not required divisible'},
    {'name':'m1_actual_weights_divisible_H210','W':[1,21],'V':[1,210],'H':210,
     'centers':[[1,0],[-1,0]],'scope':'K=2 theta=1/10 sigma=3/10 C*=20; w1=21; H divisible R=210; beta=1 excluded at strict boundary'},
    {'name':'m1_actual_weights_divisible_H420','W':[1,21],'V':[1,210],'H':420,
     'centers':[[1,0],[-1,0]],'scope':'same fixed data and centers; beta=1 included; H divisible R=210'},
    {'name':'m1_actual_weights_two_osculating_centers_H210','W':[1,21],'V':[1,210],'H':210,
     'centers':[[1,0],[2,'11/16']],
     'scope':'actual separated weights; fixed centers on F(Y)=3Y-13Y^2/8+Y^3/2-Y^4/16-29/16 with logarithmic contact order at least 3 at both centers; H divisible R=210'},
    {'name':'m1_generic_rational_centers','W':[1,3],'V':[1,9],'H':36,
     'centers':[[1,0],[2,3]],'arithmetic':'rational','scope':'exploratory weights below separation threshold; theta=1/3; fixed centers'},
    {'name':'m1_w0_gt_v0','W':[2,5],'V':[1,25],'H':50,
     'centers':[[1,0],[-1,0]],'arithmetic':'rational','scope':'exploratory below separation threshold; theta=1/5, K*w0/v0*theta=4/5'},
    {'name':'m2_same_diagonal_offsets_H20','W':[1,2,4],'V':[1,5,10],'H':20,
     'centers':[[1,0,0],[-1,0,0]],'arithmetic':'rational','scope':'m=2 theta=2/5; exploratory nonseparated weights; invariant hyperplane X2=X1'},
    {'name':'m2_distinct_transverse_offsets_H20','W':[1,2,4],'V':[1,5,10],'H':20,
     'centers':[[1,0,0],[-1,0,1]],'arithmetic':'rational','scope':'same weak weights; two different transverse offsets'},
    {'name':'m2_unequal_weights_same_diagonal_H40','W':[1,2,8],'V':[1,5,20],'H':40,
     'centers':[[1,0,0],[-1,0,0]],'scope':'m=2 theta=2/5; fixed common invariant hyperplane; moderate hierarchy below actual threshold'},
]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--names',nargs='*')
    ap.add_argument('--prime',type=int,default=1000003)
    ap.add_argument('--output',default='certificates/interpolation_rank.json')
    args=ap.parse_args()
    if args.prime < 2 or any(args.prime % p == 0 for p in range(2,int(args.prime**0.5)+1)):
        raise ValueError('The modular modulus must be prime')
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    results=[]
    for case in CASES:
        if args.names is not None and case['name'] not in args.names:
            continue
        result=test(case,args.prime)
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='certificates'},ensure_ascii=False),flush=True)
        Path(args.output).write_text(json.dumps({'method':'exact rational matrix; modular full-rank certificate; fixed centers in each case','results':results},ensure_ascii=False,indent=2),encoding='utf-8')
    return results


if __name__=='__main__':
    main()
