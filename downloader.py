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
    def download(self, url, start_at_position=1):
        """Download the video and return what position you downloaded up to."""
        pass

    @abstractmethod
    def get_info(self, url):
        """Get information on what is to be downloaded, such as links,
        number of files etc."""
        pass
