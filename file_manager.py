"""
File manager manages migrating files from the download
folder onto an SD card or some other storage.
"""
import os

LOCAL_DOWNLOAD_FOLDER = os.path.dirname(__file__) + "/downloads"
EXTERNAL_DOWNLOAD_FOLDER = "Directory to download folder on external storage"


class InvalidDirectoryError(Exception):
    pass


class FileManager:
    def __init__(self,
                 local_download_folder=LOCAL_DOWNLOAD_FOLDER,
                 external_download_folder=EXTERNAL_DOWNLOAD_FOLDER):
        self.raise_error_if_directory_does_not_exist(local_download_folder)

        self.local_download_folder = local_download_folder
        self.external_download_folder = external_download_folder

    @staticmethod
    def raise_error_if_directory_does_not_exist(directory):
        if not os.path.isdir(directory):
            error_message = f"{directory} is not a valid directory."
            raise InvalidDirectoryError(error_message)

    def _get_local_file_path(self, file_name):
        return self.local_download_folder + '/' + file_name

    def external_file_path(self, file_name):
        return self.external_download_folder + '/' + file_name

    def move_file_to_external_storage(self, file_name):
        path = self._get_local_file_path(file_name)
        external_path = self.external_file_path(file_name)
        os.rename(path, external_path)




# Function move files

# Function delete files

# Function move to external storage

def move_file_to_external_storage(file):
    os.rename(file, EXTERNAL_DOWNLOAD_FOLDER)

# Function delete from local storage
