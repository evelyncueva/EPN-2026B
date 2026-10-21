# Repository Guidelines

## Project Structure & Module Organization

This repository contains Spanish-language LaTeX materials for EPN linear algebra courses.

- `Apuntes2026B/`: current semester lesson notes, local document classes, style packages, and institutional logos.
- `Apuntes 2025-A/`: earlier notes, including bimonthly compilations and weekly lessons under `Primer bimestre/` and `Segundo bimestre/`.
- `Evaluaciones/`: assessments and their supporting LaTeX resources. Read its existing `AGENTS.md` before editing this directory.
- `Graficos/`: EPS illustrations used in course materials.

Files such as `.pdf`, `.aux`, `.log`, and `.synctex.gz` appear alongside sources. Treat `.tex`, `.sty`, `.cls`, and original graphics as editable inputs.

## Build, Test, and Development Commands

Install a LaTeX distribution such as MiKTeX or TeX Live with `pdflatex` and, preferably, `latexmk`. Compile from the document directory so local packages and logos resolve:

```powershell
Set-Location Apuntes2026B
latexmk -pdf -interaction=nonstopmode -halt-on-error Semana03_clase01.tex
```

Alternatively, run `pdflatex -interaction=nonstopmode -halt-on-error Semana03_clase01.tex` twice to resolve references. Quote filenames containing spaces, for example `"Semana04_clase 01.tex"`. EPS assets require the distribution's EPS-to-PDF conversion support. No project-wide build script or automated test suite was found.

## Coding Style & Naming Conventions

Keep instructional prose in Spanish and preserve accents and existing file encoding. Follow nearby LaTeX formatting; use four spaces when indenting new environment content. Reuse established macros and environments such as `\R`, `\Mat`, `defi`, `teo`, and `ejem`.

For new current-semester lessons, follow `Semana03_clase01.tex`. Preserve existing filenames and relative asset paths. Edit shared `.sty` or `.cls` files only when the change should affect all documents using them. No formatter or linter configuration is provided.

## Testing Guidelines

Compile each affected document and inspect its log for errors, undefined references, and layout warnings. Review the PDF for equations, numbering, accents, logos, and page breaks. Check mathematical examples and solutions independently. Shared template changes require compiling representative dependent documents. There is no automated coverage requirement.

## Commit & Pull Request Guidelines

Git metadata is unavailable in this checkout, so historical commit conventions cannot be verified. Use concise, descriptive messages such as `Fix row reduction example in week 03 notes`. Keep changes focused. Pull requests should identify affected lessons, explain mathematical or template changes, and report compilation results. Include PDF excerpts or screenshots for layout changes and link relevant issues when available.