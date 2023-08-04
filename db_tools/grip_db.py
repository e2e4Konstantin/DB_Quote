import sqlite3


class GripDB:
    def __init__(self, db_file_name: str = None):
        self.db_file_name = db_file_name
        self.connect = None
        self.cursor = None

    def __enter__(self):
        self.connect_db()
        return self.cursor

    def __exit__(self, exception_type, exception_value, traceback):
        self.close_db()

    def __str__(self):
        return f"db name: {self.db_file_name}, connect: {bool(self.connect)}, cursor: {bool(self.cursor)}"

    def connect_db(self):
        try:
            self.connect = sqlite3.connect(self.db_file_name, check_same_thread=False)
            self.cursor = self.connect.cursor()
        except sqlite3.Error as err:
            if self.connect:
                self.connect.rollback()
            print(f"ошибка открытия БД Sqlite3: {err}")

    def close_db(self):
        if self.connect:
            self.connect.commit()
            self.cursor.close()
            self.connect.close()
            self.connect = None
            self.cursor = None

    def inform(self) -> None:
        if not self.connect:
            self.connect_db()
        else:
            if not self.cursor:
                try:
                    self.cursor = self.connect.cursor()
                except sqlite3.Error as err:
                    self.close_db()
                    print(f"ошибка открытия БД Sqlite3: {err}")
                    return None
        print("------------>>", self.cursor)
        self.cursor.execute('SELECT SQLITE_VERSION()')
        print(f"SQLite version: {self.cursor.fetchone()[0]}")
        print(f"connect.total_changes: {self.connect.total_changes}")

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for index, table_i in enumerate(tables):
            table_name = table_i[0]
            count = self.cursor.execute(f"SELECT COUNT(1) from {table_name}")
            print(f"\n{index + 1}. таблица: {table_name}, записей: {count.fetchone()[0]}")
            table_info = self.cursor.execute(f"PRAGMA table_info({table_name})")
            data = table_info.fetchall()
            print(f"поля таблицы: ")
            [print(f"\t{d}") for d in data]
        self.close_db()






