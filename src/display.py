import pygame
from tile import *
from game_logic import get_score

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2048")

header_font = pygame.font.Font(ttf_path, 150)
header_text = header_font.render('2048', True, BLACK, COLOR_EMPTY)
header_rect = header_text.get_rect(center=(500, 100), size=(200, 200))

game_over_font = pygame.font.Font(ttf_path, 100)
game_over_text = game_over_font.render('GAME OVER', True, BLACK, COLOR_EMPTY)
game_over_rect = game_over_text.get_rect(center=(515, 900), size=(150, 150))

victory_font = pygame.font.Font(ttf_path, 100)
victory_text = victory_font.render('YOU WIN!', True, BLACK, COLOR_EMPTY)
victory_rect = victory_text.get_rect(center=(500, 900), size=(150, 150))

score_board_font = pygame.font.Font(ttf_path, 50)
score_board_text = score_board_font.render('{}'.format(get_score()), True, BLACK, COLOR_2)
score_board_rect = score_board_text.get_rect(center=(850, 100), size=(100, 100))
score_board_bg = pygame.Rect(750, 50, 200, 100)

reset_button_font = pygame.font.Font(ttf_path, 25)
reset_button_text = reset_button_font.render('NEW GAME', True, BLACK, COLOR_2)
reset_button_rect = reset_button_text.get_rect(center=(125, 100), size=(100, 100))
reset_button_bg = pygame.Rect(40, 75, 175, 50)


def draw_tiles(tiles):
    """
    Displays the game board on the screen.

    Args:
        tiles (list of lists): The 2D grid representing the game board.

    Returns:
        None:

    """
    font = pygame.font.Font(ttf_path, 48)

    x_spacer = 225
    y_spacer = 225
    for tile_list in tiles:
        for tile in tile_list:
            text = font.render('{}'.format(tile.value) if tile.value != 0 else '', True, tile.text_color)
            tile_bg = pygame.Rect(x_spacer, y_spacer, 125, 125)
            pygame.draw.rect(screen, tile.bg_color, tile_bg)
            current_tile = text.get_rect(center=(x_spacer + 62.5, y_spacer + 57.5), size=(125, 125))
            screen.blit(text, current_tile)
            x_spacer += 150
        x_spacer = 225
        y_spacer += 150


def update_score_board(score):
    """
    Updates the game's score on the score board display.

    Args:
        score (int): The current game score.

    Returns:
        tuple: A tuple containing the updated score board text and its rectangle.
    """
    global score_board_text
    global score_board_rect
    score_board_text = score_board_font.render('{}'.format(score), True, BLACK, COLOR_2)
    score_board_rect = score_board_text.get_rect(center=(850, 100), size=(100, 100))
    return score_board_text, score_board_rect
