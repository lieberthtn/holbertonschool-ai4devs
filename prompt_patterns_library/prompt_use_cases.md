# Prompt Use Cases

## 1. Code Quality & Refactoring
- **Code Optimization**
    - **Goal**: Improve execution speed and reduce complexity.
    - **Input**: Source code in [LANGUAGE].
    - **Output**: Optimized code with a brief performance explanation.
- **Legacy Code Modernization**
    - **Goal**: Update old syntax to modern standards (e.g., Python 2 to 3, ES5 to ES6).
    - **Input**: Deprecated code snippet.
    - **Output**: Modernized code using current best practices.
- **Naming Conventions Enforcement**
    - **Goal**: Ensure variables and functions follow a specific naming style (e.g., camelCase, snake_case).
    - **Input**: Code block with inconsistent naming.
    - **Output**: Refactored code with consistent naming.

## 2. Debugging & Error Handling
- **Stack Trace Analysis**
    - **Goal**: Identify the root cause of a crash based on logs.
    - **Input**: Error log and relevant source file.
    - **Output**: Explanation of the bug and a suggested fix.
- **Security Vulnerability Detection**
    - **Goal**: Find common security flaws like SQL Injection or XSS.
    - **Input**: Web application backend code.
    - **Output**: List of vulnerabilities and remediation steps.
- **Logical Bug Identification**
    - **Goal**: Find why a function returns the wrong value despite no syntax errors.
    - **Input**: Function code and expected vs. actual output.
    - **Output**: Explanation of the logical flaw.

## 3. Testing & Validation
- **Unit Test Generation**
    - **Goal**: Automatically create tests for a given function.
    - **Input**: Source function in [LANGUAGE].
    - **Output**: Test suite using [TEST_FRAMEWORK].
- **Edge Case Identification**
    - **Goal**: Discover input values that might break the code.
    - **Input**: Function description or code.
    - **Output**: List of boundary conditions to test.

## 4. Documentation & Maintenance
- **API Documentation Generation**
    - **Goal**: Create clear documentation for public methods.
    - **Input**: Source code of classes and methods.
    - **Output**: Documentation in Markdown or JSDoc/Doxygen format.
- **Commit Message Generation**
    - **Goal**: Write standard-compliant commit messages (e.g., Conventional Commits).
    - **Input**: Git diff output.
    - **Output**: A structured commit message summary.
- **Code Comments Addition**
    - **Goal**: Explain complex logic within the code for better maintainability.
    - **Input**: Dense or complex code block.
    - **Output**: Annotated code with inline comments.
