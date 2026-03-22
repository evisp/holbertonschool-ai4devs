# setup_notes.md

## Objective

Prepare Visual Studio Code and GitHub Copilot for AI-assisted development and project testing.

## Environment

- IDE: Visual Studio Code
- Development environment: WSL2
- Primary language: Python
- Additional languages: JavaScript, TypeScript, HTML, CSS, JSON, Bash
- AI assistant: GitHub Copilot
- AI chat tool: GitHub Copilot Chat

## Tool Versions

Record the exact installed versions from the local machine.

- VS Code: `1.112.0`
- WSL: `2.0`
- Python: `3.10.12`
- pip: `22.0.2`
- Node.js: `v24.13.0`
- npm: `11.6.2`
- Git: `2.34.1`

## Extensions Installed

- GitHub Copilot
- GitHub Copilot Chat
- Remote - WSL
- Python
- Pylance
- Python Debugger
- ESLint
- Prettier - Code formatter
- Docker

## Setup Steps

1. Installed Visual Studio Code on Windows.
2. Installed and enabled WSL2.
3. Opened the project from WSL using `code .`.
4. Installed the **Remote - WSL** extension.
5. Confirmed VS Code is running in a WSL window.
6. Installed **GitHub Copilot**.
7. Installed **GitHub Copilot Chat**.
8. Signed in with GitHub inside VS Code.
9. Enabled Copilot suggestions and Copilot Chat.
10. Installed the **Python** extension.
11. Installed **Pylance**.
12. Installed **Python Debugger**.
13. Installed **ESLint**.
14. Installed **Prettier - Code formatter**.
15. Installed **Docker** for container-related workflows.
16. Selected the Python interpreter inside WSL.
17. Verified Python runs correctly in the integrated terminal.
18. Verified Copilot suggestions appear in code files.
19. Verified Copilot Chat works inside VS Code.

## Basic Workspace Configuration

Created `.vscode/settings.json` with a simple AI-ready setup:

```json
{
  "editor.formatOnSave": true,
  "files.trimTrailingWhitespace": true,
  "python.defaultInterpreterPath": "/usr/bin/python3",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  }
}
