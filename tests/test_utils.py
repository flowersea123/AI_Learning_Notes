"""测试工具函数"""

import unittest
from src.utils import add_numbers, multiply_numbers


class TestUtils(unittest.TestCase):
    """测试工具函数"""
    
    def test_add_numbers(self):
        """测试加法"""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_multiply_numbers(self):
        """测试乘法"""
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 2), -2)
        self.assertEqual(multiply_numbers(0, 100), 0)


if __name__ == "__main__":
    unittest.main()
