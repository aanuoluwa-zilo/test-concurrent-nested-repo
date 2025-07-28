# Test at depth 4, file 3
import unittest

class TestNested4_3(unittest.TestCase):
    def test_depth_4(self):
        self.assertEqual(4, 4)

    def test_file_3(self):
        self.assertEqual(3, 3)

    def test_nested_structure(self):
        self.assertTrue(True)