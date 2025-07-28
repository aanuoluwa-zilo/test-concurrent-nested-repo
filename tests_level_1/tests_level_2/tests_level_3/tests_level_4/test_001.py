# Test at depth 4, file 1
import unittest

class TestNested4_1(unittest.TestCase):
    def test_depth_4(self):
        self.assertEqual(4, 4)

    def test_file_1(self):
        self.assertEqual(1, 1)

    def test_nested_structure(self):
        self.assertTrue(True)