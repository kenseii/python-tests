import unittest

import dice


class DieTests(unittest.TestCase):

    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)

    # this test method ensures that 6 sides dice has 6 sides
    # it also ensures that in 6 sides dice there are values from 1,6
    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.value, range(1, 7))

    # test to check if i can add dice instances together and get an integer

    def test_add(self):
        self.assertIsInstance(self.d6 + self.d8, int)

    # test a dice to have one side
    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            dice.Die(1)


class RollTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        # 3 dices in hand
        self.hand3 = dice.Roll('3d6')

    # test the lowest possible output from 3 dices
    def test_lower(self):
        self.assertGreaterEqual(int(self.hand3), 3)

    # test the highest possible output from 3, 6 sided dices
    def test_upper(self):
        self.assertLessEqual(int(self.hand3), 18)

    def test_membership(self):
        test_die = dice.Die(2)
        # give this test die the value of what was in hand1
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die, self.hand1.results)

    # This function is supposed to raise that error once tested
    def test_bad_description(self):
        with self.assertRaises(ValueError):
            dice.Roll('2b6')

    # Adding tests to increase coverage
    def test_adding(self):
        self.assertEqual(self.hand1 + self.hand3, sum(self.hand1) + sum(self.hand3))


if __name__ == "__main__":
    unittest.main()
