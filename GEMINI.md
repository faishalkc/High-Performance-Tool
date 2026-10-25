# Gemini Instructions

You are working on High Performance Tool, a small Windows desktop application built with Python and Tkinter. It interacts with Windows power plans through `powercfg`.

## Project Context

- Main script: `HPTool.py`
- Main application classes: `PowerPlan` and `HPToolWindow`
- Assets: `banner.png` and `icon.ico`, stored beside the main script
- Dependencies: listed in `requirements.txt`
- Target platform: Windows

## Implementation Guidelines

- First understand the relevant code and project context.
- Inspect only the files required for the requested task; do not perform a full project scan by default.
- Make small, maintainable changes and avoid unnecessary restructuring.
- Preserve existing behavior unless the user explicitly requests a change.
- Follow the current Python/Tkinter implementation and code style.
- Avoid adding dependencies unless they are justified.
- Treat `powercfg` operations and system power settings carefully; do not expand their scope beyond the request.
- Preserve compatibility with the existing asset paths.
- Update `README.md` when setup, usage, dependencies, or visible behavior changes.

## Verification

- Perform relevant checks when available.
- Be transparent about what was actually tested.
- Do not report successful tests or Windows behavior without verifying them.
- Mention when Windows-specific functionality could not be tested in the current environment.
