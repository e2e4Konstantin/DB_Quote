import sqlite3
from .db_queries import db_queries


def create_database_table(query: str, db_cursor: sqlite3.Cursor) -> bool | None:
    if query:
        table_name = query.split("_")[-1].lower().capitalize()
        try:
            db_cursor.execute(db_queries.get(query, None))
            print(f"создана таблица: {table_name}.")
        except sqlite3.Error as err:
            print(f"ошибка создания таблицы: {table_name},\n{err}")
            return False
    return None


def build_tables(db_cursor: sqlite3.Cursor) -> bool:
    requests = ["CREATE_TABLE_QUOTES", "CREATE_TABLE_VALUE-DIMENSIONS",
                "CREATE_TABLE_DIMENSIONS", "CREATE_TABLE_DIMENSIONS-SET"]
    results = set()
    for request in requests:
        results.add(create_database_table(request, db_cursor))
    return all(results)


def write_quote(src_quote: tuple, db_cursor: sqlite3.Cursor) -> int | None:
    if src_quote and db_cursor:
        # print(src_quote)
        try:
            db_cursor.execute(db_queries.get("INSERT_QUOTES", None), src_quote)
            row = db_cursor.fetchone()
            (id_in,) = row if row else None
            # print(f"расценка: {src_quote[0]} записана в БД. {row=} id: {id_in}")
            # db_connect.commit()
            return id_in
        except sqlite3.Error as err:
            print(f"ошибка записи в БД: {err}, write_quote >> расценка: {src_quote[0]} {src_quote[1]} не записана.")
    return None
