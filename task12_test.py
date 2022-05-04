import unittest
import random

from task12 import half_subset


class TaskTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(half_subset([1, 2, 3]), (1, [3]))

    def test_random_numbers(self):
        for i in range(10000):

            size = random.randint(10, 500)
            initial = [random.randint(1, x + 1) for x in range(size)]
            output, index_array = half_subset(initial)

            half = sum(initial) // 2

            if output == -1:
                half = 0

            result_array = [initial[j - 1] for j in index_array]

            self.assertEqual(half, sum(result_array), f"Test case {i} - {sum(result_array)} should be {half}")


if __name__ == '__main__':
    unittest.main()
