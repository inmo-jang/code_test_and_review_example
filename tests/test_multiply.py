import json
import unittest
from functions import multiply

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_cases(self):
        with open("tests/test_cases.json", "r") as f:
            test_cases = json.load(f)

        for case in test_cases:
            a = case["input"]["a"]
            b = case["input"]["b"]
            expected = case["expected"]
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(multiply(a, b), expected)

if __name__ == "__main__":
    unittest.main()
