# Repository Guidelines

## Project Structure & Module Organization

This repository contains Spanish-language differential calculus notes for the 2026B term. Each week is self-contained:

- `semana_01/semana01.tex` and `semana_02/semana02.tex`: lesson content, exercises, solutions, and inline TikZ diagrams.
- `semana_XX/estilo_apuntes.sty`: local formatting package defining A5 layout, colors, headers, and teaching environments.
- `semana_XX/semanaXX.pdf`: compiled notes tracked alongside their sources.

For new weeks, follow the `semana_03/semana03.tex` naming pattern and include the required local style package. There are no separate application, test, or asset directories.

## Build, Test, and Development Commands

Install a LaTeX distribution such as MiKTeX or TeX Live with the packages required by `estilo_apuntes.sty`, plus TikZ. Compile from the week directory so LaTeX finds its local package:

```powershell
Set-Location semana_01
pdflatex -interaction=nonstopmode -halt-on-error semana01.tex
pdflatex -interaction=nonstopmode -halt-on-error semana01.tex
```

The second pass resolves cross-references. Alternatively, run `latexmk -pdf semana01.tex` to manage compilation passes automatically. Use the corresponding directory and filename for other weeks. Run `latexmk -c semana01.tex` to remove auxiliary build files while retaining the PDF.

## Coding Style & Naming Conventions

Save `.tex` and `.sty` files as UTF-8 and retain Spanish prose and mathematical terminology. Follow surrounding formatting; use two-space indentation inside lists and TikZ blocks. Reuse existing environments such as `definicion`, `ejemplo`, `ejercicios`, and `solucion`, and descriptive labels such as `fig:pares-ordenados-funcion`. Keep solutions inside `\ifmostrarSoluciones` conditionals. Review both local style copies when changing shared formatting. No formatter or linter is configured.

## Testing Guidelines

There is no automated test framework or coverage threshold. Compile every affected week, inspect logs for errors, unresolved references, and layout warnings, and review the resulting PDF for clipped equations, diagrams, and page breaks. Verify mathematical statements and worked solutions. Check both `\mostrarSolucionestrue` and `\mostrarSolucionesfalse` when modifying conditional content, then restore the intended setting.

## Commit & Pull Request Guidelines

Existing commits use descriptive action-oriented subjects in English or Spanish, without a consistent prefix scheme. Follow that pattern, for example: `Clarify domain restrictions in semana02`. Keep changes focused and update the corresponding PDF when changing notes. PR descriptions should identify affected weeks, explain content or formatting changes, report compilation and visual checks, and link relevant issues. Include PDF page screenshots when layout changes need review. Avoid committing auxiliary files such as `.aux`, `.log`, and `.out`.