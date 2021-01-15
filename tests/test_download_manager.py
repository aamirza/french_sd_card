import unittest
from unittest import mock

import download_manager
import youtube
from download_manager import DownloadManager
from youtube import YoutubeDownloader


class FileManagerTestCase(unittest.TestCase):
    def setUp(self):
        youtube = YoutubeDownloader()
        self.dm = DownloadManager(youtube)

    @mock.patch.object(youtube.YoutubeDownloader, 'download')
    def test_downloadPlaylist_downloadsToFolder(self, mock_download):
        self.dm.download_all()
        mock_download.assert_called()

    def test_downloadPlaylist_updatesLastVideoDownloaded(self):
        self.fail("Once a playlist is downloaded, the index of the last "
                  "video downloaded should be updated and stored "
                  "somewhere.")

    def test_downloadPlaylist_invalidDownloadFolder_raisesErrors(self):
        self.fail("If a download folder is invalid, an error needs"
                  "to be raised.")


if __name__ == '__main__':
    unittest.main()
