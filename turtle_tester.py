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


def line(xy_f:tuple[int, int, int, int],
         wth:int,
         col:tuple[int, int, int]) -> None:

    x_s, y_s, x_e, y_e = xy_f[0], xy_f[1], xy_f[2], xy_f[3]

    pygame.draw.line(screen, col, (x_s, y_s), (x_e, y_e), wth)

move_data = im()
screen.fill((255, 255, 255))
n = 0
# Game loop.
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.

    # Draw
    try:
        t, xy, c, w = move_data[str(n)]
        print(t, xy, c, w)
        if t == "l":
            line(xy, w, c)

            # add draw object ex: circles, ...
        else:
            print("ERROR: unsupported draw object")
        n+=1
    except KeyError:
        pass
    pygame.display.flip()
    fpsClock.tick(fps)

