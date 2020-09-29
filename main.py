from FileParser import *
from SpreadSheetWriter import *
import argparse

import time
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Count hit defs in XML file')
    parser.add_argument('-p', '--path', help='The path of the directory containing the files')

    args = parser.parse_args()

    if args.path:
        f = FilesParser(args.path)
    else:
        f = FilesParser()

    r = f.get_results()

    s = SpreadSheet(r)
    s.write_file_names()
    s.write_hits()
    s.save_workbook()

    print('Done! Check the output.xls file :)')

