"""
File manager manages migrating files from the download
folder onto an SD card or some other storage.
"""
import os

LOCAL_DOWNLOAD_FOLDER = "Directory to download folder on local storage"
EXTERNAL_DOWNLOAD_FOLDER = "Directory to download folder on external storage"

# Function move files

# Function delete files

# Function move to external storage

def move_file_to_external_storage(file):
    os.rename(file, EXTERNAL_DOWNLOAD_FOLDER)

# Function delete from local storage
