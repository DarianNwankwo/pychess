from graphics import *
from math import ceil
from time import sleep

from board import Board
from tile import Tile
from piece import Piece


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
    chess = Board()
    print(chess.board)

    while chess.still_playing():
        sleep(.1)
        xclick, yclick = chess.get_mouse_click()
        tile_location = chess.get_tile_clicked(xclick, yclick)
        tile = chess.get_tile(tile_location)

    #     cur_tile = board.get(tile_location, None)

    #     if not_valid_tile(cur_tile): continue

    #     if should_update_current_and_previous_tile(prev_tile, cur_tile):
    #         prev_tile.onclick(window)

    #     if should_update_current_tile(cur_tile):
    #         cur_tile.onclick(window)
    #         prev_tile = cur_tile