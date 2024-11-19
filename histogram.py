from typing import Tuple, Any

import matplotlib.pyplot as plt
import numpy
import numpy as np
from numpy import ndarray, dtype, floating

from graph_image import graph_histogram


def show_histogram(x: numpy.ndarray, y: list) -> None:
    plt.figure(figsize=(10, 5))
    plt.feel_between(x, y, label='График кол-ва пикселей от уровня яркости', color='red')
    plt.plot(x, y, label='График кол-ва пикселей от уровня яркости', color='red')
    plt.title('Гистограмма изображения')
    plt.xlabel('Градация яркости')
    plt.ylabel('Кол-во пикселей каждого уровня яркости')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()

    plt.show()


def create_histogram(image: np.ndarray) -> tuple[ndarray[Any, dtype[floating[Any]]], list]:
    """Create histogram with function graph_histogram and with library matplotlib"""
    x = np.linspace(0, 255, 255)
    y = graph_histogram(x, image)
    return x, y


def create_show_histogram(image: np.ndarray):
    x, y = create_histogram(image)
    show_histogram(x, y)
