import os


class IteratorInDir:
    """This class is move into the folder and print abs path of files in folder"""
    def __init__(self, folder_path):
        self.filenames = []
        self.fileabspaths = []
        self.counter = 0
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                self.filenames.append(file_name)
                self.fileabspaths.append(os.path.abspath(file_name))


    def __iter__(self):
        return self


    def __next__(self):
        if self.counter < len(self.fileabspaths):
            self.counter += 1
            return self.fileabspaths[self.counter - 1]
        else:
            raise StopIteration