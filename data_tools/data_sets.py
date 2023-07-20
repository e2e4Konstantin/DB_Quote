import os
import sys
import pandas

DEBUG_ON = False


class SourceData:
    def __init__(self, file_name, file_path, sheet_name):
        self.file_name = file_name
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.full_path = None
        self.df: pandas.DataFrame() = None
        self.row_max = 0
        self.column_max = 0
        self.column_number = {}
        self.get_full_name()
        self.get_data()
        self.column_number_generate()

    def get_full_name(self):
        fullpath = os.path.abspath(os.path.join(self.file_path, self.file_name))
        self.full_path = fullpath if os.path.exists(fullpath) else None
        if not self.full_path:
            print(f"--> Не найден фйл: '{self.file_name}' в папке: '{self.file_path}'")
            sys.exit()

    def get_data(self):
        try:
            if self.full_path:
                self.df = pandas.read_excel(self.full_path, sheet_name=self.sheet_name, header=None, dtype="object")
                if not self.df.empty:
                    self.row_max = self.df.shape[0]-1
                    self.column_max = self.df.shape[1]-1
                else:
                    raise TypeError(self.__class__)
        except Exception as err:
            print(f"\tget_data --> {err}")
            sys.exit()

    def __str__(self):
        return f"файл: {self.full_path}\nтаблица: {self.sheet_name}', строк: {self.row_max + 1}, столбцов: {self.column_max + 1}\n" \
               f"pandas.version: {pandas.__version__}"

    def column_number_generate(self):
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alphabet.extend([alphabet[0] + v for v in alphabet])
        lc_alphabet = list('abcdefghijklmnopqrstuvwxyz')
        lc_alphabet.extend([lc_alphabet[0] + v for v in lc_alphabet])
        self.column_number = {v: i for i, v in enumerate(alphabet)}
        self.column_number.update({v: i for i, v in enumerate(lc_alphabet)})

    def cell_value(self, row, column) -> any:
        if row >= 0 and column >= 0:
            value = self.df.iat[row, column]
            if pandas.isna(value):
                return None
            return value
        return None


