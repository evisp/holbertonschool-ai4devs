# Reflection on AI-Assisted Debugging

This project explored AI-assisted debugging by fixing five intentionally buggy programs across Python, JavaScript, Java, and C++. The process was structured and repeatable: identify the defect, implement a fix in a `_fixed` file, and validate behavior with simple tests (assertions, console logs, or small runtime checks). Alongside the code, I documented outcomes in a validation log and wrote short bug reports.

I treated each fix as a claim that must be proven:

>> “A change that compiles is not automatically a fix.”  
>> “A fix that passes one example can still be wrong.”

That mindset mattered because the easiest bugs were the ones with a single canonical correction, while the hardest ones required interpreting the developer’s intent.

**Easiest:** `bug1.py` (syntax errors) was the most mechanical; missing colons and an unclosed parenthesis are unambiguous. `bug4.cpp` (off-by-one) was similarly clear: `i <= 5` on a 5-element array is a boundary error that can trigger undefined behavior. `bug2.js` (logic inversion) was easy once the intended semantics were recognized: `isEven` should return true for even numbers, and the counter should increment when a match is found.

**Hardest:** `bug5.py` was difficult because it was underspecified. Calling `.split()` on a list is invalid, but the “correct” replacement depends on intent: split a CSV string into tokens, join a list into a CSV string, or normalize values to strings. `bug3.java` was technically simple (loop bound and null dereference), but it forced a design choice: what is correct behavior when a value is null—default, warn, or fail fast?

My trust in AI suggestions is high when the failure is deterministic and local (syntax, bounds, inverted conditions) and the patch is small enough to test quickly. Trust drops when the fix requires choosing between multiple valid behaviors or when a confident answer hides a requirements decision. A practical rule emerged:

>> Trust the AI’s first draft; trust the tests for the final verdict.

Human intuition mattered most in intent inference, policy decisions, and test selection. I had to choose which behavior to preserve in `bug5.py`, decide how to handle nulls in `bug3.java`, and pick edge cases (empty input, negatives, nulls) that reflect real usage.

In real-world debugging, AI is best as a rapid hypothesis generator and editor. It accelerates the “first useful guess,” especially across languages, but it does not replace specification and verification. Guardrails make it safe: add a test that fails before the fix and passes after, prefer explicit conversions and safe loop patterns, and treat ambiguity as a requirements question.

>> AI is the accelerator; tests are the steering wheel; human judgment decides the destination.
