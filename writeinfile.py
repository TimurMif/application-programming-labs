from iter import IteratorInDir


def write_file_abs_rel(path: list[list[str]], file_path: str) -> list[list[str]]:
    """Download in file abs and rel path of file"""
    iterator = IteratorInDir(file_path)
    for val in iterator:
        path_line = ["", ""]
        path.append(path_line)
        path[iterator.counter][0] = str(val)
        path[iterator.counter][1] = str(file_path + "/" + iterator.filenames[iterator.counter-1])
    return path