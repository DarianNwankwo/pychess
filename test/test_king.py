import unittest
from chess.pieces import King


king = King()


class TestKing(unittest.TestCase):

    def test_get_moves(self):
        self.assertEqual(
            king.get_moves("E4"),
            sorted(
                ["F3", "F4", "F5", "E5", "E3", "D3", "D4", "D5"]
            )
        )