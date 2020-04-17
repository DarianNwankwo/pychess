class Piece:
    def __init__(self, piece):
        self.moves = piece_mappings[piece]