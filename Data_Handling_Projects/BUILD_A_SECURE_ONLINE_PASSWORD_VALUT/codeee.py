"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""
import base64
import os

VAULT_FILE = 'vault.txt'
DELIM = " || "   # keep same visual delimiter you were using

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength_checker(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)
    score = sum([length >= 8, has_upper, has_digit, has_special])
    return ["weak", "medium", "strong", "very-strong"][min(score, 3)]

def add_crediential():
    username = input("Enter username : ").strip()
    website = input("Enter your website : ").strip()
    password = input("Enter password: ").strip()
    if not (username and website and password):
        print("All fields are required.")
        return

    strength = password_strength_checker(password)
    print("Password strength:", strength)

    line = f"{website}{DELIM}{username}{DELIM}{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as file:
        file.write(encoded_line + '\n')

    print("Saved Credential")

def view_crediential():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return

    with open(VAULT_FILE, 'r', encoding='utf-8') as file:
        for raw in file:
            raw = raw.strip()
            if not raw:
                continue
            try:
                decoded = decode(raw)
                website, username, password = decoded.split(DELIM)
            except Exception:
                # skip malformed lines
                continue
            hidden_password = '*' * len(password)
            print(f"{website} | {username} | {hidden_password}")

def update_password():
    if not os.path.exists(VAULT_FILE):
        print("File Not Exists")
        return

    website_in = input("Enter website: ").strip()
    username_in = input("Enter username: ").strip()
    old_password = input("Enter old password: ").strip()
    new_password = input("Enter new password: ").strip()

    if not (website_in and username_in and old_password and new_password):
        print("All fields are required.")
        return

    changed = False
    new_lines = []

    with open(VAULT_FILE, 'r', encoding='utf-8') as file:
        for raw in file:
            raw = raw.strip()
            if not raw:
                continue
            try:
                decoded = decode(raw)
                website, username, password = decoded.split(DELIM)
            except Exception:
                # keep malformed line unchanged
                new_lines.append(raw)
                continue

            if website == website_in and username == username_in:
                if password == old_password:
                    # replace password
                    updated_line = f"{website}{DELIM}{username}{DELIM}{new_password}"
                    new_lines.append(encode(updated_line))
                    changed = True
                else:
                    print("Old password did not match for this entry.")
                    # keep original encoded line
                    new_lines.append(raw)
            else:
                # keep original entry
                new_lines.append(raw)

    if changed:
        # overwrite file with updated content
        with open(VAULT_FILE, 'w', encoding='utf-8') as file:
            for line in new_lines:
                file.write(line + '\n')
        strength = password_strength_checker(new_password)
        print("Credential updated. New password strength:", strength)
    else:
        if any(website_in == decode(l).split(DELIM)[0] and username_in == decode(l).split(DELIM)[1] for l in new_lines if l):
            # found entry but old password mismatch already reported above
            pass
        else:
            print("No matching credential found for given website and username.")

def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_crediential()
            case "2":
                view_crediential()
            case "3":
                update_password()
            case "4":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
