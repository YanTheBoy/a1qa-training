from Task1.scripts.file import File
import pytest


class TestFileModule:

    @pytest.mark.parametrize('filename', ['file.txt'])
    @pytest.mark.parametrize('content', ['simple string', ''])
    def test_getting_size(self, filename, content):
        file = File(filename, content)
        assert file.get_size() == len(content), 'Wrong size definition.'

    @pytest.mark.parametrize('filename', ['file.txt'])
    @pytest.mark.parametrize('content', ['simple string', ''])
    def test_getting_content(self, filename, content):
        file = File(filename, content)
        assert file._content == content, 'Wrong content returning.'

    @pytest.mark.parametrize('filename, content', [('file.txt', 'string')])
    def test_getting_filename(self, filename, content):
        file = File(filename, content)
        assert file.get_filename() == filename, 'Wrong filename definition.'

    @pytest.mark.parametrize('filename, content, extension',
                             [('file.txt', 'string', 'txt'),
                              ('file', 'some text', '')])
    def test_getting_extension(self, filename, content, extension):
        file = File(filename, content)
        print(extension)
        assert file.get_extension() == extension, 'Wrong extension definition.'

    @pytest.mark.parametrize('filename, content', [('file.txt', 'string')])
    def test_getting_size_after_get_ext(self, filename, content):
        file = File(filename, content)
        file.get_extension()
        assert file.get_size() == len(content), 'Wrong size definition.'

    @pytest.mark.parametrize('filename, content', [('file.txt', 'string')])
    def test_getting_content_after_get_ext(self, filename, content):
        file = File(filename, content)
        file.get_extension()
        assert file.get_content() == content, 'Wrong content returning.'
