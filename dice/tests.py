import unittest

import dice


class DieTests(unittest.TestCase):

    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)

    # this test method ensures that 6 sides dice has 6 sides
    # it also ensures that in 8 sides dice there are values from 1,7
    def test_createtion(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d8.value, range(1, 7))


if __name__ == "__main__":
    unittest.main()
