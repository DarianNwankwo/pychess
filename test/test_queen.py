import unittest
from chess.pieces import Queen


queen = Queen()


class TestQueen(unittest.TestCase):

    def test_get_moves(self):
        self.assertEqual(
            queen.get_moves("E4"),
            sorted(
                [
                    "F3", "F4", "F5", "E5", "E3", "D3", "D4", "D5",
                    "C2", "B1", "G6", "H7", "G2", "H1", "C6", "B7",
                    "A8", "C4", "B4", "A4", "G4", "H4", "E1", "E2",
                    "E6", "E7", "E8"
                ]
            )
        )


if __name__ == "__main__":
    unittest.main()