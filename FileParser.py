from os import listdir
from os.path import isfile, join
from XmlParser import *


class FilesParser:

    def __init__(self, path='files/'):
        self.file_path = path
        self.files = [f for f in listdir(self.file_path) if isfile(join(self.file_path, f))]

    def get_results(self):
        results = dict()
        for f in self.files:
            file_name = f.split('.')[0]
            file_parser = XmlParser('files/{}'.format(f))
            results[file_name] = file_parser.get_results()

        return results
