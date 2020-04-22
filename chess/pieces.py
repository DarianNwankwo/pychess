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
ROW_BOUNDS = ("1", "8")
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


class Pawn:

    name = "pawn"

    def __init__(self, is_black=True):
        self.state = {
            "is_first_move": True,
            "is_black": is_black
        }

    @classmethod
    def get_name(cls):
        return cls.name

    def get_moves(self, location, left_dominate=False, right_dominate=False):
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
        dir_ = 1 if self.state.get("is_black", False) else -1
        moves = []

        if inbounds( translate(location, 0, 1*dir_) ):
            moves.append( translate(location, 0, 1*dir_) )

        if self.state["is_first_move"] and inbounds( translate(location, 0, 2*dir_) ):
            moves.append( translate(location, 0, 2*dir_) )

        if left_dominate and inbounds( translate(location, -1, 1*dir_) ):
            moves.append( translate(location, -1, 1*dir_) )
        
        if right_dominate and inbounds( translate(location, 1, 1*dir_) ):
            moves.append( translate(location, 1, 1*dir_) )

        return sorted(moves)

    def set_is_first_move(self, b):
        self.state.update({ "is_first_move": b })
    

class Rook:

    name = "rook"

    def __init__(self):
        pass

    @classmethod
    def get_name(cls):
        return cls.name

    def get_moves(self, location):
        col_ndx, row_ndx = location[0], location[1]
        moves = []

        # Iterate across rows while holding column constant
        for row in ROW_INDEX:
            moves.append( f"{col_ndx}{row}" )

        # Likewise for columns
        for col in COL_INDEX:
            moves.append( f"{col}{row_ndx}" )

        return sorted(list(filter(lambda loc: loc != location, moves)))


class Knight:

    name = "knight"

    def __init__(self):
        pass

    @classmethod
    def get_name(cls):
        return cls.name

    def get_moves(self, location):
        translations = [(2, 1), (2, -1), (-2, 1), (-2, -1)]
        moves = []

        for trans in translations:
            new_location = translate(location, *trans)
            if inbounds(new_location):
                moves.append(new_location)

        for trans in translations:
            new_location = translate(location, *reversed(trans))
            if inbounds(new_location):
                moves.append(new_location)
        
        return sorted(moves)


class Bishop:

    name = "bishop"

    def __init__(self):
        pass

    def get_moves(self, location):
        left_location = right_location = location
        moves = []
        # Collect moves diagonally up
        steps = ord(ROW_BOUNDS[1]) - ord(location[1])
        for _ in range(steps):
            left_location = translate(left_location, 1, 1)
            right_location = translate(right_location, -1, 1)
            if inbounds(left_location): moves.append(left_location)
            if inbounds(right_location): moves.append(right_location)

        # Collect moves diagonally down
        left_location = right_location = location
        steps = ord(location[1]) - ord(ROW_BOUNDS[0])
        for _ in range(steps):
            left_location = translate(left_location, 1, -1)
            right_location = translate(right_location, -1, -1)
            if inbounds(left_location): moves.append(left_location)
            if inbounds(right_location): moves.append(right_location)

        return sorted(moves)
        

    @classmethod
    def get_name(cls):
        return cls.name


class Queen:

    name = "queen"

    def __init__(self):
        pass

    @classmethod
    def get_name(cls):
        return cls.name

    def get_moves(self, location):
        col_ndx, row_ndx = location[0], location[1]
        left_location = right_location = location
        moves = []

        # Iterate across rows while holding column constant
        for row in ROW_INDEX:
            moves.append( f"{col_ndx}{row}" )

        # Likewise for columns
        for col in COL_INDEX:
            moves.append( f"{col}{row_ndx}" )

        # Collect moves diagonally up
        steps = ord(ROW_BOUNDS[1]) - ord(location[1])
        for _ in range(steps):
            left_location = translate(left_location, 1, 1)
            right_location = translate(right_location, -1, 1)
            if inbounds(left_location): moves.append(left_location)
            if inbounds(right_location): moves.append(right_location)

        # Collect moves diagonally down
        left_location = right_location = location
        steps = ord(location[1]) - ord(ROW_BOUNDS[0])
        for _ in range(steps):
            left_location = translate(left_location, 1, -1)
            right_location = translate(right_location, -1, -1)
            if inbounds(left_location): moves.append(left_location)
            if inbounds(right_location): moves.append(right_location)

        moves = list(set(moves))

        return sorted(list(filter(lambda loc : loc != location, moves)))



class King:

    name = "king"

    def __init__(self):
        pass

    @classmethod
    def get_name(cls):
        return cls.name

    def get_moves(self, location):
        translations = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        moves = []

        for trans in translations:
            new_location = translate(location, *trans)
            if inbounds(new_location):
                moves.append(new_location)

        return sorted(moves)


PIECE_MAPPINGS = {
    "pawn": Pawn,
    "rook": Rook,
    "bishop": Bishop,
    "queen": Queen,
    "king": King,
    "knight": Knight
}


if __name__ == "__main__":
    print(PIECE_MAPPINGS["knight"]().get_moves("D4"))