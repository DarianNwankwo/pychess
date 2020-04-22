from graphics import *
from tile import Tile


class Board:

    IMAGE_DIR = "./images"
    COL_INDEX = "ABCDEFGH"
    ROW_INDEX = range(1,9)
    CHESS_PIECE_DIMENSIONS = (60, 60)
    ORDINAL_OFFSET = 64
    WINDOW_ORIGIN = (0, 0)
    PRIMARY_COLOR = "purple"
    SECONDARY_COLOR = "orange"
    INIT_BOARD_CONFIG = {
    "pawn": [col+"7" for col in COL_INDEX] + [col+"2" for col in COL_INDEX],
    "rook": ["A8", "H8", "A1", "H1"],
    "knight": ["B8", "G8", "B1", "G1"],
    "bishop": ["C8", "F8", "C1", "F1"],
    "queen": ["D8", "D1"],
    "king": ["E8", "E1"]
    }

    def __init__(
        self,
        board_width=480,
        board_height=480,
        padding=200,
        window_title="Chess"
        ):
        self.width = board_width
        self.height = board_height
        self.window_width = board_width + padding
        self.window_height = board_height + padding
        self.window_title = window_title
        self.xoffset = padding // 2
        self.yoffset = padding // 2
        self._build_game()

    def _init_state(self):
        self.state = {
            "game_still_active": True,
            "tile_is_active": False,
            "active_tile": None,
            "prev_tile": None
        }

    def _initialize_board(self):
        """Initialize the carteasian and chess based coordinates for the board."""
        board = {}
        is_colored = True
        cpd = self._get_chess_piece_dimensions()
        xoffset, yoffset = self._get_offsets()

        for ondx, row_num in enumerate(Board.ROW_INDEX):
            for indx, col_char in enumerate(Board.COL_INDEX):
                chess_coord = f"{col_char}{row_num}"
                cartesian_coord_bl = ( cpd[0]*indx + xoffset, cpd[1]*ondx + yoffset )
                cartesian_coord_tr = ( cpd[0]*(indx+1) + xoffset, cpd[1]*(ondx+1) + yoffset )
                color = self._get_color(is_colored)
                board[chess_coord] = Tile(cartesian_coord_bl, cartesian_coord_tr, color)
                is_colored = not is_colored
            is_colored = not is_colored

        self.board = board

    def _create_gui(self):
        wd = self._get_window_dimensions()
        origin = self._get_window_origin()
        window = GraphWin(self.window_title, wd[0], wd[1])
        window.setCoords(origin[0], origin[1], wd[0], wd[1])
        self.window = window

    def _get_window_dimensions(self):
        return (self.window_width, self.window_height)

    def _draw_chessboard(self):
        line_count = len(Board.ROW_INDEX) + 1
        xoffset, yoffset = self._get_offsets()
        cpd = self._get_chess_piece_dimensions()

        for _ in range(line_count):
            start = Point(xoffset, yoffset)
            end = Point(xoffset, len(Board.ROW_INDEX)*cpd[0] + yoffset)
            Line(start, end).draw(self.window)
            start = Point(yoffset, xoffset)
            end = Point(len(Board.ROW_INDEX)*cpd[0] + yoffset, xoffset)
            Line(start, end).draw(self.window)
            xoffset += cpd[0]
    
    def _color_chessboard(self):
        xoffset, yoffset = self._get_offsets()
        cpd = self._get_chess_piece_dimensions()

        for row_ndx in range(len(Board.ROW_INDEX)):
            zig_zag = row_ndx % 2 == 0
            for col_ndx in range(len(Board.COL_INDEX)):
                start = Point( xoffset + cpd[0]*col_ndx, yoffset + cpd[1]*row_ndx)
                end = Point( xoffset + cpd[0]*(col_ndx+1), yoffset + cpd[1]*(row_ndx+1))
                color = self._get_color(zig_zag)
                zig_zag = not zig_zag
                r = Rectangle(start, end)
                r.setFill(color)
                r.draw(self.window)

    def _setup_chessboard(self):
        cpd = self._get_chess_piece_dimensions()
        board = self._get_board()
        window = self._get_window()

        for piece, locations in Board.INIT_BOARD_CONFIG.items():
            midpoint = len(locations) // 2
            for count, loc in enumerate(locations):
                image_name = self._get_image_name(count < midpoint, piece)
                piece_image = Image(
                    Point(
                        board[loc].getX() + cpd[0] // 2,
                        board[loc].getY() + cpd[1] // 2
                    ),
                    image_name
                )
                piece_image.draw(window)
                board[loc].set_piece(piece_image, piece)

    def _get_window(self):
        return self.window

    def _get_board(self):
        return self.board

    def _get_image_name(self, is_white, piece):
        return f"{Board.IMAGE_DIR}/white_{piece}.png" if is_white else f"{Board.IMAGE_DIR}/black_{piece}.png"

    def _get_window_origin(self):
        return Board.WINDOW_ORIGIN

    def _build_game(self):
        self._initialize_board()
        self._create_gui()
        self._draw_chessboard()
        self._color_chessboard()
        self._setup_chessboard()
        self._init_state()

    def _get_chess_piece_dimensions(self):
        """Returns a tuple of the chess piece dimensions"""
        return Board.CHESS_PIECE_DIMENSIONS

    def _get_color(self, is_primary):
        return Board.PRIMARY_COLOR if is_primary else Board.SECONDARY_COLOR
    
    def _get_offsets(self):
        return self.xoffset, self.yoffset

    def _get_active_tile(self):
        return self.state["active_tile"]

    def still_playing(self):
        return self.state["game_still_active"]

    def get_tile(self, location):
        # If clicking the same tile, return active tile
        if self._get_board().get(location, None) == self._get_active_tile():
            return self._get_active_tile()

        # Deactivate active tile
        if self.state.get("tile_is_active", False):
            tile = self._get_active_tile()
            tile.onclick( self._get_window() )
            self.state.update( {"tile_is_active": False} )

        tile = self._get_board().get(location, None)

        # Only change state of tile's with pieces
        if tile and not tile.has_piece(): return tile
        if not tile: return tile

        tile.onclick( self._get_window() )
        self.state.update({
            "tile_is_active": True,
            "active_tile": tile
        })
        return tile

    def get_tile_clicked(self, x, y):
        xoffset, yoffset = self._get_offsets()
        xprime, yprime = x - xoffset, y - yoffset
        cpd = self._get_chess_piece_dimensions()

        col_ndx = chr( int(xprime // cpd[0]) + 1 + Board.ORDINAL_OFFSET )
        row_ndx = int(yprime // cpd[1]) + 1
        return f"{col_ndx}{row_ndx}"

    def get_mouse_click(self):
        w = self._get_window()
        p = w.getMouse()
        return p.getX(), p.getY()