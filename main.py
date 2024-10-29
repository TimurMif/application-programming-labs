import argparse
import csv

import writeinfile
import icrawlerdo


def open_and_write(path_to_file: str, urls: list):
    """open and write in file"""
    with open(path_to_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(list(urls))


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


if __name__ == "__main__":
    main()