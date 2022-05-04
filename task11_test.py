import unittest
import random

from task11 import find_max_weight


class TaskTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(find_max_weight(10, [1, 4, 8]), 9, "OK")

    def test_custom(self):
        self.assertEqual(find_max_weight(20, [1, 4, 8]), 13, "OK")
        self.assertEqual(find_max_weight(50, [10, 40, 8]), 50, "OK")
        self.assertEqual(find_max_weight(45, [1, 40, 8]), 41, "OK")
        self.assertEqual(find_max_weight(200, [10, 40, 80]), 130, "OK")
        self.assertEqual(find_max_weight(2, [1, 41, 1]), 2, "OK")


if __name__ == '__main__':
    unittest.main()
