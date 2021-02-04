from unittest import TestCase
from file_duplicator import file_handler


class TestIterateFile(TestCase):
    def test_ideal_case(self):
        result = file_handler.iterate_file('testfile.txt', 1)
        expected = 'testfile(1).txt'
        self.assertEqual(result, expected)

    def test_multiple_periods(self):
        result = file_handler.iterate_file('hibernate.cfg.xml', 1)
        expected = 'hibernate.cfg(1).xml'
        self.assertEqual(result, expected)