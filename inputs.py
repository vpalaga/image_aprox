import cv2

class Inputs:
    img = cv2.imread("input_img.jpg", cv2.IMREAD_GRAYSCALE)

    pixel_distance = 10 # not used now
    evolution = 1000
    max_line_w = 500
    lines_p_evo = 2
    color_sep = 50

    opacity_1_pc = 0.3

    w = img.shape[1]
    h = img.shape[0]
