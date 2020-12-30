import unittest
from unittest import mock

import youtube


class YoutubeTestCase(unittest.TestCase):
    def test_validYoutubeLink_badLink_returnsFalse(self):
        youtube_link = "https://youcube.com"

        self.assertFalse(youtube.valid_link(youtube_link))

    def test_validYoutubeLink_goodLink_returnsTrue(self):
        youtube_link = "https://www.youtube.com/playlist?list=" \
                       "PLCzImqCYRfNfJOzblgIkAPkG0HuMBtT5j"

        self.assertTrue(youtube.valid_link(youtube_link))

if __name__ == '__main__':
    unittest.main()
