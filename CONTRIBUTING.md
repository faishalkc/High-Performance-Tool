# Contributing to High Performance Tool

Thank you for your interest in contributing to High Performance Tool!

Contributions such as bug reports, suggestions, documentation improvements, and code changes are welcome. This project is a lightweight Windows utility, so please keep contributions focused and straightforward.

## Reporting Bugs

Before opening an issue:

- Check whether the issue has already been reported.
- Make sure you are using a supported Windows environment.
- Include clear steps to reproduce the problem.

When reporting a bug, provide as much relevant information as possible:

- Windows version.
- Python version, if running the script directly.
- The behavior you expected and what happened instead.
- Any error message or traceback.
- Whether the issue is related to changing the Windows power plan with `powercfg`.

Please do not include personal information or sensitive system details in issue reports.

## Suggesting Features

Feature suggestions are welcome. Please explain:

- The problem or use case the feature would address.
- How you expect the feature to work.
- Any relevant limitations or considerations.

Keep suggestions aligned with the purpose of High Performance Tool: a simple utility for managing the Windows power plan.

## Contributing Code

1. Fork the repository.
2. Create a branch for your change.
3. Make your changes.
4. Review the changes and verify the application behaves as expected.
5. Open a pull request with a clear description.

For example:

```bash
git checkout -b fix/describe-the-change
```

## Development Guidelines

- Keep the application compatible with its intended Windows environment.
- Preserve the existing Python and Tkinter approach unless a change is necessary.
- Keep changes focused; avoid introducing dependencies without a clear need.
- Preserve the existing behavior of `powercfg` interactions and handle command failures appropriately.
- Keep `banner.png` and `icon.ico` paths compatible with the project's existing asset layout.
- Follow the existing code style and use clear, descriptive names.
- Update the README if a change affects setup, usage, or visible application behavior.

## Validation

Before submitting a pull request:

- Run the application on Windows, when possible.
- Check the relevant power-plan behavior and confirm errors are handled sensibly.
- If you run into an environment where Windows-specific functionality cannot be tested, mention that in the pull request.

Do not state that tests passed unless you actually ran them.

## Pull Requests

Please include:

- A short summary of the change.
- The reason for the change.
- Any relevant testing or manual verification.
- Screenshots, when useful for a user-interface change.

Thank you for helping improve High Performance Tool!
