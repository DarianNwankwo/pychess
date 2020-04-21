import unittest
from chess.pieces import Pond

p = Pond()

class TestPond(unittest.TestCase):

    def test_get_moves(self):
        self.assertEqual(p.get_moves("A2"), ["A3", "A4"])
        p.set_is_first_move(False)
        self.assertEqual(p.get_moves("A3", False), ["A2"])
        self.assertEqual(p.get_moves("B4", True, True, True), ["A5", "B5", "C5"])
        self.assertEqual(p.get_moves("B4", False, True, True), ["A3", "B3", "C3"])


if __name__ == "__main__":
    unittest.main()