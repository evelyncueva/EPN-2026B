# Repository Guidelines

## Project Structure & Module Organization

This directory contains course materials within the parent `EPN2026` Git repository. Materials are grouped by session date: `Jueves26/`, `Lunes30/`, `Martes01/`, and `Miércoles02/`. Each session contains lecture PDFs such as `Clase13.pdf`. `Jueves26/` also contains reference summaries and the Python notebook `12-Perceptron-Lineal.ipynb`, which demonstrates linear perceptron training with NumPy and Matplotlib. There are no separate source, test, or asset directories.

## Build, Test, and Development Commands

Run these commands from `PUC_curso/` in a suitable Python environment:

- `python -m pip install notebook nbconvert numpy matplotlib` installs the notebook tools and imported libraries; no dependency manifest is currently provided.
- `jupyter notebook` starts the local notebook interface. Select a Python 3 kernel; the existing notebook records Python 3.11.3.
- `jupyter nbconvert --to notebook --execute "Jueves26/12-Perceptron-Lineal.ipynb" --output "12-Perceptron-Lineal.executed" --output-dir "$env:TEMP"` executes the notebook into a temporary output file in PowerShell.

There is no application build step. HTML5 animation rendering may require FFmpeg on `PATH`.

## Coding Style & Naming Conventions

Use four spaces for Python indentation and `snake_case` for new functions and descriptive variables. Preserve mathematical symbols where they clarify the lesson. Keep Spanish explanations, comments, and plot labels consistent with the surrounding material. Preserve fixed random seeds for reproducible examples. Follow existing session-folder and lecture-number naming patterns, and retain accents in paths. No formatter or linter is configured.

## Testing Guidelines

No automated test framework or coverage threshold is configured. After notebook changes, restart the kernel and run every cell in order. Check training output, plots, and animations, including examples that redefine functions across sections. Open changed PDFs to confirm legibility and page layout. Avoid committing temporary execution files or unrelated output changes.

## Commit & Pull Request Guidelines

Parent-repository history uses descriptive action-oriented messages in English and Spanish, such as `Add solutions and exercises for linear algebra and calculus topics`. Follow that style and identify the affected session or topic. Keep commits focused on related teaching materials. In pull requests, describe the educational change, list affected files, and state validation performed. Include screenshots for meaningful visual changes and link an issue when applicable. Review staged paths carefully to exclude unrelated parent-repository work.
