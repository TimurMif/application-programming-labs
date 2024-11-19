import numpy as np
import pandas.core.frame

import pandas as pd


def image_width(image: np.ndarray) -> int:
    height, width, channels = image.shape
    return width


def image_height(image: np.ndarray) -> int:
    height, width, channels = image.shape
    return height


def image_chanel(image: np.ndarray) -> int:
    height, width, channels = image.shape
    return channels


def filter_size_table(table: pandas.core.frame.DataFrame, max_width: int, max_height: int) -> pandas.core.frame.DataFrame:
    records = []
    for row in range(0, table.shape[0]):
            if int(table.iat[row, table.columns.get_loc("Высота изображения")]) <= max_height and int(table.iat[row, table.columns.get_loc("Ширина изображения")]) <= max_width:
                record = []
                for i in range(0, table.shape[1]):
                    record.append(table.iat[row,i])
                records.append(record)
    df = pd.DataFrame(records)
    return df


def sort_square_table(table: pandas.core.frame.DataFrame, up_down: bool) -> pandas.core.frame.DataFrame:
    return table.sort_values(by="Площадь изображения", ascending= up_down)


def static_info(table: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
    mid_width = table["Высота изображения"].mean()
    mid_height = table["Ширина изображения"].mean()
    mid_chanel = table["Глубина изображения"].mean()
    mid_square = table["Площадь изображения"].mean()

    max_width = table["Высота изображения"].max()
    max_height = table["Ширина изображения"].max()
    max_chanel = table["Глубина изображения"].max()
    max_square = table["Площадь изображения"].max()

    min_width = table["Высота изображения"].min()
    min_height = table["Ширина изображения"].min()
    min_chanel = table["Глубина изображения"].min()
    min_square = table["Площадь изображения"].min()

    return pd.DataFrame({ 'Значение' : ["Высота изображения", "Ширина изображения", "Глубина изображения", "Площадь изображения"], 'Среднее' : [mid_height, mid_width, mid_chanel, mid_square], 'Максимальное' : [max_height, max_width, max_chanel, max_square], 'Минимальное' : [min_height, min_width, min_chanel, min_square]})
