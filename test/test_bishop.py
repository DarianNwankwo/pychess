import unittest
from chess.pieces import Bishop


bishop = Bishop()


class TestBishop(unittest.TestCase):

    def test_get_moves(self):
        self.assertEqual(
            bishop.get_moves("C1"),
            sorted(
                ['A3', 'B2', 'D2', 'E3', 'F4', 'G5', 'H6']
            )
        )


if __name__ == "__main__":
    unittest.main()