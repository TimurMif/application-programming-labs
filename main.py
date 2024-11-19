import csv
import argparse

import pandas.core.frame
import pandas as pd
import cv2

from operation_data import image_height
from operation_data import image_chanel
from operation_data import filter_size_table
from operation_data import sort_square_table
from operation_data import static_info
from operation_data import image_width
from histogram import create_show_histogram
import writeinfile
import icrawlerdo

def open_and_write(path_to_file: str, urls: list) -> None:
    """open and write in file"""
    with open(path_to_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(list(urls))


def addition_for_table(table: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
    '''Addition in table three columns with data'''
    heights = []
    widths = []
    channels = []
    squares = []
    for i in range(0, table.shape[0]):
        image = cv2.imread(str(table.iat[i, 1]))
        heights.append(image_height(image))
        widths.append(image_width(image))
        channels.append(image_chanel(image))
        squares.append(image_width(image) * image_height(image))

    table["Высота изображения"] = heights
    table["Ширина изображения"] = widths
    table["Глубина изображения"] = channels
    table["Площадь изображения"] = squares
    return table


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest="keyword", type=str)
    parser.add_argument("-p", dest="path", type=str)
    parser.add_argument("-s", dest="save", type=str)
    args = parser.parse_args()

    all_path = [
        ["Абсолютный путь (ПК)", "Относительный путь (ПК)"],
    ]
    icrawlerdo.icrawler(args.keyword, args.path)
    all_path = writeinfile.write_file_abs_rel(all_path, args.path)
    open_and_write(args.save, all_path)

    df = pd.read_csv("data.csv")

    print("\n|1 ПУНКТ|\n")
    print(df.head(df.shape[0]))

    df = df.rename(columns={'Абсолютный путь (ПК)' : 'Абс. путь', 'Относительный путь (ПК)' : 'Отн. путь'})
    print("\n|2 ПУНКТ|\n")
    print(df.head(df.shape[0]))

    print("\n|3,6 ПУНКТ|\n")
    df = addition_for_table(df)
    print(df.head(df.shape[0]))

    print("\n|4 ПУНКТ|\n")
    table = static_info(df)
    print(table.head(table.shape[0]))

    print("\n|5 ПУНКТ|\n")
    print(filter_size_table(df, 2600, 2000))

    print("\n|7 ПУНКТ|\n")
    print(sort_square_table(df, True))

    create_show_histogram(df)


if __name__ == "__main__":
    main()