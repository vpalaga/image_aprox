import cv2
from PIL import Image
import numpy as np
from tqdm import tqdm
import os, json

from image_comparator import compare as img_compare
from inputs import Inputs
from shape_handler import make_img


def export(data):
    with open("moves.json", "w") as f:
        json.dump(data, f, indent=4)  # indent=4 makes it pretty-printed

move_data = {}

line_with_conf = Inputs.max_line_w / Inputs.evolution

img = Image.new("RGB", (Inputs.w, Inputs.h), "white")

progress = tqdm(total=Inputs.evolution, desc="Progress:")

line_nr = 0

for _ in range(Inputs.evolution):

    new_img, part_move_dict = make_img(img, line_with_conf*_)

    cv_im_orig = cv2.cvtColor(np.array(img),     cv2.COLOR_RGB2GRAY)
    cv_im_new  = cv2.cvtColor(np.array(new_img), cv2.COLOR_RGB2GRAY)

    orig_comp = img_compare(Inputs.img, cv_im_orig)
    new_comp  = img_compare(Inputs.img, cv_im_new)

    if new_comp > orig_comp:
        #print(new_comp)

        img = new_img

        for key, val in part_move_dict.items():
            move_data[line_nr] = val
            line_nr += 1

    progress.update(1)

img.show()

export(move_data)

# save as int.png
outputs = os.listdir("./outputs/")
img_num = 0
for name in outputs:
    if int(name.strip(".png")) >= img_num:
        img_num = int(name.strip(".png"))

img.save(f"./outputs/{img_num}.png")