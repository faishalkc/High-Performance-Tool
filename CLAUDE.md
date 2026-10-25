# Claude Instructions

You are working on High Performance Tool, a lightweight Windows utility written in Python with a Tkinter interface. The application uses `powercfg` to interact with Windows power plans.

## Project Context

- `HPTool.py` is the main application script.
- The application includes the `PowerPlan` and `HPToolWindow` classes.
- `banner.png` and `icon.ico` are project assets located beside the main script.
- `requirements.txt` lists third-party dependencies.
- The project is intended for Windows; `powercfg` behavior is platform-specific.

## How to Work

- Understand the relevant project context before implementing a request.
- Inspect only the files necessary for the requested task. Avoid scanning the entire repository without a reason.
- Prefer focused, minimal changes over unnecessary refactoring.
- Preserve the existing application behavior unless a change is explicitly requested.
- Keep the existing Python and Tkinter approach unless the task requires otherwise.
- Avoid adding dependencies without a clear need.
- Be cautious when changing `powercfg` calls or system power settings; make only the changes requested.
- Keep asset paths compatible with the current project layout.
- Update the README if installation, usage, dependencies, or visible behavior changes.

## Validation and Reporting

- Run relevant checks when possible and state exactly what was checked.
- Do not claim tests passed if they were not run.
- If you cannot test Windows-specific functionality in the current environment, say so.
- Keep the final summary concise and mention relevant limitations.
