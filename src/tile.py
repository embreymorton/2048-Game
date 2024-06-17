from pydantic import BaseModel
from typing import Tuple
from constants import *

class Tile(BaseModel):
    """
    Represents a tile on the game board.

    Attributes:
        value (int): The value displayed on the tile.
        bg_color (tuple): The background color of the tile.
        text_color (tuple): The text color of the tile.
        merged (bool): A flag indicating whether the tile has been merged with another tile.
    """
    value: int
    bg_color: Tuple[int, int, int]
    text_color: Tuple[int, int, int]
    merged: bool = False

# Dictionary of Tile Objects
tiles = {
    0: Tile(value=0, bg_color=COLOR_EMPTY, text_color=WHITE),
    2: Tile(value=2, bg_color=COLOR_2, text_color=BLACK),
    4: Tile(value=4, bg_color=COLOR_4, text_color=BLACK),
    8: Tile(value=8, bg_color=COLOR_8, text_color=WHITE),
    16: Tile(value=16, bg_color=COLOR_16, text_color=WHITE),
    32: Tile(value=32, bg_color=COLOR_32, text_color=WHITE),
    64: Tile(value=64, bg_color=COLOR_64, text_color=WHITE),
    128: Tile(value=128, bg_color=COLOR_128, text_color=WHITE),
    256: Tile(value=256, bg_color=COLOR_256, text_color=WHITE),
    512: Tile(value=512, bg_color=COLOR_512, text_color=WHITE),
    1024: Tile(value=1024, bg_color=COLOR_1024, text_color=WHITE),
    2048: Tile(value=2048, bg_color=COLOR_2048, text_color=WHITE)
}

def get_tile(value: int) -> Tile:
    """
    Create and return a Tile object based on the given value.

    Args:
        value (int): The value to assign to the Tile.

    Returns:
        Tile: A Tile object with the specified value and appropriate colors.
    """
    return tiles.get(value, Tile(value=0, bg_color=COLOR_EMPTY, text_color=WHITE))
