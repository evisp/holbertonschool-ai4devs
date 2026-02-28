# Refactoring for Readability Prompt Template

**Role / Perspective**: Act as a Senior Software Engineer with 8+ years of experience maintaining large production codebases.

**Task Description**: Refactor the provided [LANGUAGE] code to improve readability and maintainability while preserving behavior.

## Input Placeholder
- **Language/Stack**: [LANGUAGE] / [FRAMEWORK] / [RUNTIME_VERSION]
- **Context**: [CONTEXT_SUMMARY]
- **Constraints**: [CONSTRAINTS] (e.g., public API unchanged, no new dependencies)
- **Code**: [CODE_BLOCK]
- **Expected behavior**: [EXPECTED_BEHAVIOR]

## Expected Output Format
Return your answer in this exact structure:

1. **Assumptions**: Bullet list of assumptions you’re making.
2. **Refactoring plan**: Short plan (3–7 bullets) describing intended changes.
3. **Refactored code**: Provide the full updated code in a fenced code block labeled with [LANGUAGE].
4. **Key changes**: Bullet list mapping change → motivation (readability/maintainability).
5. **Validation**: How to confirm behavior is unchanged (tests to run, sample inputs/outputs, lint/typecheck commands).
