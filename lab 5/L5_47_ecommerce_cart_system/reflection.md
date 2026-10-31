
# Lab 5 – Reflection

## 1. What is the importance of static code analysis?

Static code analysis helps identify potential bugs, security vulnerabilities, and coding standard violations without executing the program. It improves software quality by detecting problems early in development and making the code easier to maintain.

## 2. What did you learn from Pylint, Bandit, and Flake8?

Pylint helped identify code quality issues such as unused variables, missing documentation, mutable default arguments, and naming convention violations.

Bandit helped identify security vulnerabilities such as the use of eval(), weak MD5 hashing, insecure random number generation, and shell command execution.

Flake8 helped identify formatting and style violations, including unused imports, bare exception handling, incorrect comparisons with None, and excessively long lines.

## 3. What was the most important issue identified during the lab?

The use of eval() and insecure hashing were among the most important issues because they could affect the security of the application. The use of os.system() also introduced a potential command injection vulnerability.

These issues were corrected by replacing unsafe operations with safer Python alternatives.

## 4. How did static analysis improve the overall quality of the program?

Static analysis improved the program's readability, security, and maintainability. Unused variables and imports were removed, functions were renamed using snake_case, documentation was added, and file handling was improved.

After making the corrections, the Pylint score increased from 3.86/10 to 10.00/10. Bandit reported zero issues, and Flake8 reported no formatting violations.

## Conclusion

This lab demonstrated how static analysis tools can improve software quality without executing the source code. Using Pylint, Bandit, and Flake8 together provided a comprehensive approach to identifying and correcting code quality, security, and formatting issues.
