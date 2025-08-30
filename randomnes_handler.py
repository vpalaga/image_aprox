import random
from inputs import Inputs


def gray_colour(flt: float, op: float) -> tuple[int, int, int, int]:
    val = round(flt * 255)
    opacity = round(op*255)
    #print(f"val: {val}")
    return val, val, val, opacity


def opac_r(n_f):
    max_o = -(n_f*(100/Inputs.evolution))+ 100 + Inputs.opacity_1_pc*100#

    if max_o > 100:
        max_o = 100

    min_o = max_o - (max_o / 2)

    return int(min_o), int(max_o)


def r_val(n, line_cof) -> tuple[int, tuple[int, int, int, int]]:
    #print(f"{n=}")
    a, b = opac_r(n)

    o = (random.randint(round(a), round(b))) / 100


    choose_col_modus = random.randint(0, Inputs.color_sep) # have a chance for pure white or black
    if choose_col_modus <= 0:
        c = gray_colour(0, o)

    elif choose_col_modus >= Inputs.color_sep:
        c = gray_colour(1, o)

    else:
        c = gray_colour(1 / choose_col_modus, o)


    a = round(Inputs.max_line_w - line_cof - 100)
    if a < 0:
        a = 0
    b = round(Inputs.max_line_w - line_cof)

    w = random.randint(a, b)

    #print(a, b)
    return w, c


def r_p():

    return (random.randint(0, Inputs.w),
            random.randint(0, Inputs.h),
            random.randint(0, Inputs.w),
            random.randint(0, Inputs.h),
            )

