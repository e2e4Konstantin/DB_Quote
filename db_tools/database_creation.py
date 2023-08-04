import sqlite3
import os

from db_tools.db_queries import db_queries
from setting import check_db_file, get_full_file_name
from db_tools import GripDB


def creation_database(db_file_name: str, path_db_file_name: str = "") -> None:
    db = GripDB(check_db_file(db_file_name, path_db_file_name))
    try:
        with db as cursor:
            result = cursor.execute(db_queries.get("CREATE_TABLE_PHYSICAL_PROPERTIES", None))
            print(f"создана таблица физических. {result}")

            result = cursor.execute(db_queries.get("CREATE_TABLE_MEASUREMENT_UNITS", None))
            print(f"создана таблица единиц измерения. {result}")

            cursor.execute(db_queries.get("DROP_INDEX_MEASUREMENT_UNITS", None))
            result = cursor.execute(db_queries.get("CREATE_INDEX_MEASUREMENT_UNITS", None))
            print(f"создан индекс для единиц измерения. {result}")

        db.inform()
    except sqlite3.Error as err:
        db.close_db()
        print(f"ошибка БД Sqlite3: {err}")


def main():
    f = "test_db_open.db"
    creation_database(f)
    # os.remove(f) if get_full_file_name(f) else f""


if __name__ == "__main__":
    print(f"main -->> dir() ={[x for x in dir() if x[:2] != '__']}")
    main()
