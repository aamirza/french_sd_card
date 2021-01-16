"""
DownloadManager is a class that takes a Downloader objects, retains knowledge
of which files have already been downloaded, and which files are new and
should be downloaded.
"""
import os
import pickle


class DownloadManager:
    LAST_POSITIONS_FILE = os.path.dirname(__file__) + "/positions.pk1"
    def __init__(self, *downloaders):
        """
        :param downloaders: Object of type Downloader
        """
        self.services = [downloader for downloader in downloaders]
        # Download positions stores the last file downloaded in each playlist
        self.download_positions = self.load_positions()

    def download_all(self):
        """Download all new audio from all the services"""
        for service in self.services:
            start_at_position = self.get_position(service.url)
            service.download(start_at_position=start_at_position)

    def get_position(self, url):
        try:
            position = self.download_positions[url]
        except KeyError:
            position = 1
        return position

    def load_positions(self):
        """Get last download positions for each URL"""
        try:
            with open(self.LAST_POSITIONS_FILE, 'rb') as positions_file:
                positions = pickle.load(positions_file)
        except FileNotFoundError:
            positions = {}
        return positions

# Downloader class
    # Init
        # An iteration of Downloader objects

    # Download All
        # For service in downloader:
            # Download files starting at a position
            # Save 'position' of the last file downloaded Save_position()

    # Save position
        # Saves last file downloaded, to know where to start from afterwards

    