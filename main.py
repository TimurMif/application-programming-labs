import os
import argparse

import cv2

from histogram import create_show_histogram
from oper_image import resize_image
from oper_image import image_height
from oper_image import image_width
from oper_image import show_image
from oper_image import load_in_file


def take_from_con() -> tuple[str, str, int, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest="pathim", type=str)
    parser.add_argument("-s", dest="pathsv", type=str)
    parser.add_argument("-w", dest="width", type=int)
    parser.add_argument("-i", dest="height", type=int)
    args = parser.parse_args()
    return (args.pathim, args.pathsv, args.width, args.height)


def main():
    pathim, pathsv, width, height = take_from_con()

    try:
        image = cv2.imread(pathim)
        create_show_histogram(image)
        show_image(image)
        print("Ширина изображения: ", image_width(image))
        print("Высота изображения: ", image_height(image))
        resized_image = resize_image(image, int(width), int(height))
        show_image(resized_image)
        os.makedirs(pathsv, exist_ok=True)
        load_in_file(image, str(pathsv + '/new_image.jpg'))
        load_in_file(resized_image, str(pathsv + '/resize_image.jpg'))
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()


