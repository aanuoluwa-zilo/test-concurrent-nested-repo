# Test at depth 4, file 2
import unittest

class TestNested4_2(unittest.TestCase):
    def test_depth_4(self):
        self.assertEqual(4, 4)

    def test_file_2(self):
        self.assertEqual(2, 2)

    def test_nested_structure(self):
        self.assertTrue(True)