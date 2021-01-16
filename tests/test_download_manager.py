import unittest
from unittest import mock

import download_manager
import youtube
from download_manager import DownloadManager
from youtube import YoutubeDownloader


class FileManagerTestCase(unittest.TestCase):
    def setUp(self):
        youtube = YoutubeDownloader(self.billboard2019_playlist())
        self.dm = DownloadManager(youtube)

    def billboard2019_playlist(self):
        '''Sample playlist'''
        return "https://www.youtube.com/playlist?list=" \
               "PLCzImqCYRfNfJOzblgIkAPkG0HuMBtT5j"

    @mock.patch.object(youtube.YoutubeDownloader, 'download')
    def test_downloadPlaylist_downloadsToFolder(self, mock_download):
        self.dm.download_all()

        mock_download.assert_called()

    @mock.patch.object(youtube.YoutubeDownloader, 'download')
    @mock.patch('download_manager.pickle')
    def test_downloadPlaylist_updatesLastVideoDownloaded(self, mock_pickler,
                                                         mock_download):
        self.dm.download_all()

        mock_pickler.assert_called()

    @mock.patch.object(download_manager.pickle, 'load')
    def test_getPositions_returnsPickleFilePositions(self, mock_pickler):
        expected_return_value = {self.billboard2019_playlist(): "1"}
        mock_pickler.return_value = expected_return_value

        with mock.patch('builtins.open'):
            positions = self.dm.get_positions()

        self.assertEqual(expected_return_value, positions)


    def test_downloadPlaylist_invalidDownloadFolder_raisesErrors(self):
        self.fail("If a download folder is invalid, an error needs"
                  "to be raised.")


if __name__ == '__main__':
    unittest.main()
