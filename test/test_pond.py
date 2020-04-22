import unittest
from chess.pieces import Pawn


black_pawn = Pawn(is_black=True)
white_pawn = Pawn(is_black=False)


class Testpawn(unittest.TestCase):

    def test_forwards_get_moves(self):
        p = black_pawn
        self.assertEqual(p.get_moves("A2"), ["A3", "A4"])
        p.set_is_first_move(False)
        self.assertEqual(p.get_moves("A3"), ["A4"])
        self.assertEqual(p.get_moves("B4", True, True), ["A5", "B5", "C5"])
        self.assertEqual(p.get_moves("H5", True, True), ["G6", "H6"])
        self.assertEqual(p.get_moves("E8", True, True), [])
        self.assertEqual(p.get_moves("D6", right_dominate=True), ["D7", "E7"])
        self.assertEqual(p.get_moves("D6", left_dominate=True), ["C7", "D7"])

    def test_backwards_get_moves(self):
        p = white_pawn
        self.assertEqual(p.get_moves("A7"), ["A5", "A6"])
        p.set_is_first_move(False)
        self.assertEqual(p.get_moves("A3"), ["A2"])
        self.assertEqual(p.get_moves("B4", True, True), ["A3", "B3", "C3"])
        self.assertEqual(p.get_moves("H5", True, True), ["G4", "H4"])
        self.assertEqual(p.get_moves("E7", True, True), ["D6", "E6", "F6"])
        self.assertEqual(p.get_moves("D6", right_dominate=True), ["D5", "E5"])
        self.assertEqual(p.get_moves("D6", left_dominate=True), ["C5", "D5"])


if __name__ == "__main__":
    unittest.main()