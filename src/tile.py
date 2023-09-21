from constants import *


class Tile:
    """
    Represents a tile on the game board.

    Attributes:
        value (int): The value displayed on the tile.
        bg_color (tuple): The background color of the tile.
        text_color (tuple): The text color of the tile.
        merged (bool): A flag indicating whether the tile has been merged with another tile.
    """

    def __init__(self, value, bg_color, text_color, merged=False):
        self.value = value
        self.bg_color = bg_color
        self.text_color = text_color
        self.merged = merged


def get_tile(value):
    """
    Create and return a Tile object based on the given value.

    Args:
        value (int): The value to assign to the Tile.

    Returns:
        Tile: A Tile object with the specified value and appropriate colors.
    """
    match value:
        case 0:
            return Tile(0, COLOR_EMPTY, WHITE)
        case 2:
            return Tile(2, COLOR_2, BLACK)
        case 4:
            return Tile(4, COLOR_4, BLACK)
        case 8:
            return Tile(8, COLOR_8, WHITE)
        case 16:
            return Tile(16, COLOR_16, WHITE)
        case 32:
            return Tile(32, COLOR_32, WHITE)
        case 64:
            return Tile(64, COLOR_64, WHITE)
        case 128:
            return Tile(128, COLOR_128, WHITE)
        case 256:
            return Tile(256, COLOR_256, WHITE)
        case 512:
            return Tile(512, COLOR_512, WHITE)
        case 1024:
            return Tile(1024, COLOR_1024, WHITE)
        case 2048:
            return Tile(2048, COLOR_2048, WHITE)
        case _:
            return Tile(0, COLOR_EMPTY, WHITE)
