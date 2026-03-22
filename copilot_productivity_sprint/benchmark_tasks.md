## Task 1 - User Registration Validator

**Estimated Time**: 15–20 minutes

**Requirements**:  
Implement a Python function `validate_user(data)` that checks whether a user registration payload is valid.

**Inputs**:  
A Python dictionary with:
- `name` (string)
- `email` (string)
- `age` (integer)

Example:
```python
{
  "name": "Alice",
  "email": "alice@example.com",
  "age": 22
}
```

**Outputs**:  
A dictionary with:
- `valid` (boolean)
- `errors` (list of strings)

Example:
```python
{
  "valid": True,
  "errors": []
}
```

**Acceptance Criteria**:
- `name` must not be empty
- `email` must contain `@`
- `age` must be an integer greater than or equal to 18
- Returns `valid: True` and an empty error list when input is correct
- Returns `valid: False` and one or more error messages when input is invalid


## Task 2 - Notes CRUD Endpoint

**Estimated Time**: 20–30 minutes

**Requirements**:  
Implement a small API endpoint to create notes using Python and a lightweight web framework such as Flask or FastAPI.

**Inputs**:  
HTTP `POST /notes` with JSON body:
```json
{
  "title": "Buy milk",
  "content": "Remember to buy milk after work"
}
```

**Outputs**:  
On success, return a created note object with an ID.

Example:
```json
{
  "id": 1,
  "title": "Buy milk",
  "content": "Remember to buy milk after work"
}
```

**Acceptance Criteria**:
- Returns HTTP `201` on success
- Returns JSON with `id`, `title`, and `content`
- `title` is required
- Returns HTTP `400` if `title` is missing or empty
- Data can be stored in memory; no database is required


## Task 3 - To-Do List Filter

**Estimated Time**: 15–25 minutes

**Requirements**:  
Implement a small JavaScript function that filters a list of to-do items by status.

**Inputs**:  
An array of objects:
```javascript
[
  { id: 1, title: "Write tests", done: true },
  { id: 2, title: "Fix bug", done: false },
  { id: 3, title: "Update docs", done: false }
]
```

And a filter value:
- `"done"`
- `"pending"`

**Outputs**:  
A filtered array of matching items.

Example:
```javascript
[
  { id: 2, title: "Fix bug", done: false },
  { id: 3, title: "Update docs", done: false }
]
```

**Acceptance Criteria**:
- `"done"` returns only completed tasks
- `"pending"` returns only incomplete tasks
- Returns an empty array if no items match
- Function does not modify the original array

