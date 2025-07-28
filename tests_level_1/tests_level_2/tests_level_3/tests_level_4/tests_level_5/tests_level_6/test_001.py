# Test at depth 6, file 1
import unittest

class TestNested6_1(unittest.TestCase):
    def test_depth_6(self):
        self.assertEqual(6, 6)

    def test_file_1(self):
        self.assertEqual(1, 1)

    def test_nested_structure(self):
        self.assertTrue(True)