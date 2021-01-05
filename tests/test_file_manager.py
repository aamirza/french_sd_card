import unittest


class FileManagerTestCase(unittest.TestCase):
    def test_something(self):
        self.fail()

    def test_downloadPlaylist_downloadsToFolder(self):
        self.fail("Downloading a Youtube playlist should download into "
                  "the designated folder.")

    def test_downloadPlaylist_updatesLastVideoDownloaded(self):
        self.fail("Once a playlist is downloaded, the index of the last "
                  "video downloaded should be updated and stored "
                  "somewhere.")

    def test_downloadPlaylist_invalidDownloadFolder_raisesErrors(self):
        self.fail("If a download folder is invalid, an error needs"
                  "to be raised.")


if __name__ == '__main__':
    unittest.main()
