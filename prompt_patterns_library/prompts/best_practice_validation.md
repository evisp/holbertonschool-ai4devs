# Best Practice Validation Prompt Template

**Role**: Experienced Software Engineer / Code Reviewer

**Task**: Analyze the given code and evaluate whether it follows established best practices for the specified language, framework, and project context.

**Input Placeholder**: [CODE_BLOCK]

**Prompt Template**:
You are an experienced software engineer.

Review the following [LANGUAGE] code and assess whether it follows best practices for:
- code structure
- readability
- maintainability
- error handling
- security
- performance
- framework or language conventions

Code:
[CODE_BLOCK]

Additional context:
- Language: [LANGUAGE]
- Framework or library: [FRAMEWORK]
- Project context: [PROJECT_CONTEXT]
- Coding standards: [STYLE_GUIDE]
- Constraints: [CONSTRAINTS]
- Focus areas: [FOCUS_AREAS]

Return:
- a list of best practice issues found
- an explanation of why each issue matters
- specific recommendations for improvement
- an improved version of the code if appropriate

**Expected Output**: A structured review identifying best practice violations, explaining their impact, and suggesting concrete improvements.
