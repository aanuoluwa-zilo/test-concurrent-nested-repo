# Test at depth 2, file 3
import unittest

class TestNested2_3(unittest.TestCase):
    def test_depth_2(self):
        self.assertEqual(2, 2)

    def test_file_3(self):
        self.assertEqual(3, 3)

    def test_nested_structure(self):
        self.assertTrue(True)