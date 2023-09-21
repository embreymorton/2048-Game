import os
import sys

# Colors
BACKGROUND_COLOR = (187, 173, 159)
COLOR_EMPTY = (203, 193, 178)
COLOR_2 = (238, 227, 217)
COLOR_4 = (237, 224, 200)
COLOR_8 = (242, 177, 121)
COLOR_16 = (245, 149, 99)
COLOR_32 = (246, 124, 95)
COLOR_64 = (246, 94, 59)
COLOR_128 = (237, 207, 114)
COLOR_256 = (237, 204, 97)
COLOR_512 = (237, 200, 80)
COLOR_1024 = (237, 197, 63)
COLOR_2048 = (237, 194, 46)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)

# Dimensions of game screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Path to font used
ttf_path = os.path.join(sys.path[0], '../assets/Montserrat-Bold.ttf')