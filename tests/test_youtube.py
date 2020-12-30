import unittest
from unittest import mock

import youtube
import youtube_stub


class YoutubeTestCase(unittest.TestCase):
    def billboard2019_playlist(self):
        '''Sample playlist'''
        return "https://www.youtube.com/playlist?list=" \
               "PLCzImqCYRfNfJOzblgIkAPkG0HuMBtT5j"

    def test_validYoutubeLink_badLink_returnsFalse(self):
        youtube_link = "https://youcube.com"

        self.assertFalse(youtube.valid_link(youtube_link),
                         "Your function failed to catch an invalid link")

    def test_validYoutubeLink_goodLink_returnsTrue(self):
        youtube_link = self.billboard2019_playlist()

        self.assertTrue(youtube.valid_link(youtube_link),
                        "The YouTube link you entered is invalid.")

    @mock.patch.object(youtube.YoutubeDL, 'extract_info')
    def test_listPlaylistVideos_returnsList(self, mock_extract_info):
        playlist = self.billboard2019_playlist()

        mock_extract_info.return_value = youtube_stub.extract_info
        playlist_info = youtube.get_playlist_videos_info(playlist)

        mock_extract_info.assert_called_with(playlist, download=False)
        self.assertTrue(isinstance(playlist_info, list),
                        "Video list did not return a dict")

    @mock.patch.object(youtube.YoutubeDL, 'extract_info')
    def test_playlistVideos_returnsValidYoutubePages(self, mock_extract_info):
        playlist = self.billboard2019_playlist()

        mock_extract_info.return_value = youtube_stub.extract_info
        playlist_info = youtube.get_playlist_videos_info(playlist)

        self.assertTrue(youtube.valid_link(playlist_info[0]["webpage_url"]),
                        "Your playlist does not contain a video")





if __name__ == '__main__':
    unittest.main()
