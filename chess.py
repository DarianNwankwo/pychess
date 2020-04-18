from graphics import *
from math import ceil
from time import sleep

from tile import Tile
from piece import Piece


IMAGE_DIR = "images"
COL_INDEX = "ABCDEFGH"
ROW_INDEX = range(1, 9)
CHESS_PIECE_DIMENSIONS = (60, 60)
ORDINAL_OFFSET = 64
PADDING = 140
BOARD_WIDTH = 480
BOARD_HEIGHT = 480
WINDOW_WIDTH = BOARD_WIDTH + PADDING
WINDOW_HEIGHT = BOARD_HEIGHT + PADDING
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


def initialize_board():
    """Initialize the cartesian and chess based coordinates for the board."""
    board = {}
    offset = PADDING // 2
    is_colored = True

    for ondx, row_num in enumerate(ROW_INDEX, start=0):
        for indx, col_char in enumerate(COL_INDEX, start=0):
            chess_coord = "{}{}".format(col_char, row_num)
            cartesian_coord_bl = (
                CHESS_PIECE_DIMENSIONS[0]*indx + offset,
                CHESS_PIECE_DIMENSIONS[1]*ondx + offset
            )
            cartesian_coord_tr = (
                CHESS_PIECE_DIMENSIONS[0]*indx + offset + CHESS_PIECE_DIMENSIONS[0],
                CHESS_PIECE_DIMENSIONS[1]*ondx + offset + CHESS_PIECE_DIMENSIONS[1]
            )

            color = PRIMARY_COLOR if is_colored else SECONDARY_COLOR
            board[chess_coord] = Tile(cartesian_coord_bl, cartesian_coord_tr, color)
            is_colored = not is_colored
        is_colored = not is_colored

    return board


def create_gui(window_name):
    window = GraphWin(window_name, WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setCoords(
        WINDOW_ORIGIN[0], WINDOW_ORIGIN[1], WINDOW_WIDTH, WINDOW_HEIGHT)
    return window


def draw_chessboard(window):
    line_count = len(ROW_INDEX) + 1
    x_offset, y_offset = PADDING // 2, PADDING // 2

    for _ in range(line_count):
        start, end = Point(x_offset, y_offset), Point(x_offset, len(ROW_INDEX)*CHESS_PIECE_DIMENSIONS[0] + y_offset)
        Line(start, end).draw(window)
        start, end = Point(y_offset, x_offset), Point(len(ROW_INDEX)*CHESS_PIECE_DIMENSIONS[0] + y_offset, x_offset)
        Line(start, end).draw(window)
        x_offset += CHESS_PIECE_DIMENSIONS[0]

    return window


def color_chessboard(window, color=PRIMARY_COLOR):
    """Color every other tile."""
    x_offset, y_offset = PADDING // 2, PADDING // 2

    for row_ndx in range(len(ROW_INDEX)):
        # When alternating columns, the square to draw is offset by 1. This simulates the
        # zigzag nature of the painting
        zig_zag = True if row_ndx % 2 else False
        for col_ndx in range(len(COL_INDEX)):
            start = Point(
                x_offset + CHESS_PIECE_DIMENSIONS[0]*col_ndx,
                y_offset + CHESS_PIECE_DIMENSIONS[0]*row_ndx
            )
            end = Point(
                x_offset + CHESS_PIECE_DIMENSIONS[0]*col_ndx + CHESS_PIECE_DIMENSIONS[0],
                y_offset + CHESS_PIECE_DIMENSIONS[0] * row_ndx + CHESS_PIECE_DIMENSIONS[0]
            )
            color = SECONDARY_COLOR if zig_zag else PRIMARY_COLOR
            zig_zag = not zig_zag
            rectangle = Rectangle(start, end)
            rectangle.setFill(color)
            rectangle.draw(window)

    return window


def setup_chessboard(window, board):
    """Draw the game pieces onto the chess board."""
    for piece, locations in INIT_BOARD_CONFIG.items():
        midpoint = len(locations) // 2
        for count, loc in enumerate(locations):
            image_name = f"{IMAGE_DIR}/black_{piece}.png" if count < midpoint else f"{IMAGE_DIR}/white_{piece}.png"
            piece_image = Image(
                Point(
                    board[loc].getX() + CHESS_PIECE_DIMENSIONS[0] // 2,
                    board[loc].getY() + CHESS_PIECE_DIMENSIONS[1]  // 2
                ),
                image_name
            )
            piece_image.draw(window)
            board[loc].piece = piece_image
            
    return window


def get_mouse_click(window):
    point = window.getMouse()
    return point.getX(), point.getY()


def get_tile(board, x, y):
    x_offset, y_offset = PADDING // 2, PADDING // 2
    xprime, yprime = x - x_offset, y - y_offset
    col_ndx = chr( ceil(xprime / CHESS_PIECE_DIMENSIONS[1]) + ORDINAL_OFFSET)
    row_ndx = ceil(yprime / CHESS_PIECE_DIMENSIONS[0])
    return f"{col_ndx}{row_ndx}"


def should_update_current_and_previous_tile(prev_tile, cur_tile):
    return cur_tile and prev_tile and (cur_tile != prev_tile) and prev_tile.still_active()


def should_update_current_tile(cur):
    return cur != None


def not_valid_tile(tile):
    return tile and not tile.has_piece()


if __name__ == "__main__":
    board = initialize_board()
    window = create_gui("Chess")
    window = draw_chessboard(window)
    window = color_chessboard(window)
    window = setup_chessboard(window, board)

    game_still_active = True
    cur_tile, prev_tile = None, None

    while game_still_active:
        sleep(.1)
        xclick, yclick = get_mouse_click(window)
        tile_location = get_tile(board, xclick, yclick)

        cur_tile = board.get(tile_location, None)

        if not_valid_tile(cur_tile): continue

        if should_update_current_and_previous_tile(prev_tile, cur_tile):
            prev_tile.onclick(window)

        if should_update_current_tile(cur_tile):
            cur_tile.onclick(window)
            prev_tile = cur_tile