1. Which issues were the easiest to fix, and which were the hardest? Why?
Easiest: Removing the eval() function. It was a single line that needed to be deleted to eliminate a high-severity security vulnerability. Using f-strings also provided an easy readability fix.

Hardest: The mutable default argument (logs=[]). This fix requires specific knowledge of how Python evaluates function arguments once at definition, necessitating a change to logs=None and conditional initialization inside the function.

2. Did the static analysis tools report any false positives? If so, describe one example.
Yes, the tools reported an unused import warning (W0611/F401) for the logging module. This is often considered a false positive or minor cleanup because the module was likely imported with the intention of being used later, but it does not represent a functional bug in the existing code.

3. How would you integrate static analysis tools into your actual software development workflow?
Integrate Flake8 for fast style checks into the local development workflow using a pre-commit hook.

Integrate Pylint and Bandit into the Continuous Integration (CI) pipeline. The CI job would be configured to fail if security vulnerabilities (Bandit) or critical bugs (Pylint) are found, enforcing strict quality gates on all code merged.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
Robustness: Significantly improved by replacing the broad except: with except KeyError: and using with open(...) for safer resource management, preventing masked errors and file leaks.

Security: Achieved by immediately removing the dangerous eval() call, eliminating a high-severity vulnerability.

Readability: Improved by using modern f-strings for logging and output, making the code cleaner and easier to maintain.