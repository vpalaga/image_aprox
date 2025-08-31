import sys

import cv2
from PIL import Image
import numpy as np
from tqdm import tqdm
import os, json

from image_comparator import compare as img_compare
from inputs import Inputs
from shape_handler import make_img


def export(data, pth):
    with open(f"{pth}.json", "w") as f:
        json.dump(data, f, indent=5)  # indent=4 makes it pretty-printed


move_data = {}
acc_data  = {}

line_with_conf = Inputs.max_line_w / Inputs.evolution

img = Image.new("RGBA", (Inputs.w, Inputs.h), (255, 255, 255, 255))

progress = tqdm(total=Inputs.evolution, desc="Progress:")

n = None # so idea doesn't: Name 'n' can be undefined
line_nr = 0

for n in range(Inputs.evolution):

    new_img, part_move_dict = make_img(img, n, line_with_conf) # gen a new random image

    cv_im_orig = cv2.cvtColor(np.array(img),     cv2.COLOR_RGB2GRAY)  # get to readable format
    cv_im_new  = cv2.cvtColor(np.array(new_img), cv2.COLOR_RGB2GRAY)

    orig_comp = img_compare(Inputs.img, cv_im_orig) # compare the older image
    new_comp  = img_compare(Inputs.img, cv_im_new ) # compare the new random one

    if new_comp > orig_comp:

        img = new_img

        for key, val in part_move_dict.items():
            move_data[line_nr] = val
            line_nr += 1

    acc_data[n] = orig_comp # save acc data for analyse

    progress.update(1)

if n is not None:
    print(f"\n  accuracy: {round(acc_data[n], ndigits=2)}")
    print(f"with strokes: {len(move_data)}")

img.show()

export(move_data, "moves")
export(acc_data,  "acc")

# save as int.png
outputs = os.listdir("./outputs/")
img_num = 0
for name in outputs:
    if int(name.strip(".png")) >= img_num:
        img_num = int(name.strip(".png"))

img.save(f"./outputs/{img_num + 1}.png")

sys.exit()