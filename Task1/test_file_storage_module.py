from Task1.scripts.file_storage import FileStorage
from Task1.scripts.file import File
import pytest


class TestFileStorageModule:

    @pytest.mark.parametrize('filestorage', [FileStorage(5), FileStorage(-1)])
    def test_creating_storage_with_correct_value(self, filestorage):
        assert filestorage._max_size >= 0, 'Setting negative storage size.'

    @pytest.mark.parametrize('filestorage', [FileStorage(10)])
    @pytest.mark.parametrize('file', [File('A.doc', 'ninewords'), File('B.omg', 'elevenwords')])
    def test_writing_in_filestorage(self, filestorage, file):
        assert (file.get_size() < filestorage._available_size) == filestorage.write(file), \
            'Wrongly file storage writing.'

    @pytest.mark.parametrize('filestorage, file1, file2', [
        (FileStorage(10), File('A.doc', '12345'), File('B.omg', '67')),
        (FileStorage(10), File('C.kek', '12345'), File('D.jpg', '1234567')),
        (FileStorage(10), File('E.pin', '12345'), File('F.tag', '54321'))
    ])
    def test_overwriting_in_filestorage(self, file1, file2, filestorage):
        filestorage.write(file1)
        assert (file2.get_size() <= filestorage._available_size) == filestorage.write(file2), 'Oversize writing.'

    @pytest.mark.parametrize('filestorage, file', [(FileStorage(10), File('A.doc', 'simple text'))])
    def test_file_exist_error_raising(self, file, filestorage):
        filestorage.write(file)
        with pytest.raises(Exception):
            assert filestorage.write(file), 'File exist error does not raise.'

    @pytest.mark.parametrize('filestorage', [FileStorage(10)])
    @pytest.mark.parametrize('file1, file2',
                             [(File('A.doc', 'smart'), File('B.omg', 'kind'))])
    def test_deleting_from_storage(self, file1, file2, filestorage):
        filestorage.write(file1)
        filestorage.write(file2)
        assert filestorage.delete(file1._filename) != (file1._filename in filestorage._files), 'Wrongly file deleting.'

    @pytest.mark.parametrize('filestorage', [FileStorage(10)])
    @pytest.mark.parametrize('file', [File('A.doc', 'smart'), File('B.omg', 'kind')])
    def test_getting_file_exist(self, file, filestorage):
        filestorage.write(file)
        assert filestorage.is_exists(file) == (file._filename in filestorage._files), 'Wrongly file exist definition.'

    @pytest.mark.parametrize('filestorage, file', [(FileStorage(10), File('A.doc', 'smart'))])
    def test_getting_file(self, file, filestorage):
        filestorage.write(file)
        assert filestorage.get_file(file._filename) is file, 'Incorrect return of an existing file.'

    @pytest.mark.parametrize('filestorage', [FileStorage(10)])
    def test_getting_none_if_no_file(self, filestorage):
        assert filestorage.get_file('Filename.txt') is None, 'None does not returning.'
        
    @pytest.mark.parametrize('filestorage, file1, file2', [
        (FileStorage(10), File('A.doc', 'fivee'), File('B.omg', 'four'))])
    def test_getting_files_list(self, file1, file2, filestorage):
        filestorage.write(file1)
        filestorage.write(file2)
        assert filestorage.get_files() == [file1, file2], 'Inccorect file`s list returning'
        
    @pytest.mark.parametrize('filestorage, file', [(FileStorage(10), File('A.doc', 'smart'))])
    def test_getting_available_size(self, file, filestorage):
        filestorage.write(file)
        assert filestorage.get_available_size() == (filestorage._max_size - len(file._content)), \
            'Incorrect size definition.'
            
    @pytest.mark.parametrize('filestorage', [FileStorage(10), FileStorage(-5), FileStorage(0)])
    def test_getting_storage_max_size(self, filestorage):
        assert filestorage.get_max_size() == filestorage._max_size, 'Incorrect max size definition.'
