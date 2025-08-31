import cv2

class Inputs:
    img = cv2.imread("input_img3.jpg", cv2.IMREAD_GRAYSCALE)

    pixel_dist  = 10 # not used now
    evolution   = 10000
    max_line_w  = 400
    lines_p_evo = 4
    color_sep   = 10

    shapes = ["l", "c"]

    opacity_1_pc = 0.5

    w = img.shape[1]
    h = img.shape[0]
