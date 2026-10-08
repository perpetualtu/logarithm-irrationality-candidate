# Verification record and boundary

**Result class: candidate complete resolution.** The manuscript presents a complete proposed chain for `μ(log 2) = 2` and its rational-logarithm extension. Internal mathematical audits have not located a fatal inference or an unproved required sublemma in the inspected chain. This is a report about internal review, not independent peer review or certification by Lean, Coq, Isabelle, or another proof kernel.

## Exact claim and conventions

For irrational real `x`, the manuscript uses

$$
\mu(x)=\sup\{\nu>0:0<|x-p/q|<q^{-\nu}
\text{ for infinitely many coprime }p\in\mathbb Z,\ q\ge2\}.
$$

All logarithms of positive numbers are real natural logarithms. The local expression `log(1+t)` is its formal Taylor series, also used analytically on the indicated small disk.

For every fixed `a ∈ Q_{>0} \ {1}` and real `ν > 2`, the candidate theorem asserts the existence of `Q(a, ν)` such that all integers `p` and `q ≥ Q(a, ν)` satisfy `|log a − p/q| ≥ q^(−ν)`. The proposed contradiction actually excludes arbitrarily large denominators with error at most `q^(−ν)`. Unreduced fractions and zero error are allowed in that contradiction, so irrationality is not assumed circularly. Dirichlet's theorem supplies the reverse inequality `μ ≥ 2` once irrationality is established.

Neither an effective `Q(a, ν)` nor a threshold uniform over all bases is asserted. Exponent `ν = 2` is outside the eventual-lower-bound quantifier.

## Main mathematical dependency chain

| Dependency | Role in the proposed proof | Point requiring scrutiny |
| --- | --- | --- |
| Weighted transverse multiplicity | Compares products of coordinate weights and commuting-field costs from a local length lower bound and weighted Bézout upper bound. | Local coordinates on a transverse slice; ideal-inclusion direction; isolated intersection multiplicities; uniformity when components vary. |
| Curve inequality | Converts excess weighted contact into persistent derivative vanishing, then forces `Y` to be constant by the residue obstruction `dX_i = dY/Y`. | All normalization branches; selection of normal bases; center-independent separation thresholds; the constant-`Y` case. |
| Separated-weight interpolation | Turns the curve inequality into eventual surjectivity onto every coefficient packet of strict weight `< H`. | Ordinary Rees blow-up, ampleness, ordinary powers `I^n`, high-degree pushdown, and Serre vanishing. |
| Full-row-rank minor | Supplies a nonzero determinant from interpolation. | Its nonvanishing is an output of interpolation, not an assumption used to prove interpolation. |
| Arithmetic lower bound | Clears the rational Taylor and approximation denominators and uses a nonzero integer determinant. | Exact row and column scaling; LCM bound; signs of row benefits and column costs. |
| Exact row translation | Rewrites approximate-center rows using entire test functions at exact logarithmic centers. | Finite expansion identity; tail budget; bounds uniform over selected columns. |
| Collision estimate | Repeated Taylor degrees in a transverse-index group make determinant terms vanish, giving quadratic saving. | Absolute convergence; cancellation only within the same index group; uniform remainder as `H → ∞`. |
| Determinant comparison | Uses either many low-index rows or many high-index rows to contradict the arithmetic lower bound. | Both alternatives are exhaustive; lattice counts and normalized errors have fixed positive margins. |
| Parameter selection | Realizes those margins for each real `ν > 2`. | A finite dimension is fixed before choosing approximation scales; all data are fixed before the degree limit. |
| Rational-base extension and rational scaling | Handles `a = u/v`, then obtains rational-logarithm combinations and rational powers as corollaries. | Exact denominator clearing, absorption in the `Y` budget, sign-safe analytic radius, and fixed-factor denominator comparisons. |

The logical order is

```text
local multiplicity -> curve inequality -> interpolation -> nonzero minor
nonzero minor + arithmetic + translation + collision -> determinant comparison
parameter selection + determinant comparison -> eventual lower bound
eventual lower bound -> irrationality; Dirichlet -> exponent exactly 2
rational-base clearing + analytic bounds -> same chain for each rational base
rational scaling -> rational-logarithm combinations and rational-power corollaries
```

The proposed argument supplies its own modified geometric proof. It does not use the theorem `μ(π) = 2` as a black-box premise.

## Essential order of quantifiers

The interpolation statement fixes integers `m, K ≥ 1` and positive rational `w_0, v_0, θ` with

$$
0<\theta<1,\qquad K\theta^m<1,\qquad
K(w_0/v_0)\theta^m<1.
$$

