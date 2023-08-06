import sqlite3
import os

from db_tools.db_queries import db_queries
from setting import physical_properties_data, measurement_units, check_db_file, get_full_file_name, console_colors
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
            print(f"insert_item >> ошибка записи {data} в БД Sqlite3: {console_colors['RED']}{err}{console_colors['RESET']}")
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
    db = GripDB(check_db_file(file_name))
    with db as cur:
        for units in measurement_units:
            id_physical_property = get_id_physical_property(cur, units[-1])
            idp = insert_item(cur, "INSERT_MEASUREMENT_UNITS", units[:-1]+(id_physical_property,))
            print(f"{idp}")
    db.inform()


def get_id_physical_property(cur: sqlite3.Cursor, name_rus: str) -> int | None:
    """ получает из БД id физического свойства с именем nam_rus """
    sql_instruction = db_queries.get("GET_ID_PHYSICAL_PROPERTY", None)
    if sql_instruction and name_rus:
        try:
            cur.execute(sql_instruction, (name_rus, ))
            id_pp = cur.fetchone()
            id_pp = id_pp or None
            print(f"название: '{name_rus}' найдено в БД. id: {id_pp}")
            return id_pp[0]
        except sqlite3.Error as err:
            print(f"get_id_physical_property >> запись {name_rus = } в БД не найдена: {err}")
    else:
        print(f"get_id_physical_property >> не найдено такой sql инструкции {sql_instruction} или пустое название: {name_rus}")


if __name__ == "__main__":
    f = "test_db_open.db"
    # delete_all_data_from_unit_measure(f)
    # enter_unit_measure(f)

    # instruction = """DELETE FROM tblPhysicalProperties WHERE name_rus = 'масса';"""
    # idp = insert_item(db.cursor, "INSERT_PHYSICAL_PROPERTIES", ('масса', 'mass', 'n'))
    # print(f"{idp}")
    #
    # db_control = GripDB(check_db_file(f))
    # with db_control as cursor:
    #
    #     print(id)
    #     sql = db_queries.get("INSERT_MEASUREMENT_UNITS", None)
    #     print(sql)
    #     d = next(iter(measurement_units))
    #     print(d)
    #     id = get_id_physical_property(cursor, d[-1])
    #     dm = d[:-1]+(id,)
    #     print(dm)
    #
    #     # sql = """INSERT INTO tblMeasurementUnits (name_rus, name_eng, short_name_rus, short_name_eng, basis, multiplier, FK_tblPhysicalProperties_tblMeasurementUnits) VALUES (?, ?, ?, ?, ?, ?, ?);"""
    #     cursor.execute(sql, dm)
    #     id = cursor.fetchone()
    #     print(id)

    enter_measurement_units(f)











