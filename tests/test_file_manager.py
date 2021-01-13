import unittest

import file_manager
from file_manager import FileManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fm = FileManager()

    def test_fileManager_invalidDirectoryRaisesError(self):
        with self.assertRaisesRegexp(file_manager.InvalidDirectoryError,
                                     " is not a valid directory"):
            fm = FileManager(local_download_folder="lalala/download")



if __name__ == '__main__':
    unittest.main()
