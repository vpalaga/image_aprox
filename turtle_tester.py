import sys, json, os

import pygame
from pygame.locals import *

from inputs import Inputs


def im():
    # Path where exe (or script) lives
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "moves.json")

    with open(file_path, "r") as f:
        data = json.load(f)
    return data


pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = Inputs.w, Inputs.h
screen = pygame.display.set_mode((width, height))


def gray_colour(flt: float) -> tuple[int, int, int]:
    val = round(flt * 255)
    #print(f"val: {val}")
    return val, val, val


def line(xy:tuple[int, int, int, int], wth:int, col:float) -> None:
    x_s, y_s, x_e, y_e = xy[0], xy[1], xy[2], xy[3]
    pygame.draw.line(screen, gray_colour(col), (x_s, y_s), (x_e, y_e), wth)

move_data = im()


# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.

    # Draw.

    pygame.display.flip()
    fpsClock.tick(fps)

