import csv

import cv2
import numpy as np

from iter import IteratorInDir


def write_file_abs_rel(path: list[list[str]], file_path: str) -> list[list[str]]:
    """Download in file abs and rel path of file"""
    iterator = IteratorInDir(file_path)
    for val in iterator:
        path.append(["",""])
        path[iterator.counter-1][0] = str(val)
        path[iterator.counter-1][1] = str(file_path + "/" + iterator.filenames[iterator.counter-1])
    return path


def show_image_from_file(image: np.ndarray) -> None:
    "take a numpy.ndarray and show on screen image"
    cv2.imshow('image', image)  # отображение


def open_and_write(path_to_file: str, urls: list) -> None:
    """open and write in file"""
    with open(path_to_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(list(urls))
