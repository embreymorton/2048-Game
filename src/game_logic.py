import random
from tile import get_tile


def shift_tiles(tiles, direction):
    """
    Shift the tiles in the specified direction.

    Args:
        tiles (list of lists): The 2D grid representing the game board.
        direction (int): An integer representing the direction of the shift.
            1: Shift tiles upwards
            2: Shift tiles downwards
            3: Shift tiles left
            4: Shift tiles right

    Returns:
        None: Modifies the 'tiles' list

    """

    def reset_merges():
        """
        Set value of 'merged' to False for each tile.

        Returns:
            None: Modifies tiles
        """
        for tup in tiles:
            for tile in tup:
                tile.merged = False

    def rotate_90_degrees_clockwise(board):
        """
        Rotate a 2D board 90 degrees clockwise.

        Args:
            board (list of lists): The 2D board to be rotated.

        Returns:
            list of lists: The rotated board.
        """
        n = len(board)
        rotated_board = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated_board[i][j] = board[n - 1 - j][i]

        return rotated_board

    def rotate_180_degrees_clockwise(board):
        """
        Rotate a 2D board 180 degrees clockwise.

        Args:
            board (list of lists): The 2D board to be rotated.

        Returns:
            list of lists: The rotated board.
        """
        return rotate_90_degrees_clockwise(rotate_90_degrees_clockwise(board))

    def rotate_270_degrees_clockwise(board):
        """
        Rotate a 2D board 270 degrees clockwise.

        Args:
            board (list of lists): The 2D board to be rotated.

        Returns:
            list of lists: The rotated board.
        """
        return rotate_90_degrees_clockwise(rotate_180_degrees_clockwise(board))

    shifted = False

    def shift_left(tup):
        """
        Shifts tiles to the left in a row, merging tiles whenever possible.

        Args:
            tup (list of Tile): The list of Tile objects representing a row.

        Returns:
            None

        This function shifts the tiles to the left within a row or column represented by the input 'tup'.
        It checks for matching adjacent tiles and merges them if their values are equal.
        The 'score_counter' is updated based on the merged tiles.
        The 'shifted' flag is set to True if any tile movement occurs.
        """
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

    # Can shift up, down, and right using shift_left by rotating the game board
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
    """
        Generate a starting 4x4 grid with two random tiles (either 2 or 4) placed on the board.

    Returns:
        list of lists of Tile: A 2D array representing the initial game grid.
    """
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
    """
    Get the current score of the game.

    Returns:
        int: The current score.
    """
    return score_counter


def reset_grid():
    """
    Sets the current score of the game to zero and resets the game board to a new initial state.

    Returns:
        None:
    """
    global grid
    global score_counter
    grid = generate_grid()
    score_counter = 0


last_insert_x = None
last_insert_y = None


def insert_tile(tiles):
    """
    Inserts a new tile (either 2 or 4) into the grid at a different empty position than the last inserted tile.

    Args:
        tiles (list of lists): The 2D grid representing the game board.

    Returns:
        None:

    """
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
    """
    Get the current game board.
    Returns:
        list of lists of Tile: A 2D array representing the initial game grid.
    """
    return grid


def print_grid(tiles):
    """
    Prints the game board to the console.
    Args:
        tiles (list of lists): The 2D array to be printed.

    Returns:
        None:
    """
    for row in tiles:
        for tile in row:
            print(f"{tile.value:4}", end=" ")
        print()
    print()


def empty_tile_counter(tiles):
    """
    Counts how many empty tiles are on the game board.
    Args:
        tiles (list of lists): The 2D array to be checked.

    Returns:
        int: The number of empty tiles.
    """
    count = 0
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                count += 1
    return count


def full_grid(tiles):
    """
    Checks if the game board is full.

    Args:
        tiles (list of lists): The 2D array to be checked.

    Returns:
        boolean: True if the game board has zero empty tiles.
    """
    if empty_tile_counter(tiles) == 0:
        return True
    else:
        return False


def check_loss(tiles):
    """
    Checks to see if the game is lost by examining the game board.

    Args:
        tiles (list of lists of Tile): The 2D grid represending the game board.

    Returns:
        boolean: True if the game is lost, meaning the board is full and has zero mergeable tiles.
    """
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
    """
    Checks to see if the game is won by examining the game board.

    Args:
        tiles (list of lists of Tile): The 2D grid representing the game board.

    Returns:
        boolean: True if a tile with the value '2048' is present on the game board.

    """
    return any(any(tile.value == 2048 for tile in row) for row in tiles)
