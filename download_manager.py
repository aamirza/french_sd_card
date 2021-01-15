"""
DownloadManager is a class that takes a Downloader objects, retains knowledge
of which files have already been downloaded, and which files are new and
should be downloaded.
"""


class DownloadManager:
    def __init__(self, *downloaders):
        """
        :param downloaders: Object of type Downloader
        """
        self.services = [downloader for downloader in downloaders]

    def download_all(self):
        '''Download all new audio from all the services'''
        for service in self.services:
            service.download()

# Downloader class
    # Init
        # An iteration of Downloader objects

    # Download All
        # For service in downloader:
            # Download files starting at a position
            # Save 'position' of the last file downloaded Save_position()

    # Save position
        # Saves last file downloaded, to know where to start from afterwards

    