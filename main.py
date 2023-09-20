import os
import random
import sys
import pygame
from tile import *

ttf_path = os.path.join(sys.path[0], 'assets/Montserrat-Bold.ttf')

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

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

score_counter = 0
score_board_font = pygame.font.Font(ttf_path, 50)
score_board_text = score_board_font.render('{}'.format(score_counter), True, BLACK, COLOR_2)
score_board_rect = score_board_text.get_rect(center=(850, 100), size=(100, 100))
score_board_bg = pygame.Rect(750, 50, 200, 100)

reset_button_font = pygame.font.Font(ttf_path, 25)
reset_button_text = reset_button_font.render('NEW GAME', True, BLACK, COLOR_2)
reset_button_rect = reset_button_text.get_rect(center=(125, 100), size=(100, 100))
reset_button_bg = pygame.Rect(40, 75, 175, 50)


def generate_grid():
    x1 = random.randint(0, 3)
    y1 = random.randint(0, 3)
    x2 = random.randint(0, 3)
    y2 = random.randint(0, 3)

    while x1 == x2 and y1 == y2:
        x2 = random.randint(0, 3)
        y2 = random.randint(0, 3)

    generated_grid = []
    for i in range(4):
        row = []
        for j in range(4):
            if (j == x1 and i == y1) or (j == x2 and i == y2):
                row.append(get_tile(random.choices([2, 4], [0.8, 0.2])[0]))
            else:
                row.append(get_tile(0))
        generated_grid.append(row)

    return generated_grid


grid = generate_grid()


def reset_grid():
    global grid
    global score_counter
    global score_board_text
    global score_board_rect
    grid = generate_grid()
    score_counter = 0
    update_score_board()


def update_score_board():
    global score_board_text
    global score_board_rect
    score_board_text = score_board_font.render('{}'.format(score_counter), True, BLACK, COLOR_2)
    score_board_rect = score_board_text.get_rect(center=(850, 100), size=(100, 100))


def shift_tiles(tiles, direction):
    def reset_merges():
        for tup in tiles:
            for tile in tup:
                tile.merged = False

    def rotate_90_degrees_clockwise(board):
        n = len(board)
        rotated_board = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated_board[i][j] = board[n - 1 - j][i]

        return rotated_board

    def rotate_180_degrees_clockwise(board):
        return rotate_90_degrees_clockwise(rotate_90_degrees_clockwise(board))

    def rotate_270_degrees_clockwise(board):
        return rotate_90_degrees_clockwise(rotate_180_degrees_clockwise(board))

    shifted = False

    def shift_left(tup):
        global score_counter
        nonlocal shifted

        for i in range(1, 4):
            if tup[i].value == tup[i - 1].value and tup[i - 1].merged is not True and tup[i].merged is not True:
                tile_value_update = tup[i].value * 2
                tup[i - 1] = get_tile(tile_value_update)
                tup[i - 1].merged = True if tup[i - 1].value != 0 else False
                tup[i] = get_tile(0)
                score_counter += tile_value_update
                if tile_value_update != 0:
                    shifted = True
            elif tup[i - 1].value == 0:
                tup[i - 1] = get_tile(tup[i].value)
                if tup[i].value != 0:
                    shifted = True
                tup[i] = get_tile(0)
                shift_left(tup)

    match direction:
        case 1:
            tiles = rotate_270_degrees_clockwise(tiles)
            for row in tiles:
                shift_left(row)
            tiles = rotate_90_degrees_clockwise(tiles)
        case 2:
            tiles = rotate_90_degrees_clockwise(tiles)
            for row in tiles:
                shift_left(row)
            tiles = rotate_270_degrees_clockwise(tiles)
        case 3:
            for row in tiles:
                shift_left(row)
        case 4:
            tiles = rotate_180_degrees_clockwise(tiles)
            for row in tiles:
                shift_left(row)
            tiles = rotate_180_degrees_clockwise(tiles)
        case _:
            None

    global grid
    grid = tiles
    reset_merges()
    if not full_grid(grid) and shifted is True:
        insert_tile(grid)


