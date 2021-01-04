import unittest
from unittest import mock

import youtube
from youtube import YoutubeDownloader
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

    # Download playlist starting at certain video index. Store last video
    # downloaded.

    @mock.patch.object(youtube.YoutubeDL, 'download')
    def test_downloadPlaylist_downloadsEntirePlaylist(self, mock_yt_download):
        # Needs a file download location.
        # Link needs to be validated before connecting.
        self.fail("Test to download an entire playlist")

    def test_downloadPlaylist_invalidPlaylist_raisesError(self):
        playlist_url = "https://www.youtube.com/plalist" \
                       "?list=PLo7NRy1FWJw-NbaoWLw8PrLkQZv0w5e9y"
        with self.assertRaisesRegex(youtube.InvalidPlaylistError,
                                    "Playlist URL is invalid"):
            youtube.download_playlist(playlist_url)

    def test_downloadPlaylist_startAtInvalidNumber_raisesWarning(self):
        self.fail("If no videos are download because 'start at' is a "
                  "number higher than the number of playlists in a video,"
                  "this should display some kind of warning or error.")

    def test_downloadPlaylist_updatesLastVideoDownloaded(self):
        self.fail("Once a playlist is downloaded, the index of the last "
                  "video downloaded should be updated and stored "
                  "somewhere.")

    @mock.patch('youtube.YoutubeDL')
    def test_downloadPlaylist_downloadsAudioByDefault(self, mock_ydl):
        YoutubeDownloader.download_playlist(self.billboard2019_playlist())
        mock_ydl.assert_called_with(YoutubeDownloader.download_audio_params)

    def test_downloadPlaylist_downloadFolderNotSelected_raisesErrors(self):
        # TODO: Move to file manager
        self.fail("If a download folder is not selected, an error needs"
                  "to be raised.")


if __name__ == '__main__':
    unittest.main()
