"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move
- Ignore a specific file: "day_01.py"

Teaches:
- File system operations
- Automation
- File handling with `os` and `shutil`
"""

import os       # For interacting with the file system
import shutil   # For moving files between folders

# ✅ Dictionary that maps folder names to file extensions
EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".png", ".jpg", ".jpeg"],
    "TextFiles": [".txt"]
}

def get_destination_folder(filename):
    """
    Determine which folder the file should go into
    based on its extension.
    """
    # Extract the file extension and convert it to lowercase
    ext = os.path.splitext(filename)[1].lower()

    # Match the extension with the appropriate folder
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder

    # If no match found, send the file to "Others" folder
    return "Others"

def sort_files(folder_path):
    """
    Sort all files in the given folder into subfolders
    based on their file type.
    """
    # Loop through all items in the folder
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        # ✅ Skip directories (we only want to move files)
        if not os.path.isfile(full_path):
            continue

        # ✅ Skip a specific file (e.g., the main script itself)
        if file == "day1.py":
            print(f"Skipping file: {file}")
            continue

        # ✅ Determine the destination folder for the file
        dest_folder = get_destination_folder(file)
        dest_path = os.path.join(folder_path, dest_folder)

        # ✅ Create the destination folder if it doesn't exist
        os.makedirs(dest_path, exist_ok=True)

        # ✅ Move the file to the destination folder
        shutil.move(full_path, os.path.join(dest_path, file))
        print(f"Moved: {file} -> {dest_folder}/")

if __name__ == "__main__":
    """
    Entry point of the program.
    Ask the user for a folder path.
    If left blank, use the current working directory.
    """
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()  # Use current directory if blank

    # ✅ Check if the given folder is valid
    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        # ✅ Call the sorting function
        sort_files(folder)
        print("✅ Sorting completed")
