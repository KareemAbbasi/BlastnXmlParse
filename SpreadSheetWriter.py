import xlwt
from xlwt import Workbook


class SpreadSheet:

    def __init__(self, results):
        self.results: dict = results
        self.wb: Workbook = Workbook()
        self.sheet = self.wb.add_sheet('Sheet 1')
        self.names = []
        self.file_names = []
        self.sheet_data = dict()
        self.get_names()
        self.create_new_dict()

    def get_names(self):
        names = set()

        for file in self.results.values():
            for file_result in file.keys():
                names.add(file_result)
        names = sorted(names)
        self.names = names
        return names

    def create_new_dict(self):

        new_dict = dict()
        for name in self.names:
            new_dict[name] = self.number_hit_repetitions(name)

        self.sheet_data = new_dict
        return new_dict

    def number_hit_repetitions(self, hit_name):
        values = dict()
        file_names = sorted(self.results.keys())
        self.file_names = file_names
        for file in file_names:
            if hit_name in self.results[file].keys():
                values[file] = self.results[file][hit_name]
            else:
                values[file] = 0

        return values

    def write_file_names(self):
        for i in range(1, len(self.file_names) + 1):
            style = xlwt.easyxf('font: bold 1; align: horiz center')
            style.alignment.wrap = 1

            self.sheet.write(0, i, self.file_names[i - 1], style)

    def write_hits(self):
        row = 0
        for hit in self.sheet_data.items():
            row += 1
            style = xlwt.easyxf('font: bold 1')
            self.sheet.write(row, 0, hit[0], style)
            for i in range(0, len(self.file_names)):
                self.sheet.write(row, i + 1, hit[1][self.file_names[i]])

    def save_workbook(self):
        self.wb.save('output.xls')
