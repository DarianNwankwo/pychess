from graphics import Point, Rectangle
from pieces import PIECE_MAPPINGS
from pieces import Bishop, King, Knight, Pawn, Queen, Rook


class Tile:
    
    ACTIVE_COLOR = "green"

    def __init__(self, bl, tr, color):
        self.bl = bl
        self.tr = tr
        self.rectangle = Rectangle(
            Point(self.bl[0], self.bl[1]),
            Point(self.tr[0], self.tr[1])
        )
        self.piece_image = None
        self.piece_obj = None
        self.state = {
            "active": False,
            "original_fill": color
        }

    def location(self):
        return self.bl

    def getX(self):
        return self.bl[0]

    def getY(self):
        return self.bl[1]

    def get_moves(self, location):
        if self.piece_obj:
            return self.piece_obj.get_moves(location)
        return []

    def set_piece(self, piece_image, piece_name):
        self.piece_image = piece_image
        self.piece_obj = PIECE_MAPPINGS[piece_name]()
        return self

    def still_active(self):
        return self.state["active"]

    def has_piece(self):
        return self.piece_image != None

    def onclick(self, window):
        if self.piece_image:
            self.rectangle.undraw()
            active = self.state["active"]
            color = Tile.ACTIVE_COLOR if not active else self.state["original_fill"]
            self.rectangle.setFill(color)
            self.rectangle.draw(window)
            self.piece_image.undraw()
            self.piece_image.draw(window)
            self.state["active"] = not active


