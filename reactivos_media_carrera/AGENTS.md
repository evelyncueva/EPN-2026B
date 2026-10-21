# Repository Guidelines

## Project Structure & Module Organization

This directory currently contains PDF documents rather than a software application:

- `2. MATD124 Calculo diferencial.pdf`
- `quipux.pdf`
- `AGENTS.md`: contributor instructions.

Keep related documents in the repository root while the collection remains small. No source-code, test, or asset directories currently exist. If editable document sources are added, explain their location and how they produce the corresponding PDFs.

## Build, Test, and Development Commands

There is no configured build system, package manager, application runtime, or automated test suite. Use these PowerShell commands to inspect the collection:

```powershell
Get-ChildItem -File
Get-ChildItem -Filter *.pdf | Select-Object Name, Length
```

The first lists files; the second lists PDFs and their sizes. Open changed PDFs in a local viewer for review. If a document-generation workflow is introduced, document its prerequisites and exact commands here.

## Document Style & Naming Conventions

Preserve existing filenames unless a rename is necessary and explained. For new course materials, use descriptive filenames containing the course code and topic, following the existing `MATD124` example. Quote filenames containing spaces in shell commands.

Use clear Markdown headings and short paragraphs for documentation. No formatter, linter, programming-language style, or indentation standard is currently configured.

## Validation Guidelines

Before submitting a PDF, verify that it opens, every page renders, and text, equations, and figures remain legible. Check page order and ensure the filename describes the document. Review changed academic content for correctness. There is no automated coverage requirement.

## Commit & Pull Request Guidelines

No Git metadata is available in this checkout, so existing commit conventions cannot be verified. When version control is used, write concise, action-oriented messages, such as `docs: add MATD124 practice questions`.

Describe which documents changed, why, and what manual validation was performed. Link a related issue when available. Include page references or screenshots when they help reviewers assess layout or content changes.
