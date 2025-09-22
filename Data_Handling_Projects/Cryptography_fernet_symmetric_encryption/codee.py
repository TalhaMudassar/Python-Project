"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

# ------------------ KEY HANDLING ------------------
def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
    else:
        with open(KEY_FILE, "rb") as file:
            key = file.read()
    return Fernet(key)

fernet = load_or_create_key()

# ------------------ VAULT HANDLING ------------------
def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_vault(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

# ------------------ CORE FEATURES ------------------
def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": title,
        "encrypted_content": encrypted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("✅ Note saved successfully.")

def list_notes():
    data = load_vault()
    if not data:
        print("No notes yet.")
        return

    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} {note['timestamp']}")

def view_note():
    data = load_vault()
    if not data:
        print("No notes yet.")
        return

    list_notes()
    try:
        index = int(input("Enter note number to view: ")) - 1
        if 0 <= index < len(data):
            encrypted = data[index]["encrypted_content"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"\n 📝 {data[index]['title']} - {data[index]['timestamp']}\n\n{decrypted}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

def search_notes():
    keyword = input("Enter a keyword to search: ").strip().lower()
    data = load_vault()
    found = [note for note in data if keyword in note["title"].lower()]
    if not found:
        print("No matching notes found.")
    else:
        for note in found:
            print(f"{note['title']} {note['timestamp']}")

# ------------------ MAIN MENU ------------------
def main():
    while True:
        print("\n🔐 Offline Notes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Enter an option: ").strip()

        match choice:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_note()
            case "4": search_notes()
            case "5": break
            case _: print("Invalid input, try again.")

if __name__ == "__main__":
    main()