def draw_tiles(tiles):
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


def empty_tile_counter(tiles):
    count = 0
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                count += 1
    return count


last_insert_x = None
last_insert_y = None


def insert_tile(tiles):
    global last_insert_x
    global last_insert_y

    num_x = random.randint(0, 3)
    num_y = random.randint(0, 3)
    while tiles[num_y][num_x].value != 0:
        num_x = random.randint(0, 3)
        num_y = random.randint(0, 3)

    if last_insert_x != num_x or last_insert_y != num_y or empty_tile_counter(tiles) == 1:
        tiles[num_y][num_x] = get_tile(random.choices([2, 4], [0.8, 0.2])[0])
        last_insert_x = num_x
        last_insert_y = num_y
    else:
        insert_tile(tiles)


def print_grid(tiles):
    for row in tiles:
        for tile in row:
            print(f"{tile.value:4}", end=" ")  # Adjust the width as needed
        print()  # Move to the next row


def full_grid(tiles):
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                return False
    return True


# needs work
def check_loss(tiles):
    if not full_grid(tiles):
        return False

    # Check for mergeable tiles horizontally
    for row in tiles:
        for i in range(len(row) - 1):
            if row[i].value == row[i + 1].value:
                return False

    # Check for mergeable tiles vertically
    for col in range(len(tiles[0])):
        for i in range(len(tiles) - 1):
            if tiles[i][col].value == tiles[i + 1][col].value:
                return False

    # If no empty tiles and no mergeable tiles, the game is lost
    return True


def check_win(tiles):
    if any(any(tile.value == 2048 for tile in row) for row in tiles):
        return True
    else:
        return False


key_pressed = False
run = True
while run:
    screen.fill(COLOR_EMPTY)
    pygame.draw.rect(screen, COLOR_2, score_board_bg)
    pygame.draw.rect(screen, BACKGROUND_COLOR, score_board_bg, 10)
    screen.blit(score_board_text, score_board_rect)
    pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(200, 200, 625, 625))
    draw_tiles(grid)

    screen.blit(header_text, header_rect)

    pygame.draw.rect(screen, COLOR_2, reset_button_bg)
    screen.blit(reset_button_text, reset_button_rect)
    pygame.draw.rect(screen, BACKGROUND_COLOR, reset_button_bg, 5)

    if check_win(grid):
        screen.blit(victory_text, victory_rect)

    if check_loss(grid):
        screen.blit(game_over_text, game_over_rect)

    key = pygame.key.get_pressed()
    if (key[pygame.K_UP] or key[pygame.K_w]) and not key_pressed:
        shift_tiles(grid, 1)
        update_score_board()
        print_grid(grid)
        print()
        key_pressed = True
    elif (key[pygame.K_DOWN] or key[pygame.K_s]) and not key_pressed:
        shift_tiles(grid, 2)
        update_score_board()
        print_grid(grid)
        print()
        key_pressed = True
    elif (key[pygame.K_LEFT] or key[pygame.K_a]) and not key_pressed:
        shift_tiles(grid, 3)
        update_score_board()
        print_grid(grid)
        print()
        key_pressed = True
    elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and not key_pressed:
        shift_tiles(grid, 4)
        update_score_board()
        print_grid(grid)
        print()
        key_pressed = True

    if not any(key):
        key_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 185 and 75 <= mouse[1] <= 125:
                reset_grid()

    mouse = pygame.mouse.get_pos()
    if 40 <= mouse[0] <= 215 and 75 <= mouse[1] <= 125:
        pygame.draw.rect(screen, GREY, reset_button_bg)
        screen.blit(reset_button_font.render('NEW GAME', True, BLACK, GREY), reset_button_rect)
        pygame.draw.rect(screen, BACKGROUND_COLOR, reset_button_bg, 5)

    pygame.display.update()

pygame.quit()

test = 'test'
