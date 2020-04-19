from graphics import Point, Rectangle


class Tile:
    
    ACTIVE_COLOR = "green"

    def __init__(self, point1, point2, color):
        self.point1 = point1
        self.point2 = point2
        self.rectangle = Rectangle(
            Point(self.point1[0], self.point1[1]),
            Point(self.point2[0], self.point2[1])
        )
        self.piece = None
        self.state = {
            "active": False,
            "original_fill": color
        }

    def location(self):
        return self.point1

    def getX(self):
        return self.point1[0]

    def getY(self):
        return self.point1[1]

    def set_piece(self, p):
        self.piece = p
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