It then permits successive sufficiently large positive rational weights `w_1, …, w_m`. Each lower threshold depends only on the fixed basic parameters and earlier weights. It is independent of all center coordinates. Put `W = (w_0, w_1, …, w_m)` and `V = (v_0, w_1/θ, …, w_m/θ)`.

Only after the weights are fixed are arbitrary centers `(y_j, c_{j1}, …, c_{jm})` chosen, with nonzero pairwise distinct `y_j`. The polynomial-to-jet map uses `Y = y_j(1+t)` and `X_i = c_{ji}+u_i+log(1+t)`. The source has weighted degree `≤ H`; the target retains monomials with strict `V`-weight `< H`.

A divisibility step for `H` can depend only on the weights. The eventual lower threshold for `H` can depend on the fixed centers. A single threshold working simultaneously for every center configuration is not required. The application chooses a finite dimension, approximation weights, and centers before letting `H` tend to infinity.

The nonzero and distinct-`Y` hypotheses matter. Internal audits include dimension obstructions when either is removed. Cases violating these hypotheses or the sufficient separation thresholds are not counterexamples to the stated theorem.

## Rational-base extension

Write `a = u/v` in lowest terms with `u, v` positive integers. At centers `y_j = a^j`, scale a column `Y^h X^α` by

$$
v^{(K-1)h}\prod_i q_i^{\alpha_i},
$$

and a row indexed by `(j, s, β)` by `∏ q_i^(−β_i)`. After multiplying by the stated Taylor-denominator factor, entries are integers because their base factor is

$$
u^{jh}v^{(K-1-j)h}.
$$

Both powers are nonnegative for `0 ≤ j < K`. The extra column cost is `(K−1)h log v`. Choosing `w_0 ≥ (K−1) log v` absorbs it in the original budget `w_0 h + w·α ≤ H`, with no new leading arithmetic loss.

For each fixed base, an analytic radius proportional to `K(1+|log a|)` covers the translated centers. This handles `0 < a < 1` and negative approximation numerators. The chosen dimension makes the radius-to-`w_0` ratio and the rational-denominator cost small before approximation weights and centers are fixed.

For a nonzero finite combination `ω = ∑ b_k log a_k`, where `b_k ∈ Q` and `a_k ∈ Q_{>0}`, choose a positive integer `N` clearing the `b_k`. Then `Nω = log r` for a positive rational `r ≠ 1`. Invariance of irrationality exponent under nonzero rational scaling gives the stated corollary. Similarly, `α^N ∈ Q_{>0}` gives `N log α = log(α^N)`. This does not assert exponent two for arbitrary positive algebraic bases.

## Internal audit scope

The full `log 2` derivation received an internal step-by-step audit on 7 October 2026. It covered local multiplicity, the curve inequality, the geometric interpolation passage, the arithmetic and analytic determinant bounds, parameter existence, the degree-limit order, and the final irrationality and Dirichlet arguments. Supporting exact parameter and row-identity diagnostics passed. Those earlier diagnostics are audit context; this repository's released checks are listed below.

A second internal audit on 8 October 2026 concentrated on the distinct-`Y` interpolation proof. Separate reviews examined the curve argument, the ordinary blow-up and global passage, and attempts to construct structural counterexamples. The audit found no counterexample under the stated hypotheses. Its scope did not constitute a fresh review of every subsequent determinant estimate. The rational-base route separately checked its denominator formula, sign handling, analytic radius, and parameter order.

The status boundary is absence of independent or formal certification. No particular missing mathematical lemma is being asserted here. Agreement among model reviewers is not a proof certificate.

## Reproducible finite checks

From the repository root, use Python 3 with its standard library:

```sh
python checks/interpolation_rank.py
python checks/rational_base_denominators.py
```

| Check | Output | What it establishes |
| --- | --- | --- |
| [checks/interpolation_rank.py](checks/interpolation_rank.py) | [certificates/interpolation_rank.json](certificates/interpolation_rank.json) | Matrix dimensions and exact or prime-field rank for the specified finite center, weight, and degree configurations; full-rank pivot columns where recorded. |
| [checks/rational_base_denominators.py](checks/rational_base_denominators.py) | [certificates/rational_base_denominators.json](certificates/rational_base_denominators.json) | Exact coefficient-level denominator clearing for the specified finite rational bases, approximants, monomials, and Taylor orders. |

