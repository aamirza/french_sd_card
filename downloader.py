import os
from abc import ABC, abstractmethod

DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'


class Downloader(ABC):
    def __init__(self, download_folder=None):
        if download_folder:
            self.download_folder = download_folder
        else:
            self.download_folder = DOWNLOAD_FOLDER

    @abstractmethod
    def download(self, url: str, start_at_position: int = 1) -> int:
        """Download the video and return what position you downloaded up to."""
        pass

    @abstractmethod
    def get_info(self, url: str):
        """Get information on what is to be downloaded, such as links,
        number of files etc."""
        pass
