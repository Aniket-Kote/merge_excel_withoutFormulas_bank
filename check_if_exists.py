import os

from pathlib import Path

def delete_file(file_path):
    try:
        path = Path(file_path)
        path.unlink()
        print(f"{file_path} has been deleted successfully.")
    except OSError as e:
        print(f"Error occurred while deleting {file_path}: {e}")



def check_file_exists(file_path):
    if os.path.exists(file_path):
        delete_file(file_path)
    else:
        print("File does not exist.")
    

