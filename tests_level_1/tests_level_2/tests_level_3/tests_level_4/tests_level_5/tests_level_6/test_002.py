# Test at depth 6, file 2
import unittest

class TestNested6_2(unittest.TestCase):
    def test_depth_6(self):
        self.assertEqual(6, 6)

    def test_file_2(self):
        self.assertEqual(2, 2)

    def test_nested_structure(self):
        self.assertTrue(True)