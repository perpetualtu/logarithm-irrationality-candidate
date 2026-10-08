# 对数无理度数：候选证明

本仓库提供完整、可独立编译的候选论文，主张

$$
\mu(\log 2)=2,\qquad
\mu(\log a)=2\quad(a\in\mathbb Q_{>0}\setminus\{1\}).
$$

`log` 为实自然对数，`μ` 为无理度数。论文包含不同乘法中心的插值证明、行列式估计、参数选择，以及有理底数扩展。推论覆盖正有理数对数的非零有限有理线性组合，也覆盖满足 `α > 0`、`α ≠ 1`、某个正整数次幂 `α^N` 为有理数的 `log α`；未声称覆盖全部正代数数。

**当前状态：经过内部审查的候选完整证明，尚无外部数学家确认或形式化内核认证。** 已审查链中未定位到致命错误；模型一致意见、有限计算及编译成功都不能替代证明认证。不能依据本仓库把文献中的已验证界更新为 `2`，也不主张已完成穷尽的新颖性或最新纪录核查。

- [完整论文 PDF](paper.pdf)
- [独立 LaTeX 源码](paper.tex)
- [验证说明及依赖链](VERIFICATION.md)
- [English README](README.md)

对每个固定的正有理数 `a ≠ 1` 和每个实数 `ν > 2`，候选证明给出 `Q(a, ν)`，使所有整数 `p` 及 `q ≥ Q(a, ν)` 满足 `|log a − p/q| ≥ q^(−ν)`。阈值可以依赖底数，未声称有效计算或对所有底数统一。

在仓库根目录，使用 Python 3 标准库运行有限检查，再用含所需宏包的 LaTeX 环境编译两遍：

```sh
python checks/interpolation_rank.py
python checks/rational_base_denominators.py
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

检查结果写入 `certificates/`。有限实例证书不证明全部参数下的插值定理；详见 [VERIFICATION.md](VERIFICATION.md)。

论文第 2–4 节改编自 OpenAI 的 [*The irrationality exponent of π is 2*，2026 年 9 月 24 日稿](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf)。本仓库是借助 Codex 整理的研究草稿；引用和改编不表示 OpenAI 对本仓库署名或背书。采用 [Apache-2.0 许可证](LICENSE)，改编说明见 [NOTICE](NOTICE)。
