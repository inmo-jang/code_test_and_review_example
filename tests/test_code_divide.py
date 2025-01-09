import unittest
import json
from functions import divide

class TestDivideFunction(unittest.TestCase):
    def setUp(self):
        # JSON 파일에서 테스트 케이스 로드
        with open("tests/test_cases_divide.json", "r") as f:
            self.test_cases = json.load(f)

    def test_divide(self):
        for case in self.test_cases:
            a = case["input"]["a"]
            b = case["input"]["b"]

            if "expected" in case:
                with self.subTest(a=a, b=b):
                    self.assertAlmostEqual(divide(a, b), case["expected"], places=7)
            elif "expected_error" in case:
                with self.subTest(a=a, b=b):
                    with self.assertRaises(eval(case["expected_error"])):
                        divide(a, b)

if __name__ == "__main__":
    unittest.main()
