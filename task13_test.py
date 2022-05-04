import unittest
import random

from task13 import can_divide


class TaskTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(can_divide([3, 3, 3, 3], 3, 12 // 3, 12 // 3, 12 // 3, {}), False, "OK")
        self.assertEqual(can_divide([40], 0, 40 // 3, 40 // 3, 40 // 3, {}), False, "OK")
        self.assertEqual(can_divide([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 10, 118, 118, 118, {}), True, "OK")
        self.assertEqual(can_divide([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 12, 36, 36, 36, {}), True, "OK")

    def test_custom(self):
        for i in range(10000):
            num = random.randint(1, i+2)
            size = random.randint(5, 50)
            array = [num for _ in range(size)]
            one_third = sum(array) // 3
            result = can_divide(array, len(array) - 1, one_third, one_third, one_third, {})

            self.assertEqual(result, len(array) % 3 == 0, "OK")
            

if __name__ == '__main__':
    unittest.main()
