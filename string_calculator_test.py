import unittest
from string_calculator import Add

class TestStringCalculator(unittest.TestCase):
    def test_none_numbers(self):
        self.assertEqual(0, Add(""))
    def test_single_number(self):
        self.assertEqual(1, Add("1"))
    def test_two_numbers(self):
        self.assertEqual(3, Add("1,2"))
    def test_multi_numbers(self):
        self.assertEqual(15, Add("1,2,3,4,5"))
    def test_valueError(self):
        with self.assertRaises(ValueError):
            Add("1,a")
    def test_newlineCorrect(self):
        self.assertEqual(6, Add("1\n2,3"))
    def test_nelineError(self):
        with self.assertRaises(ValueError):
            Add("1,\n")

if __name__ == "__main__":
    unittest.main()