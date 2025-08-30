from PIL import ImageDraw, Image
from inputs import Inputs
import randomnes_handler

def make_img(old, n, line_cof):
    new_img_f = old.copy()

    lines_layer = Image.new("RGBA", old.size, (0, 0, 0, 0))

    move_data_func = {}

    for line_nr in range(Inputs.lines_p_evo):
        w, c = randomnes_handler.r_val(n, line_cof) # select line values
        xy = randomnes_handler.r_p()
        t = "l"

        move_data_func[line_nr] = (t, xy, c, w) # save line data

        #  make a temporary layer for each line so they can be combined and overlapped
        temp = Image.new("RGBA", old.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(temp)

        draw.line(xy, fill=c, width=w) # draw a random line

        lines_layer = Image.alpha_composite(lines_layer, temp)

    # overlap lines with background
    new_img_f = Image.alpha_composite(new_img_f, lines_layer)

    return new_img_f, move_data_func

if __name__ == "__main__":
    img = Image.new("RGBA", (500, 500), (255, 255, 255, 255))

    img, _ = make_img(img, 100)
    img.show()
