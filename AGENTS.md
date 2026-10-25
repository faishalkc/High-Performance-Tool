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

The repository may also contain project documentation such as `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and this instruction file.

## Working Principles

- Read the relevant project context before making changes.
- Inspect only the files needed for the requested task; do not scan the entire project by default.
- Prefer a small, targeted change over broad refactoring.
- Preserve existing behavior unless the task explicitly requests a behavior change.
- Avoid adding dependencies unless they are necessary and justified.
- Do not claim that tests or validation were performed unless they were actually run.

## Application Guidelines

- `HPTool.py` is the main application script.
- Preserve the existing responsibilities and style of `PowerPlan` and `HPToolWindow`.
- Keep the UI based on Tkinter unless the requested task calls for a different approach.
- Treat `powercfg` interactions as Windows-specific. Handle command errors and unexpected output sensibly.
- Do not assume Windows-specific behavior can be validated in a non-Windows environment.
- Keep `banner.png` and `icon.ico` compatible with the app's existing asset-loading paths.
- Avoid changing power-plan behavior, command arguments, or system settings beyond the scope of the request.

## Dependencies and Compatibility

- Check `requirements.txt` before introducing or changing third-party dependencies.
- Prefer Python standard-library features when practical.
- Keep changes compatible with the project's intended Windows environment.
- Do not add platform support claims unless the application has actually been adapted and verified for those platforms.

## Documentation

- Update `README.md` when a change affects installation, usage, dependencies, or visible behavior.
- Keep documentation accurate and concise.
- Do not add a changelog unless explicitly requested.

## Validation

When relevant and available:

- Run a syntax check or other focused validation.
- Launch the application on Windows to check UI behavior.
- Verify the relevant power-plan operation and error handling.
- Report what was and was not tested clearly.

## Git and Scope

- Do not modify unrelated files.
- Do not overwrite user changes.
- Avoid committing generated files, local environments, caches, or secrets.
