# Style Enforcement Prompt Template

**Role**: Experienced Software Engineer / Code Reviewer

**Task**: Rewrite the given code to enforce consistent naming, formatting, and coding conventions according to the specified style guide.

**Input Placeholder**: [CODE_BLOCK]

**Prompt Template**:
You are an experienced software engineer.

Review and rewrite the following [LANGUAGE] code so it follows a consistent coding style.

Apply the requested conventions for:
- naming
- formatting
- indentation
- comments
- file or framework-specific style rules

Code:
[CODE_BLOCK]

Additional context:
- Language: [LANGUAGE]
- Style guide: [STYLE_GUIDE]
- Naming convention: [NAMING_CONVENTION]
- Formatting preferences: [FORMATTING_RULES]
- Project context: [PROJECT_CONTEXT]
- Constraints: [CONSTRAINTS]

Return:
- the rewritten code with consistent style
- a brief summary of the style improvements applied

**Expected Output**: Reformatted and renamed code that follows the requested style conventions, plus a short explanation of the updates.
