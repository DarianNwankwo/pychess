import unittest
from chess.pieces import Knight


knight = Knight()


class TestKnight(unittest.TestCase):

    def test_get_moves(self):
        self.assertEqual(
            knight.get_moves("F3"),
            sorted(
                ["G5", "H4", "E5", "D4", "E1", "D2", "G1", "H2"]
            )
        )


if __name__ == "__main__":
    unittest.main()