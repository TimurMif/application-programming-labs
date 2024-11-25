import os


class IteratorInDir:
    """This class is move into the folder and print abs path of files in folder"""
    def __init__(self, folder_path):
        self.filenames = []
        self.fileabspaths = []
        self.counter = -1
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                print(file_name)
                self.filenames.append(file_name)
                # self.fileabspaths.append(os.path.abspath(file_name))
                self.fileabspaths.append(str(folder_path + "/" + file_name))
    def __iter__(self):
        return self

    def before(self):
        if self.counter > 0:
            self.counter -= 1
            return self.fileabspaths[self.counter]
        else:
            self.counter = len(self.fileabspaths) - 1
            return self.fileabspaths[self.counter]

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.fileabspaths):
            return self.fileabspaths[self.counter]
        else:
            self.counter = 0
            return self.fileabspaths[self.counter]