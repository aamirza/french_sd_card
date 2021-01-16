"""
DownloadManager is a class that takes a Downloader objects, retains knowledge
of which files have already been downloaded, and which files are new and
should be downloaded.
"""

import functools
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

    def save_positions(func, *args, **kwargs):
        """Function wrapper for saving what was the last downloaded file
        from a URL."""
        @functools.wraps(func)
        def wrapper_save_positions(self, *args, **kwargs):
            value = func(self, *args, **kwargs)
            # Save positions to a pickler file
            with open(self.LAST_POSITIONS_FILE, 'wb') as positions_file:
                pickle.dump(self.download_positions, positions_file)
            return value

        return wrapper_save_positions

    @save_positions
    def download_all(self):
        """Download all new audio from all the services"""
        for service in self.services:
            start_at_position = self.get_position(service.url)
            position = service.download(start_at_position=start_at_position)
            self.update_position(service.url, position)

    def get_position(self, url):
        """Get last video downloaded (as position in playlist) from a
        specified URL"""
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
        except (FileNotFoundError, EOFError):
            positions = {}
        return positions

    def update_position(self, url, position):
        try:
            position = int(position)
        except ValueError:
            position = 1
        self.download_positions.update({url: position})
