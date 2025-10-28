# Static Code Analysis – Issue Documentation

| Issue Type | Tool | Line(s) | Description | Fix Implemented |
|-------------|-------|----------|--------------|----------------|
| Mutable default argument | Pylint | 10 | `logs=[]` creates shared state across calls | Changed default to `logs=None` and initialized inside function |
| Overly broad exception | Pylint | 26 | Used bare `except:` which hides all errors | Replaced with `except KeyError:` |
| Unsafe eval() usage | Bandit | 76 | `eval()` can execute arbitrary code | Removed `eval()` and replaced with safe `print()` |
| Input validation missing | Pylint / Bandit | 12 | Added numbers or invalid types to inventory | Added `isinstance()` checks for `item` and `qty` |
| Unsafe file handling | Bandit | 41, 47 | Opened files without `with` context | Used `with open(...) as f:` for safe file operations |
| Logging missing | Pylint | Various | Used print for runtime messages | Configured `logging` for consistent reporting |
| Potential KeyError | Pylint | 27 | Attempted to delete missing key | Handled with `except KeyError:` block |

✅ **Total Issues Fixed:** 6  
✅ **High/Medium Severity Issues Fixed:** 4+  
✅ **Tools Used:** `pylint`, `bandit`, `flake8`


# Reflection – Lab 5: Static Code Analysis

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

- **Easiest:** Removing `eval()` and replacing it with a safe print statement was straightforward once Bandit flagged it as a high-severity issue.  
- **Hardest:** Fixing the mutable default argument (`logs=[]`) required understanding how Python stores default arguments and rethinking the function structure.

---

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes. Bandit flagged the `open()` calls even after using a context manager (`with open(...)`). This was a false positive since the files are safely closed in the updated implementation.

---

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate **Pylint**, **Bandit**, and **Flake8** in a **GitHub Actions CI pipeline** and also configure **pre-commit hooks**.  
This ensures every code push or commit automatically runs static analysis, preventing issues from being merged into the main branch.

---

## 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?

After applying the fixes:
- The code became **safer** (no `eval`, proper file handling, specific exception handling).  
- **Logging** improved visibility into operations and errors.  
- Input validation reduced runtime crashes.  
- The program is now **PEP8-compliant** and easier to maintain or extend.

---

**Summary:**  
Static analysis tools are essential for maintaining secure, clean, and reliable Python code.  
This lab demonstrated how easily overlooked issues can be caught early through automated analysis.
