"""
ord('A') -> 65, ord('H') -> 72

  A  B  C  D  E  F  G  H
8                        8
7                        7
6                        6
5                        5
4                        4
3       x                3
2                        2
1                        1
  A  B  C  D  E  F  G  H

I make the strong assumption that the black pieces will be starting below row 3
and the white pieces will be starting above row 6. I believe this is only
necessary for the pond pieces.
"""
COLUMN_BOUNDS = ("A", "H")
ROW_BOUNDS = ("1", "9")
COL_INDEX = "ABCDEFGH"
ROW_INDEX = range(1, 9)

def inbounds(location):
    col, row = location[0], location[1]
    return col >= COLUMN_BOUNDS[0] and col <= COLUMN_BOUNDS[1] \
        and row >= ROW_BOUNDS[0] and row <= ROW_BOUNDS[1]


def translate(location, col_trans, row_trans):
    """Given a location return the strings corresponding to a translation in the x,y direction.
    
    :param location: the chess coordinate, e.g. `A1`
    :type location: str
    :param col_trans: a number representing the translation magnitude
    :type col_trans: int
    :param row_trans: a number representing the translation magnitude
    :type row_trans: int
    :returns: a new location
    :rtype: str
    """
    col_ndx, row_ndx = location[0], location[1]
    new_location = chr(ord(col_ndx) + col_trans) + chr(ord(row_ndx) + row_trans)
    return new_location


class Pond:
    def __init__(self):
        self.state = {
            "is_first_move": True
        }

    def get_moves(self, location, is_black=True, left_dominate=False, right_dominate=False):
        """Gets the possible moves for the current piece

        :param location: the chess coordinate, e.g. `A1`
        :type location: str
        :param left_dominate: true if the pond can take the piece diagonally to the left
        :type left_dominate: bool
        :param right_dominate: true if the pond can take the piece diagonally to the right
        :type right_dominate: bool
        :param is_black: true if the piece is black
        :type is_black: bool
        :returns: a list of locations
        :rtype: list[str]
        """
        dir_ = 1 if is_black else -1
        moves = []

        if inbounds(translate(location, 0, 1*dir_)):
            moves.append( translate(location, 0, 1*dir_) )

        if self.state["is_first_move"] and inbounds(translate(location, 0, 2*dir_)):
            moves.append( translate(location, 0, 2*dir_) )

        if left_dominate:
            moves.append( translate(location, -1, 1*dir_) )
        
        if right_dominate:
            moves.append( translate(location, 1, 1*dir_) )

        return sorted(moves)

    def set_is_first_move(self, b):
        self.state.update({ "is_first_move": b })


class Rook:
    def __init__(self):
        pass

    def get_moves(self, location):
        col_ndx, row_ndx = location[0], location[1]
        moves = []

        # Iterate across rows while holding column constant
        for row in ROW_INDEX:
            moves.append( f"{col_ndx}{row}" )

        # Likewise for columns
        for col in COL_INDEX:
            moves.append( f"{col}{row_ndx}" )

        return moves


class Knight:
    def __init__(self):
        pass


class Bishop:
    def __init__(self):
        pass


class Queen:
    def __init__(self):
        pass


class King:
    def __init__(self):
        pass


if __name__ == "__main__":
    pass