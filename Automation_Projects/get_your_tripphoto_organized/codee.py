"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (not implemented yet, but structure allows it)

Teaches:
- File iteration
- String formatting
- Renaming files using os.rename
- User input handling
"""

import os

def batch_rename(folder, base_name, extension):
    """
    Batch rename all files in the given folder that match the provided extension.
    The new names follow the pattern: base_name_1.extension, base_name_2.extension, ...
    """

    # Collect all files that end with the given extension (case-insensitive)
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]

    # Sort files alphabetically (optional, helps in predictable order)
    files.sort()

    #  If no matching files are found, stop the function
    if not files:
        print("No files found with the given extension in the folder.")
        return

    #  Preview the renaming changes before applying
    print("\nPreview of changes:")
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file}  =>  {new_name}")

    #  Ask the user for confirmation before renaming
    confirm = input("\nPress (y) to confirm or (n) to cancel: ").strip().lower()

    if confirm != 'y':
        print(" Renaming cancelled.")
        return

    #  Perform the actual renaming
    for i, file in enumerate(files, start=1):
        src = os.path.join(folder, file)  # Original file path
        new_name = f"{base_name}_{i}{extension}"
        dest = os.path.join(folder, new_name)  # New file path
        os.rename(src, dest)  # Rename file

    print(f"\n Renamed {len(files)} files successfully.")

if __name__ == "__main__":
    """
    Entry point of the program.
    Ask the user for folder path, base name, and file extension.
    Then call the batch_rename() function.
    """

    # Ask user for folder path or use current directory if left blank
    folder = input("Enter folder path or leave blank for current folder: ").strip() or os.getcwd()

    # Validate folder path
    if not os.path.isdir(folder):
        print(" Invalid folder path.")
    else:
        # Get base name (e.g., 'image')
        base_name = input("Enter base name for files: ").strip()

        # Get extension (e.g., '.jpg')
        extension = input("Enter file extension (e.g., .jpg): ").strip()

        # Run the batch rename process
        batch_rename(folder, base_name, extension)
