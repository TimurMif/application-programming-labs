from typing import Tuple, Any

import matplotlib.pyplot as plt
import numpy
import numpy as np
from numpy import ndarray, dtype, floating
import pandas

from graph_image import graph_histogram


def show_histogram(x: numpy.ndarray, y: list) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='График распределения площади', color='blue')
    plt.title('Грифик площади от строки таблицы')
    plt.xlabel('Индекс в таблице')
    plt.ylabel('Величина площади')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


def create_histogram(table: pandas.core.frame.DataFrame) -> tuple[ndarray[Any, dtype[floating[Any]]], list]:
    """Create histogram with function graph_histogram and with library matplotlib"""
    x = np.linspace(0, table.shape[0]-1, table.shape[0])
    y = graph_histogram(table)
    return x, y


def create_show_histogram(table: pandas.core.frame.DataFrame) -> None:
    x, y = create_histogram(table)
    show_histogram(x, y)
