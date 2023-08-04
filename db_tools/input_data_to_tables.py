import sqlite3
import os

from db_tools.db_queries import db_queries
from setting import physical_properties_data, measurement_units, check_db_file, get_full_file_name
from db_tools import GripDB


def insert_item(cur: sqlite3.Cursor, sql_instruction: str, data: tuple=None) -> int | None:
    instruction = db_queries.get(sql_instruction, None)
    if instruction:
        try:
            cur.execute(db_queries.get(sql_instruction, None), data)
            row = cur.fetchone()
            row = row or None
            print(f"запись: {data} записана в БД. id: {row}")
            return row[0]
        except sqlite3.Error as err:
            print(f"insert_item >> ошибка записи {data} в БД Sqlite3: {err}")
    else:
        print(f"insert_item >> не найдено такой sql инструкции {sql_instruction}")


def enter_unit_measure(file_name: str = "") -> None:
    db_control = GripDB(check_db_file(file_name))
    with db_control as cursor:
        for physical_property in physical_properties_data:
            idp = insert_item(cursor, "INSERT_PHYSICAL_PROPERTIES", physical_property)
            print(f"{idp}")
    db_control.inform()


def delete_all_data_from_unit_measure(file_name: str = "") -> None:
    db_control = GripDB(check_db_file(file_name))
    with db_control as cursor:
        cursor.execute(db_queries.get("DELETE_DATA_FROM_PHYSICAL_PROPERTIES", None))
    db_control.inform()


def enter_measurement_units(file_name: str = "") -> None:
    db_control = GripDB(check_db_file(file_name))
    with db_control as cursor:
        for units in measurement_units:
            idp = insert_item(cursor, "INSERT_MEASUREMENT_UNITS", units)
            print(f"{idp}")
    db_control.inform()



if __name__ == "__main__":
    f = "test_db_open.db"
    # delete_all_data_from_unit_measure(f)
    # enter_unit_measure(f)

    # instruction = """DELETE FROM tblPhysicalProperties WHERE name_rus = 'масса';"""
    # idp = insert_item(db.cursor, "INSERT_PHYSICAL_PROPERTIES", ('масса', 'mass', 'n'))
    # print(f"{idp}")

    enter_measurement_units(f)











