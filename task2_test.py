import unittest

from task2 import how_many_stops


class TaskTest(unittest.TestCase):

    def test_basic(self):
        case1 = "950\n" \
            "400\n" \
            "4\n" \
            "200 375 550 750".splitlines()

        case2 = "10\n" \
                "3\n" \
                "4\n" \
                "1 2 5 9".splitlines()

        case3 = "200\n" \
                "250\n" \
                "2\n" \
                "100 150".splitlines()

        self.assertEqual(how_many_stops(case1), 2, "should be 2")
        self.assertEqual(how_many_stops(case2), -1, "should be -1")
        self.assertEqual(how_many_stops(case3), 0, "should be 0")

    def test_custom(self):
        case1 = "1000\n" \
                "355\n" \
                "5\n" \
                "250 500 750 900".splitlines()

        case2 = "60\n" \
                "10\n" \
                "6\n" \
                "1 11 21 31 41 51".splitlines()

        case3 = "5\n" \
                "1\n" \
                "4\n" \
                "1 2 3 4".splitlines()

        self.assertEqual(how_many_stops(case1), 3, "should be 3")
        self.assertEqual(how_many_stops(case2), 6, "should be 6")
        self.assertEqual(how_many_stops(case3), 4, "should be 4")


if __name__ == '__main__':
    unittest.main()

