# Benchmark Tasks – Copilot Productivity Sprint

## Task 1: Data Processing Script (Python)
**Requirements**: Create a script that reads a JSON file containing a list of products, filters out items with a price lower than $10, and calculates the total stock value for the remaining items.
- **Inputs**: JSON file with fields `id`, `name`, `price`, and `quantity`.
- **Outputs**: A summary object `{ "filtered_count": int, "total_value": float }`.
- **Acceptance Criteria**:
  - Script must handle missing "price" or "quantity" fields without crashing.
  - Calculation must be accurate to two decimal places.

## Task 2: Express.js Authentication Middleware (JavaScript)
**Requirements**: Implement a JWT authentication middleware for an Express.js application.
- **Inputs**: HTTP Request with `Authorization: Bearer <token>` header.
- **Outputs**: `req.user` object populated if valid, or a 401/403 error response.
- **Acceptance Criteria**:
  - Returns 401 if the header is missing.
  - Returns 403 if the token is expired or invalid.
  - Successfully calls `next()` if the token is valid.

## Task 3: Unit Testing for String Utility (Any Language)
**Requirements**: Write a comprehensive set of unit tests for a function `slugify(text)` which converts strings to URL-friendly slugs (e.g., "Hello World!" -> "hello-world").
- **Inputs**: A suite of test cases (empty string, special characters, multiple spaces).
- **Outputs**: Test results (pass/fail).
- **Acceptance Criteria**:
  - Tests must cover edge cases like non-ASCII characters.
  - Tests must verify that all output is lowercase and separated by hyphens.
