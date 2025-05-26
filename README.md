# Password Strength Checker (Python)

A simple Python CLI tool to determine the strength of a user-entered password using pattern checks and a blacklist of common weak passwords.

## Features

- Validates:
  - Minimum length
  - Uppercase/lowercase letters
  - Numbers
  - Special characters
  - Common password blacklist
- Scored out of 5
- Instant feedback
- Secure password generator
  - User-defined length (min 8)
  - Uses uppercase, lowercase, numbers, and special characters


## Lessons Learned

- Regex for input validation
- Secure design principles in password creation
- Python CLI and control flow

## How to Run

```bash
python3 password_checker.py

- Choose 1 to check password strength
- Choose 2 to generate a secure password