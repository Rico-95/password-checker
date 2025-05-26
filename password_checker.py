import re

# Common weak passwords
common_passwords = [
    "password", "123456", "123456789", "qwerty", "letmein", "football",
    "admin", "welcome", "monkey", "abc123", "iloveyou", "123123"
]

def check_password_strength(password):
    score = 0
    print("\n[+] Evaluating password strength...")

    if len(password) >= 8:
        score += 1
    else:
        print("[!] Password is too short (<8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("[!] No uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("[!] No lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        print("[!] No numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("[!] No special characters")

    if password.lower() in common_passwords:
        print("[!] Password is in a common password list")
        score = 0

    print(f"\nPassword Score: {score}/5")
    if score < 3:
        print("⚠️ Weak password")
    elif score == 3 or score == 4:
        print("✅ Medium strength password")
    else:
        print("🛡️ Strong password")

if __name__ == "__main__":
    user_input = input("Enter a password to check: ")
    check_password_strength(user_input)
