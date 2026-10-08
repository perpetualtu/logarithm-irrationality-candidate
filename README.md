# Logarithm irrationality: candidate proof

This repository contains a standalone candidate proof of

$$
\mu(\log 2)=2,
\qquad
\mu(\log a)=2\quad\text{for every }a\in\mathbb Q_{>0}\setminus\{1\}.
$$

Here `log` denotes the real natural logarithm and `μ` denotes the irrationality exponent. The manuscript includes the full proposed interpolation proof, determinant estimates, parameter selection, and rational-base extension. It also derives the same exponent for every nonzero finite rational linear combination of logarithms of positive rational numbers, and for `log α` when `α > 0`, `α ≠ 1`, and `α^N` is rational for some positive integer `N`.

**Status: candidate-complete after internal audits; independent mathematical review and formal verification remain pending.** Internal readers have not identified a fatal inference in the inspected chain. Their agreement, successful compilation, and finite computational checks do not certify a theorem. This repository must not be used to describe an updated verified bound in the literature. No exhaustive novelty or current-record claim is made.

## Read the manuscript

- [paper.pdf](paper.pdf): the complete candidate manuscript.
- [paper.tex](paper.tex): its standalone LaTeX source, including the bibliography; no external TeX inputs or figures are required.
- [VERIFICATION.md](VERIFICATION.md): the dependency chain, audit scope, reproducible checks, and verification limits.
- [中文说明](README.zh-CN.md).

The quantified proposed statement is: for each fixed positive rational `a ≠ 1` and each real `ν > 2`, there is a threshold `Q(a, ν)` such that

$$
|\log a-p/q|\ge q^{-\nu}
\quad\text{for every }p\in\mathbb Z,\ q\in\mathbb Z,\ q\ge Q(a,\nu).
$$

The argument does not assert an effective threshold or one threshold uniform over all rational bases. The lower bound `μ ≥ 2` comes from Dirichlet's theorem; the proposed new content is the upper bound.

## Reproduce the artifacts

Use Python 3 with its standard library and a LaTeX installation providing `pdflatex` and the packages listed in `paper.tex`. Run these commands from the repository root:

```sh
python checks/interpolation_rank.py
python checks/rational_base_denominators.py
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The checks write [certificates/interpolation_rank.json](certificates/interpolation_rank.json) and [certificates/rational_base_denominators.json](certificates/rational_base_denominators.json). They reproduce selected finite instances using exact arithmetic. They do not prove eventual interpolation for every admissible set of parameters or the irrationality-exponent statement. See [VERIFICATION.md](VERIFICATION.md) for their precise scope.

## Provenance and license

Sections 2–4 adapt the local multiplicity, projective interpolation, determinant, and parameter mechanisms in OpenAI's [*The irrationality exponent of π is 2*, dated 24 September 2026](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf). The proposed modifications use distinct multiplicative centers `Y = 2^j`, then `Y = a^j`, with additional rational-base denominator clearing and target-dependent analytic bounds. The manuscript credits the earlier work used by that method.

This is a research draft prepared with Codex. Attribution to the source manuscript does not imply OpenAI authorship or endorsement of this repository. The source theorem's posted Lean development has not been rebuilt here and does not certify this logarithm extension.

The repository is distributed under [Apache License 2.0](LICENSE). [NOTICE](NOTICE) records the adaptation and attribution. The license file is reproduced verbatim from the license accompanying the source material.
