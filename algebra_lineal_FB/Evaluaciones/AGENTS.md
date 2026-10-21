# Repository Guidelines

## Project Structure & Module Organization

This directory contains Spanish-language LaTeX assessments for EPN linear algebra. Files live directly in the root; there are no separate source or test directories.

- `Miercoles_7_9.tex` is the current assessment entry point and uses `examenEPN0.cls`.
- `ComandoLocales.tex` supplies course metadata, student fields, instructions, and imports shared commands.
- `Comandos.tex`, `ComandosMath.tex`, and `comandosEPN*.sty` contain reusable macros; `examenEPN*.cls` define exam layouts. Other `.cls` and `.sty` files support additional document formats.
- `Logo_EPN.eps` and `Logo_DFB.eps`, plus their converted PDFs, provide institutional artwork.
- `.aux`, `.log`, `.fls`, `.fdb_latexmk`, and `.synctex.gz` files are generated compilation artifacts.

## Build, Test, and Development Commands

Run commands from this directory with a LaTeX distribution such as MiKTeX and the required packages installed. Existing build records use pdfLaTeX.

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error Miercoles_7_9.tex
```

Builds the assessment PDF and repeats compilation as needed. If `latexmk` is unavailable, run `pdflatex -interaction=nonstopmode -halt-on-error Miercoles_7_9.tex` twice to resolve references. Keep logo assets alongside the source so graphics resolve correctly.

## Coding Style & Naming Conventions

Preserve UTF-8 encoding, Spanish text, and existing command names. Use four spaces for newly indented environment contents, matching nearby code where practical. Follow the existing assessment filename pattern, such as `Miercoles_7_9.tex`. Reuse `\datosAlgebra`, `\indicacionesPrueba`, and `\puntaje` rather than duplicating formatting. Keep assessment content in its entry file and shared formatting in the appropriate macro or class file. No formatter or linter configuration is present.

## Testing Guidelines

There is no automated test framework or coverage requirement. Compile every changed assessment and inspect its PDF for clipped equations, logos, page breaks, answer space, dates, group labels, and point totals. Review the build log for errors, missing references, and overfull boxes. Independently check mathematical statements and solutions. Shared macro or class changes require recompiling all affected entry documents.

## Commit & Pull Request Guidelines

Git metadata is unavailable in this checkout, so existing commit conventions cannot be verified. Use concise, imperative messages, for example `Fix parameter-system question wording`. In pull requests, describe the affected assessment, summarize content or layout changes, and state compilation and visual checks performed. Link an issue when applicable; include PDF screenshots for layout changes. Avoid unrelated generated-artifact changes.