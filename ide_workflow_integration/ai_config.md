
## Objective

Configure AI-assisted development in Visual Studio Code for a WSL-based workflow.

## Environment

- IDE: Visual Studio Code
- Development environment: WSL2
- AI assistant: GitHub Copilot
- AI chat tool: GitHub Copilot Chat
- Primary language: Python
- Additional languages: JavaScript, TypeScript, HTML, CSS, JSON, Bash

## AI Configuration Goals

- Keep Python code clean, typed where useful, and easy to test
- Keep JavaScript and TypeScript code consistent and readable
- Use AI support for code review and documentation generation
- Make AI suggestions align with project structure and coding standards
- Keep generated output practical, minimal, and ready for review

## AI Features Enabled

- Inline code suggestions
- Copilot Chat
- Project-specific AI rules
- Language-specific coding guidance
- Specialized workflows for code review and doc generation

## Language-Specific Rules

### Python
- Prefer clear and simple functions
- Use type hints when they improve readability
- Follow Black-style formatting
- Prefer small, testable units
- Use pytest for tests when needed
- Add docstrings for public functions and modules

### JavaScript
- Prefer modern ES syntax
- Use semicolons
- Keep functions small and readable
- Prefer explicit variable names
- Follow ESLint-friendly patterns

### TypeScript
- Prefer strict typing
- Avoid `any` unless necessary
- Use interfaces or types for structured data
- Keep functions and components focused
- Prefer readable, maintainable code over clever code

### HTML and CSS
- Use semantic HTML
- Keep structure simple and accessible
- Prefer clear class names
- Avoid unnecessary nesting
- Write CSS that is easy to maintain

## Specialized AI Workflows

### 1. Code Review Workflow
Purpose:
- Review generated or edited code before accepting it

Focus areas:
- Correctness
- Readability
- Simplicity
- Edge cases
- Security basics
- Performance for obvious problems

Expected behavior:
- Point out risks clearly
- Suggest small, practical fixes
- Prefer maintainable changes over complex rewrites

### 2. Documentation Workflow
Purpose:
- Generate short technical documentation for code and project files

Focus areas:
- Function summaries
- Module purpose
- Setup instructions
- Usage examples
- Clear README-style explanations

Expected behavior:
- Keep documentation concise
- Match the code accurately
- Avoid unnecessary repetition
- Prefer examples when useful

