def pond_moves(location):
    """Returns a tuple of the possible moves"""
    pass

def rook_moves(location):
    pass

def knight_moves(location):
    pass

def bishop_moves(location):
    pass

def queen_moves(location):
    pass

def king_moves(location):
    pass


class Piece:
    def __init__(self, piece):
        self.moves = piece_mappings[piece]