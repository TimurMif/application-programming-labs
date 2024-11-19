import cv2
import numpy as np
from skimage.transform import resize


def show_image(image: np.ndarray) -> None:
    cv2.imshow('image', image)  # отображение
    cv2.waitKey(0)


def image_width(image: np.ndarray) -> int:
    height, width, channels = image.shape
    return width


def image_height(image: np.ndarray) -> int:
    height, width, channels = image.shape
    return height


def load_in_file(file: np.ndarray, path_to_file:str) -> bool:
    """Load image in file and return true if image was write in file or not"""
    file = file.astype(np.uint8)
    write_file = cv2.imwrite(path_to_file, file)
    if write_file:
        return True
    else:
        return False


def resize_image(file: np.ndarray, new_width:int, new_height: int) -> np.ndarray:
    "Resize image with skimage and return new image"
    new_image = resize(file, (new_height, new_width), anti_aliasing=True, preserve_range=True)
    return new_image.astype(np.uint8)
