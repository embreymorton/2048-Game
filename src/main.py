from game_logic import get_grid, shift_tiles, check_win, check_loss, reset_grid, print_grid
from display import *

key_pressed = False
run = True
while run:
    # Get the current game grid
    grid = get_grid()

    # Clear the screen
    screen.fill(COLOR_EMPTY)

    # Draw the score board background
    pygame.draw.rect(screen, COLOR_2, score_board_bg)
    pygame.draw.rect(screen, BACKGROUND_COLOR, score_board_bg, 10)

    # Update and display the score board text
    score_text, score_rect = update_score_board(get_score())
    screen.blit(score_text, score_rect)

    # Draw the game board background
    pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(200, 200, 625, 625))

    # Draw the tiles on the game board
    draw_tiles(grid)

    # Draw the header text
    screen.blit(header_text, header_rect)

    # Draw the reset button background
    pygame.draw.rect(screen, COLOR_2, reset_button_bg)
    screen.blit(reset_button_text, reset_button_rect)
    pygame.draw.rect(screen, BACKGROUND_COLOR, reset_button_bg, 5)

    # Check for game win and display victory text
    if check_win(grid):
        screen.blit(victory_text, victory_rect)

    # Check for game loss and display game over text
    if check_loss(grid):
        screen.blit(game_over_text, game_over_rect)

    # Check for key presses and update the grid accordingly
    key = pygame.key.get_pressed()
    if (key[pygame.K_UP] or key[pygame.K_w]) and not key_pressed:
        shift_tiles(grid, 1)
        key_pressed = True
    elif (key[pygame.K_DOWN] or key[pygame.K_s]) and not key_pressed:
        shift_tiles(grid, 2)
        key_pressed = True
    elif (key[pygame.K_LEFT] or key[pygame.K_a]) and not key_pressed:
        shift_tiles(grid, 3)
        key_pressed = True
    elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and not key_pressed:
        shift_tiles(grid, 4)
        key_pressed = True

    if not any(key):
        key_pressed = False

    # Check for quit events and reset button click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 185 and 75 <= mouse[1] <= 125:
                reset_grid()

    # Check mouse position for reset button highlight
    mouse = pygame.mouse.get_pos()
    if 40 <= mouse[0] <= 215 and 75 <= mouse[1] <= 125:
        pygame.draw.rect(screen, GREY, reset_button_bg)
        screen.blit(reset_button_font.render('NEW GAME', True, BLACK, GREY), reset_button_rect)
        pygame.draw.rect(screen, BACKGROUND_COLOR, reset_button_bg, 5)

    # Update the display
    pygame.display.update()

# Quit the game when the main loop exits
pygame.quit()
