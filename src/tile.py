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


# Dictionary of Tile Objects
tiles = {
    0: Tile(0, COLOR_EMPTY, WHITE),
    2: Tile(2, COLOR_2, BLACK),
    4: Tile(4, COLOR_4, BLACK),
    8: Tile(8, COLOR_8, WHITE),
    16: Tile(16, COLOR_16, WHITE),
    32: Tile(32, COLOR_32, WHITE),
    64: Tile(64, COLOR_64, WHITE),
    128: Tile(128, COLOR_128, WHITE),
    256: Tile(256, COLOR_256, WHITE),
    512: Tile(512, COLOR_512, WHITE),
    1024: Tile(1024, COLOR_1024, WHITE),
    2048: Tile(2048, COLOR_2048, WHITE)
}

def get_tile(value):
    """
    Create and return a Tile object based on the given value.

    Args:
        value (int): The value to assign to the Tile.

    Returns:
        Tile: A Tile object with the specified value and appropriate colors.
    """
    return tiles.get(value, Tile(0, COLOR_EMPTY, WHITE))