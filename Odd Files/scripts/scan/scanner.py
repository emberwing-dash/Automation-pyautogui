import pygame
from pathlib import Path

# Class to handle file checking logic
class FileChecker:
    def __init__(self, folder_path, files_to_check):
        self.folder_path = Path(folder_path)
        self.files_to_check = files_to_check

    def check_files_deleted(self):
        """Check if all files in the folder are deleted."""
        for file_name in self.files_to_check:
            file_path = self.folder_path / file_name
            if file_path.exists():  # If the file exists, it's not deleted
                return False
        return True  # All files are deleted




# Path to the fileDel folder (relative to your current working directory)
folder_path = 'filesDel'
files_to_check = ['file1.txt', 'file2.txt', 'file3.txt']

# Create an instance of the FileChecker class
file_checker = FileChecker(folder_path, files_to_check)

# Check if the player has won (all files are deleted)
if file_checker.check_files_deleted():
    player_wins = True

