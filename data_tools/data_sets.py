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
        self.get_full_name()
        self.get_data()

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




