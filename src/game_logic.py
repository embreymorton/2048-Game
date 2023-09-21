import random
from tile import get_tile


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
score_counter = 0


def get_score():
    return score_counter


def reset_grid():
    global grid
    global score_counter
    grid = generate_grid()
    score_counter = 0


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


def get_grid():
    return grid


def print_grid(tiles):
    for row in tiles:
        for tile in row:
            print(f"{tile.value:4}", end=" ")
        print()
    print()


def full_grid(tiles):
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                return False
    return True


def empty_tile_counter(tiles):
    count = 0
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                count += 1
    return count


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
