"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""

import os
import shutil
from watchdog.events import FileSystemEventHandler  # To handle filesystem events (e.g., file created)
from watchdog.observers import Observer             # To observe file system changes in real time

# Folder to watch for new files (default: Downloads folder)
WATCH_FOLDER = os.path.expanduser("~/Downloads")

# Mapping of file extensions to destination folders
FILE_DESTS = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
    '.zip': 'Archives'
}

# Event handler class that reacts to file system changes
class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        """
        This method runs automatically when a new file or folder is created.
        We check if it's a file, then move it to the appropriate subfolder.
        """
        # Ignore directories; we only care about files
        if event.is_directory:
            return

        # Get the full path of the newly created file
        filepath = event.src_path

        # Extract file extension and convert to lowercase for consistency
        ext = os.path.splitext(filepath)[1].lower()

        # Decide which folder the file should go to based on its extension
        dest_folder = FILE_DESTS.get(ext, 'Others')

        # Create the destination folder path
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)

        # Create the destination folder if it does not exist
        os.makedirs(full_dest, exist_ok=True)

        # Create the full path where the file will be moved
        move_to = os.path.join(full_dest, os.path.basename(filepath))

        # Try to move the file to the destination folder
        try:
            shutil.move(filepath, move_to)
            print(f"Moved: {os.path.basename(filepath)} -> {dest_folder}/")
        except Exception as e:
            print(f"Failed to move {filepath}: {e}")

if __name__ == "__main__":
    # Print the folder being watched
    print(f"Watching folder: {WATCH_FOLDER}")

    # Create an event handler object from our custom class
    event_handler = FileMoverHandler()

    # Create an Observer that will monitor the file system for changes
    observer = Observer()

    # Schedule the observer to watch the chosen folder (non-recursive)
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)

    # Start watching the folder
    observer.start()

    try:
        # Keep the script running indefinitely to continuously monitor the folder
        while True:
            pass
    except KeyboardInterrupt:
        # Stop observing when user presses Ctrl+C
        observer.stop()

    # Wait until the observer thread has fully stopped before exiting
    observer.join()
