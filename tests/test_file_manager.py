import unittest
from unittest import mock

import file_manager
from file_manager import FileManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fm = FileManager()

    def test_fileManager_invalidDirectoryRaisesError(self):
        with self.assertRaisesRegexp(file_manager.InvalidDirectoryError,
                                     " is not a valid directory"):
            fm = FileManager(local_download_folder="lalala/download")

    @mock.patch.object(file_manager.os.path, 'isdir')
    def test_fileManager_moveFilesToExternalStorage_checksIfStorageExists(
            self, mock_isdir):
        mock_isdir.return_value = False
        self.fm.move_file_to_external_storage("haha")
        mock_isdir.assert_called()

    @mock.patch.object(file_manager.os, 'listdir')
    def test_listFiles_getsListOfPaths(self, mock_listdir):
        mock_listdir.return_value = []
        self.assertEqual([], self.fm.list_local_download_files(),
                        "List local files should use listdir.")








if __name__ == '__main__':
    unittest.main()
