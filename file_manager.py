"""
File manager manages migrating files from the download
folder onto an SD card or some other storage.
"""
import os

LOCAL_DOWNLOAD_FOLDER = os.path.dirname(__file__) + "/downloads"
EXTERNAL_DOWNLOAD_FOLDER = "Directory to download folder on external storage"


class InvalidDirectoryError(Exception):
    pass


class ExternalStorageNotFound(Exception):
    pass


class FileManager:
    def __init__(self,
                 local_download_folder=LOCAL_DOWNLOAD_FOLDER,
                 external_download_folder=EXTERNAL_DOWNLOAD_FOLDER):
        self.raise_error_if_directory_does_not_exist(local_download_folder)

        self.local_download_folder = local_download_folder
        self.external_download_folder = external_download_folder

    @staticmethod
    def _directory_exists(directory):
        return os.path.isdir(directory)

    def raise_error_if_directory_does_not_exist(self, directory):
        if not self._directory_exists(directory):
            error_message = f"{directory} is not a valid directory."
            raise InvalidDirectoryError(error_message)

    def _get_local_file_path(self, file_name):
        return self.local_download_folder + '/' + file_name

    def external_file_path(self, file_name):
        return self.external_download_folder + '/' + file_name

    @staticmethod
    def _list_directory_files(directory):
        return os.listdir(directory)

    def list_local_download_files(self):
        return self._list_directory_files(self.local_download_folder)

    def move_file_to_external_storage(self, file_name):
        path = self._get_local_file_path(file_name)
        external_path = self.external_file_path(file_name)
        if self._directory_exists(self.external_download_folder):
            os.rename(path, external_path)
        else:
            error_message = f"{self.external_download_folder} not found. " \
                            f"Ensure your storage is mounted properly and " \
                            f"that the directory is valid."
            raise ExternalStorageNotFound(error_message)




# Function move files

# Function delete files

# Function move to external storage

def move_file_to_external_storage(file):
    os.rename(file, EXTERNAL_DOWNLOAD_FOLDER)

# Function delete from local storage
