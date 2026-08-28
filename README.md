# Notas de Biomate — Sistemas Dinámicos No Lineales

Course notes for **Matemáticas Biológicas** (Mathematical Biology), written in
the tradition of nonlinear dynamics à la Strogatz, with biological modeling
(Murray, Edelstein-Keshet, May) woven throughout.

**Author:** Ulises Rayón

The notes follow a geometric, intuition-first philosophy: phase lines before
formalism, vector fields before closed-form solutions, and applications drawn
from physics, neuroscience, and population biology in every chapter.

## Contents

| Part | Chapters | Topics |
|------|----------|--------|
| I — Preliminares | 1–2 | Course policy; historical overview (Newton → Poincaré → Lorenz → May → Feigenbaum) |
| II — Flujos en una dimensión | 3–8 | Phase space & geometric thinking; 1D flows; fixed points & stability; linear stability analysis; potentials & mechanical analogy |
| III — Bifurcaciones | 9–14 | Saddle-node & normal forms; transcritical; the laser threshold (Haken); pitchfork; neural-network activation functions; Newton–Raphson |
| IV — Sistemas en dos dimensiones | 15–19 | Linear 2D classification; phase planes & nullclines; conservative systems & Poincaré–Bendixson; Lotka–Volterra & limit cycles; Hopf bifurcation |
| V — Estudio de caso | 20 | **Erythropoiesis & anemia** — a 4D model (Dor & Alon, 2026) reduced to 1D, then 2D, with full qualitative analysis and a backward map of every tool used |

Every chapter ends with graduated exercises (mechanics → analysis →
biological interpretation).

## Building

Requires a standard TeX Live install with `latexmk`, `biber`, and `pygments`
(for `minted`):

```bash
latexmk -pdf -shell-escape notas.tex
```

The output is `notas.pdf` (~93 pp). All figures are native TikZ/PGFPlots —
no external image files are needed.

## Repository layout

```
notas.tex            master document (preamble, parts, chapter inputs)
chapters/            one .tex per chapter (1–20)
refs.bib             bibliography (biblatex/biber)
previous_docs/       scanned source drafts and OCR transcriptions
body/                legacy demo content (integrated into ch. 18)
lexer/               NetLogo lexer for minted highlighting
```

## License

MIT — see [LICENSE](LICENSE).
