from graphics import Point, Rectangle


class Tile:
    
    ACTIVE_COLOR = "green"

    def __init__(self, bl, tr, color):
        self.bl = bl
        self.tr = tr
        self.rectangle = Rectangle(
            Point(self.bl[0], self.bl[1]),
            Point(self.tr[0], self.tr[1])
        )
        self.piece = None
        self.piece_name = ""
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

    def set_piece(self, p, n):
        self.piece = p
        self.piece_name = n
        return self

    def still_active(self):
        return self.state["active"]

    def has_piece(self):
        return self.piece != None

    def onclick(self, window):
        if self.piece:
            self.rectangle.undraw()
            active = self.state["active"]
            color = Tile.ACTIVE_COLOR if not active else self.state["original_fill"]
            self.rectangle.setFill(color)
            self.rectangle.draw(window)
            self.piece.undraw()
            self.piece.draw(window)
            self.state["active"] = not active


