import unittest
from chess.pieces import Rook


rook = Rook()


class TestRook(unittest.TestCase):

    def test_get_moves(self):
        self.assertEqual(
            rook.get_moves("A1"),
            sorted(
                [
                    "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                    "B1", "C1", "D1", "E1", "F1", "G1", "H1"
                ]
            )
        )

        self.assertEqual(
            rook.get_moves("D3"),
            sorted(
                [
                    "D1", "D2", "D4", "D5", "D6", "D7", "D8",
                    "A3", "B3", "C3", "E3", "F3", "G3", "H3"
                ]
            )
        )


if __name__ == "__main__":
    unittest.main()