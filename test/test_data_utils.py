import unittest
from awesomelib.data_utils import filter_even, flatten_list

class TestDataUtils(unittest.TestCase):
    def test_filter_even(self):
        self.assertEqual(filter_even([1, 2, 3, 4]), [2, 4])

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3], [4, 5]]), [1, 2, 3, 4, 5])