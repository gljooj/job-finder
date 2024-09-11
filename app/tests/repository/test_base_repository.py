import os
import unittest
from app.repository.base_repository import BaseRepository


class TestBaseRepository(unittest.TestCase):
    def setUp(self):
        self.repository = BaseRepository('../tests/repository/test.json')

    def test_read_json_error(self):
        result = self.repository.save({})
        assert result == None

    def test_empty_file(self):
        BaseRepository('../tests/repository/temp.json')
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, 'temp.json')
        os.remove(file_path)
