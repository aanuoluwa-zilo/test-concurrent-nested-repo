# Test at depth 2, file 1
import unittest

class TestNested2_1(unittest.TestCase):
    def test_depth_2(self):
        self.assertEqual(2, 2)

    def test_file_1(self):
        self.assertEqual(1, 1)

    def test_nested_structure(self):
        self.assertTrue(True)