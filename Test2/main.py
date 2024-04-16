from pprint import pprint
import random
import math
import unittest


def get_score(game_stamps, offset):
    home_score = 0
    away_score = 0
    for stamp in game_stamps:
        if stamp["offset"] <= offset:
            home_score = stamp["score"]["home"]
            away_score = stamp["score"]["away"]
        else:
            break
    return home_score, away_score

class TestGetScore(unittest.TestCase):

    def setUp(self):
        # Create a sample game_stamps list
        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 10, "score": {"home": 1, "away": 0}},
            {"offset": 20, "score": {"home": 1, "away": 1}},
            {"offset": 30, "score": {"home": 2, "away": 1}},
            {"offset": 40, "score": {"home": 2, "away": 2}},
            {"offset": 50, "score": {"home": 3, "away": 2}}
        ]

    def test_get_score_before_first_stamp(self):
        # Test when the offset is before the first stamp
        home_score, away_score = get_score(self.game_stamps, 5)
        self.assertEqual(home_score, 0)
        self.assertEqual(away_score, 0)

    def test_get_score_exact_offset(self):
        # Test when the offset is exactly matching a stamp
        home_score, away_score = get_score(self.game_stamps, 20)
        self.assertEqual(home_score, 1)
        self.assertEqual(away_score, 1)

    def test_get_score_between_stamps(self):
        # Test when the offset is between two stamps
        home_score, away_score = get_score(self.game_stamps, 25)
        self.assertEqual(home_score, 1)
        self.assertEqual(away_score, 1)

    def test_get_score_after_last_stamp(self):
        # Test when the offset is after the last stamp
        home_score, away_score = get_score(self.game_stamps, 60)
        self.assertEqual(home_score, 3)
        self.assertEqual(away_score, 2)

    def test_get_score_at_first_stamp(self):
        # Test when the offset is exactly at the first stamp
        home_score, away_score = get_score(self.game_stamps, 0)
        self.assertEqual(home_score, 0)
        self.assertEqual(away_score, 0)

    def test_get_score_at_last_stamp(self):
        # Test when the offset is exactly at the last stamp
        home_score, away_score = get_score(self.game_stamps, 50)
        self.assertEqual(home_score, 3)
        self.assertEqual(away_score, 2)

if __name__ == '__main__':
    unittest.main()

