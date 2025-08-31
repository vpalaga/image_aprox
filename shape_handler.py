from PIL import ImageDraw, Image
from inputs import Inputs
import randomnes_handler
import random


def make_img(old, n, line_cof):
    new_img_f = old.copy()

    lines_layer = Image.new("RGBA", old.size, (0, 0, 0, 0))

    move_data_func = {}

    for line_nr in range(Inputs.lines_p_evo):

        #  make a temporary layer for each line so they can be combined and overlapped
        temp = Image.new("RGBA", old.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(temp)

        t = random.choice(Inputs.shapes)
        w, c = randomnes_handler.r_val(n, line_cof)  # select random values

        if t == "l":
            xy = (randomnes_handler.r_p(), randomnes_handler.r_p())


            draw.line(xy, fill=c, width=w) # draw a random line


        elif t == "c":
            xy = randomnes_handler.r_p()
            draw.circle(xy, w, c)


        else: # so pycharm doesn't: Local variable 'xy' might be referenced before assignment
            xy = None

        move_data_func[line_nr] = (t, xy, c, w) # save line data

        lines_layer = Image.alpha_composite(lines_layer, temp) # overlay

    # overlap lines with background
    new_img_f = Image.alpha_composite(new_img_f, lines_layer)

    return new_img_f, move_data_func


if __name__ == "__main__":
    img = Image.new("RGBA", (500, 500), (255, 255, 255, 255))

    img, _ = make_img(img, 100, 0)
    img.show()
