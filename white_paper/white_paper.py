from importlib.resources import path
import os
import shutil
import argparse

import cv2
import numpy as np
from tqdm import tqdm


def is_color(image: np.ndarray, RGB: list):
    return (image == RGB).all()


def mv_colorpaper(
    RGB: list = [255, 255, 255],
    path_image: str = "./image",
    path_white: str = "./white",
):
    path_image = os.path.abspath(path_image)
    lst_images = os.listdir(path_image)

    for image_name in tqdm(lst_images):
        image = cv2.imread(os.path.join(path_image, image_name))

        if is_color(image, RGB):
            shutil.move(
                src=os.path.join(path_image, image_name),
                dst=os.path.join(path_white, image_name),
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--path_image")
    parser.add_argument("--path_white")
    args = parser.parse_args()

    RGB = [255, 255, 255]

    mv_colorpaper(
        RGB=RGB, 
        path_image=args.path_image,
        path_white=args.path_white
    )