import unittest
import random

from task5 import max_prize_amount


class TaskTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(max_prize_amount(6), (3, [1, 2, 3]), "OK")
        self.assertEqual(max_prize_amount(8), (3, [1, 2, 5]), "OK")
        self.assertEqual(max_prize_amount(2), (1, [2]), "OK")
        print("done")

    def test_custom(self):
        self.assertEqual(max_prize_amount(12), (4, [1, 2, 3, 6]), "OK")
        self.assertEqual(max_prize_amount(1), (1, [1]), "OK")
        self.assertEqual(max_prize_amount(25), (6, [1, 2, 3, 4, 5, 10]), "OK")
        print("done")


if __name__ == '__main__':
    unittest.main()
