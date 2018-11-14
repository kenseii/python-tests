import unittest

import moves


# Inherit testcase class from unittest modules


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_five_plus_five(self):
        assert 5+5 == 10

    def test_one_plus_one(self):
        assert not 1+1 == 3

    # test whether these 2 variables are equal, the current rock instance and a new rock instance
    def test_equal(self):
        self.assertEqual(self.rock, moves.Rock())

# test whether these 2 variables are not equal
    def test_not_equal(self):
        self.assertNotEqual(self.rock, self.paper)

    # test if rock is greater than scissors
    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)

    # test if paper is weaker than scissors
    def test_paper_weaker_than_scissors(self):
        self.assertLess(self.paper, self.scissors)


if __name__ == '__main__':
    unittest.main()
