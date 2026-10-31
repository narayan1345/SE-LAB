
# Static Code Analysis – Issues and Fixes

## Project
E-commerce Cart System

## Tools Used
- Pylint
- Bandit
- Flake8

## 1. Issues Identified and Fixed

| No. | Issue | Tool | Severity | Fix Applied |
|---|---|---|---|---|
| 1 | Mutable default argument (`audit_log=[]`) | Pylint | Warning | Replaced with `None` and initialized inside the function. |
| 2 | Use of global statement | Pylint | Warning | Replaced global numeric variable with a dictionary-based sales data structure. |
| 3 | Bare except clause | Pylint, Bandit, Flake8 | Low | Specified `KeyError` explicitly. |
| 4 | Use of `eval()` | Pylint, Bandit | Medium | Replaced dynamic evaluation with direct arithmetic calculation. |
| 5 | Weak MD5 hashing | Bandit | High | Replaced MD5 with SHA-256. |
| 6 | Insecure random number generation | Bandit | Low | Replaced `random.randint()` with `secrets.randbelow()`. |
| 7 | Shell command execution | Bandit | High | Removed `os.system()` and used Python's print function. |
| 8 | Hardcoded gateway secret | Security review | Security concern | Removed the hardcoded demonstration secret. |
| 9 | Missing module and function docstrings | Pylint | Convention | Added descriptive docstrings. |
| 10 | Incorrect function naming | Pylint | Convention | Converted function names to snake_case. |
| 11 | Unused imports and variables | Pylint, Flake8 | Warning | Removed unnecessary imports and variables. |
| 12 | Incorrect None comparison | Pylint, Flake8 | Convention | Used `is not None`. |
| 13 | Unspecified file encoding | Pylint | Warning | Specified UTF-8 encoding. |
| 14 | Improper file handling | Pylint | Refactor | Used a with statement for file operations. |
| 15 | Line exceeding 79 characters | Flake8 | Style | Split long lines into multiple lines. |
| 16 | Missing final newline | Pylint, Flake8 | Style | Added a newline at the end of the file. |
| 17 | Unnecessary conditional statements | Pylint | Refactor | Simplified Boolean return logic. |
| 18 | Old-style string formatting | Pylint | Convention | Replaced with f-strings. |

## 2. Analysis Results

### Pylint
- Before: 3.86/10
- After: 10.00/10
- Result: All reported Pylint issues resolved.

### Bandit
- Before: 5 security issues.
- After: 0 security issues.
- Result: All reported Bandit findings resolved.

### Flake8
- Before: 7 issues.
- After: 0 issues.
- Result: All reported Flake8 findings resolved.

## 3. Conclusion

Static code analysis helped identify programming errors, security vulnerabilities, and coding standard violations in the E-commerce Cart System.

The identified issues were corrected using Pylint, Bandit, and Flake8. The final program achieved a Pylint score of 10.00/10 and reported zero issues in Bandit and Flake8.

These improvements increased the code's readability, security, maintainability, and overall quality.
