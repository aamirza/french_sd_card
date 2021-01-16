import unittest
from unittest import mock

import download_manager
import youtube
from download_manager import DownloadManager
from youtube import YoutubeDownloader


class FileManagerTestCase(unittest.TestCase):
    def setUp(self):
        youtube = YoutubeDownloader(url=self.billboard2019_playlist())
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
    @mock.patch.object(download_manager.pickle, 'dump')
    def test_downloadAll_updatesLastFileDownloaded(self,
                                                   mock_pickler,
                                                   mock_download):
        self.dm.download_all()

        mock_pickler.assert_called()

    @mock.patch.object(youtube.YoutubeDownloader, 'download')
    def test_downloadAll_startsAtLastPositionDownloaded(self,
                                                        mock_youtube_dl):
        # Start at position 5
        self.dm.download_positions = {self.billboard2019_playlist(): 5}
        self.dm.download_all()
        mock_youtube_dl.assert_called_once_with(start_at_position=5)

    @mock.patch.object(download_manager.pickle, 'load')
    def test_getPositions_returnsPickleFilePositions(self, mock_pickler):
        expected_return_value = {self.billboard2019_playlist(): "1"}
        mock_pickler.return_value = expected_return_value

        with mock.patch('builtins.open'):
            positions = self.dm.load_positions()

        self.assertEqual(expected_return_value, positions)


    def test_downloadPlaylist_invalidDownloadFolder_raisesErrors(self):
        self.fail("If a download folder is invalid, an error needs"
                  "to be raised.")


if __name__ == '__main__':
    unittest.main()
