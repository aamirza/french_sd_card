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
    @mock.patch.object(file_manager.os, 'rename')
    def test_fileManager_moveFilesToExternalStorage_checksIfStorageExists(
            self, mock_rename, mock_isdir):
        mock_isdir.return_value = True
        self.fm.move_file_to_external_storage("haha")
        mock_isdir.assert_called()  # Check if storage directory exists
        mock_rename.assert_called()  # Check if file was moved

    def test_moveFilesToExternalStorage_raisesErrorIfStorageNotFound(self):
        with self.assertRaisesRegex(
                file_manager.ExternalStorageNotFound,
                "not found. Ensure your storage is mounted properly and that "
                "the directory is valid."):
            self.fm.move_file_to_external_storage("")


    @mock.patch.object(file_manager.os, 'listdir')
    def test_listFiles_getsListOfPaths(self, mock_listdir):
        mock_listdir.return_value = []
        self.assertEqual([], self.fm.list_local_download_files(),
                        "List local files should use listdir.")








if __name__ == '__main__':
    unittest.main()