The interpolation checks include the admissible configuration `m=1`, `K=2`, `θ=1/10`, `w_0=v_0=1`, `w_1=21`, and centers `(1,0)`, `(−1,0)`. At `H=210`, the target/source dimensions are `420 × 1166`; at `H=420`, they are `1260 × 4431`. Their full-row-rank certificates modulo the prime `1000003` prove full row rank over the rationals and complex numbers for those finite matrices: a nonzero minor modulo the prime is a nonzero rational minor after denominator clearing. They do not determine a uniform large-degree threshold. Low-degree and insufficiently separated diagnostic cases must be interpreted according to their recorded hypotheses.

The rational-base checks cover 56,000 coefficients for bases `2/3`, `3/2`, `1/5`, `5`, and `101/103`, with `K=4`, `h` and both transverse monomial exponents from `0` through `3`, Taylor orders `0` through `6`, and truncation cutoffs `3` and `5`. The chosen approximation numerators are `5` and `−3`, with denominators `7` and `11`. Exact rational arithmetic verifies that every coefficient becomes an integer after the proposed row, column, and Taylor-denominator scaling. A successful finite coefficient check supports the clearing formula; the all-parameter statement relies on the written identity.

These JSON files are computational certificates for the recorded finite instances. They are not proof-kernel certificates for the geometric theorem, its asymptotic quantifiers, the analytic bounds, or the final irrationality exponents. An audit of the released manuscript should follow the mathematical dependency chain above.

## Compile the manuscript

The source is standalone and includes its bibliography. With `pdflatex` and the packages declared in `paper.tex`, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Run at least two passes, and rerun if LaTeX requests another pass to settle the contents or outlines. Successful compilation checks document syntax and rendering, not mathematical truth. No Lean build or other formal verification is claimed by this repository.

## Source attribution and external dependencies

Sections 2–4 adapt OpenAI's [*The irrationality exponent of π is 2*, dated 24 September 2026](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf). Its posted Lean work has not been rebuilt or exhaustively audited here, and its statement concerns `π`, not this extension. The adaptation and [Apache-2.0 license](LICENSE) are recorded in [NOTICE](NOTICE).

The manuscript supplies the changed argument and cites these dependencies precisely:

- [Mondal, *How many zeroes?*, arXiv:1806.05346v5](https://arxiv.org/abs/1806.05346v5), Corollary VIII.3 and Section IV.4.2: isolated intersection multiplicities and the Bézout bound used in local multiplicity.
- The Stacks Project, [02OS](https://stacks.math.columbia.edu/tag/02OS), [02ND](https://stacks.math.columbia.edu/tag/02ND), and [02NS](https://stacks.math.columbia.edu/tag/02NS): ordinary blow-up and its projective and tautological-bundle properties.
- The Stacks Project, [0AG7](https://stacks.math.columbia.edu/tag/0AG7) and [0AG6](https://stacks.math.columbia.edu/tag/0AG6): high-degree graded-piece comparison and higher-cohomology vanishing for the ordinary Rees algebra.
- The Stacks Project, [0B5U](https://stacks.math.columbia.edu/tag/0B5U): Serre vanishing; [0BXX](https://stacks.math.columbia.edu/tag/0BXX), Theorem 53.2.6 and Lemma 53.2.8: smooth complete curve models.
- Lazarsfeld, *Positivity in Algebraic Geometry I* (2004), Corollary 1.4.10: positive combinations of nef and ample classes, in the projective-scheme setting. The [author's Chapter 1](https://www.math.stonybrook.edu/~roblaz/Reprints/Laz.PAG.Chapt1.pdf) is available for review.

Historical mechanism attribution to Demailly, Philippon, and Laurent is retained in the manuscript bibliography. Those references do not replace the modified proof given here. Classical logarithm bounds are background; the repository does not claim to have established the current literature record or a newly verified bound.

## Publication preparation on 8 October 2026

The merged standalone manuscript has 23 pages. Compilation has no unresolved
references or overfull boxes. All pages were rendered and visually inspected;
no out-of-page glyphs were found. The source/PDF hashes and document checks are
recorded in [certificates/document_checks.json](certificates/document_checks.json).
These are document-quality checks, not mathematical certification.

A fresh internal audit separately checked the rational-logarithm extension's
row and column clearing, the analytic disk and normalized Taylor expansion,
both determinant alternatives, fixed-base parameter order, rational scaling,
and the two corollaries. It found no invalid inference conditional on the
stated interpolation theorem. The integer domain of the denominator was made
explicit in the extension theorem. This audit does not certify the geometry.

The released rational-base script was rerun successfully on its 56,000 exact
coefficients. The released rank script was also rerun on the small-degree and
generic rational-center cases, matching the inherited nine-case certificate.
The full nine-case JSON records the preceding interpolation re-audit run.
