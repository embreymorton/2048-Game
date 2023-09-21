from game_logic import get_grid, shift_tiles, check_win, check_loss, reset_grid, print_grid, get_score
from display import *

key_pressed = False
run = True
while run:
    grid = get_grid()
    screen.fill(COLOR_EMPTY)
    pygame.draw.rect(screen, COLOR_2, score_board_bg)
    pygame.draw.rect(screen, BACKGROUND_COLOR, score_board_bg, 10)
    screen.blit(update_score_board(get_score())[0], update_score_board(get_score())[1])
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
        # print_grid(grid)
        key_pressed = True
    elif (key[pygame.K_DOWN] or key[pygame.K_s]) and not key_pressed:
        shift_tiles(grid, 2)
        # print_grid(grid)
        key_pressed = True
    elif (key[pygame.K_LEFT] or key[pygame.K_a]) and not key_pressed:
        shift_tiles(grid, 3)
        # print_grid(grid)
        key_pressed = True
    elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and not key_pressed:
        shift_tiles(grid, 4)
        # print_grid(grid)
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
