import unittest

from score_card import score_card, stratum_for, wound_area_points


class ScoreCardTest(unittest.TestCase):
    def test_minimum_is_low(self):
        result = score_card(40, 0, 4, 1, 1, 0)
        self.assertEqual(result.points, 0)
        self.assertEqual(result.stratum, "low")

    def test_maximum_is_high(self):
        result = score_card(70, 2, 1, 5, 120, 3)
        self.assertEqual((result.points, result.stratum), (59, "high"))

    def test_frozen_boundaries(self):
        self.assertEqual(stratum_for(23), "low")
        self.assertEqual(stratum_for(24), "intermediate")
        self.assertEqual(stratum_for(33), "intermediate")
        self.assertEqual(stratum_for(34), "high")

    def test_wound_area_cuts(self):
        self.assertEqual(
            [wound_area_points(x) for x in (4.99, 5, 20, 20.01, 100, 100.01)],
            [0, 3, 3, 9, 9, 10],
        )

    def test_rejects_unknown_grade(self):
        with self.assertRaises(ValueError):
            score_card(70, 3, 1, 5, 10, 1)


if __name__ == "__main__":
    unittest.main()
