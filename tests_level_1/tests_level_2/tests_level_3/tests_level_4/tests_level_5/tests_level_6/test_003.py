# Test at depth 6, file 3
import unittest

class TestNested6_3(unittest.TestCase):
    def test_depth_6(self):
        self.assertEqual(6, 6)

    def test_file_3(self):
        self.assertEqual(3, 3)

    def test_nested_structure(self):
        self.assertTrue(True)