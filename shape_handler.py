from PIL import ImageDraw
import random
from inputs import Inputs


def gray_colour(flt: float, op=0.1) -> tuple[int, int, int, int]:
    val = round(flt * 255)
    opacity = round(op*255)
    #print(f"val: {val}")
    return val, val, val, opacity


def r_val(n) -> tuple[int, tuple[int, int, int, int]]:
    choose_col_modus = random.randint(0, Inputs.color_sep) # have a chance for pure white or black
    if choose_col_modus <= 0:
        c = gray_colour(0)

    elif choose_col_modus >= Inputs.color_sep:
        c = gray_colour(1)

    else:
        c = gray_colour(1 / choose_col_modus)

    a = round(Inputs.max_line_w - n - 100)
    if a < 0:
        a = 0
    b = round(Inputs.max_line_w - n)

    w = random.randint(a, b)
    #print(a, b)
    return w, c


def r_p():

    return (random.randint(0, Inputs.w),
            random.randint(0, Inputs.h),
            random.randint(0, Inputs.w),
            random.randint(0, Inputs.h),
            )


def make_img(old, n):
    new_img_f = old.copy()
    draw = ImageDraw.Draw(new_img_f, "RGBA")

    move_data_func = {}

    for line_nr in range(Inputs.lines_p_evo):
        w, c = r_val(n)
        xy = r_p()

        t = "l"
        move_data_func[line_nr] = (t, xy, c, w)
        print(c)

        draw.line(xy, fill=c, width=w) # draw a random line

    return new_img_f, move_data_func
