# AI Agent Instructions

## Project Overview

High Performance Tool is a lightweight Windows desktop utility written in Python. It uses Tkinter for its graphical interface and `powercfg` to interact with Windows power plans.

Keep the project simple, focused, and consistent with its existing implementation.

## Project Structure

```text
High-Performance-Tool/
├── HPTool.py
├── banner.png
├── icon.ico
├── requirements.txt
└── README.md
```

The repository may also contain documentation such as `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`.

## Working Principles

- Understand the relevant project context before making changes.
- Inspect only the files needed for the requested task; do not scan the entire project by default.
- Prefer small, targeted changes over broad refactoring.
- Preserve existing behavior unless the task explicitly requests a behavior change.
- Avoid adding dependencies unless necessary and justified.
- Do not claim that tests or validation were performed unless they were actually run.

## Application Guidelines

- `HPTool.py` is the main application script.
- Preserve the existing responsibilities and style of `PowerPlan` and `HPToolWindow`.
- Keep the interface based on Tkinter unless the task calls for a different approach.
- Treat `powercfg` interactions as Windows-specific. Handle command errors and unexpected output sensibly.
- Do not assume Windows-specific behavior can be validated in a non-Windows environment.
- Keep `banner.png` and `icon.ico` compatible with the existing asset-loading paths.
- Avoid changing power-plan behavior, command arguments, or system settings beyond the requested scope.

## Dependencies and Compatibility

- Check `requirements.txt` before adding or changing third-party dependencies.
- Prefer standard-library features when practical.
- Keep changes compatible with the project's intended Windows environment.
- Do not claim support for other platforms unless the application has been adapted and verified.

## Documentation

- Update `README.md` when a change affects installation, usage, dependencies, or visible behavior.
- Keep documentation accurate and concise.
- Do not add a changelog unless explicitly requested.

## Validation

When relevant and available:

- Run a syntax check or focused validation.
- Launch the application on Windows to check UI behavior.
- Verify the relevant power-plan operation and error handling.
- Clearly report what was and was not tested.

## Git and Scope

- Do not modify unrelated files.
- Do not overwrite user changes.
- Avoid committing generated files, local environments, caches, or secrets.
