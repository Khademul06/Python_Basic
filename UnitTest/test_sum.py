import unittest


class unitTest(unittest.TestCase):

    def test_sum_tc1(self):
        assert sum([1, 1]) == 2, "Should be 2"

    def test_sum_tc2(self):
        assert sum([1, 1]) == 3, "Should be 2"

    def test_sum_tc3(self):
        assert sum([1, 1]) == 3, "Should be 2"

    if __name__ == "main":
        test_sum_tc1()
        test_sum_tc2()
        test_sum_tc3()
