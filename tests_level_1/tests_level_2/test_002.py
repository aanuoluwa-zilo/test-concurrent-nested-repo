# Test at depth 2, file 2
import unittest

class TestNested2_2(unittest.TestCase):
    def test_depth_2(self):
        self.assertEqual(2, 2)

    def test_file_2(self):
        self.assertEqual(2, 2)

    def test_nested_structure(self):
        self.assertTrue(True)