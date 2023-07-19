import sqlite3
from .db_queries import db_queries


def quote_write(src_quote: Quote, db_cursor: sqlite3.Cursor, db_connect: sqlite3.Connection) -> int | None:
    if src_quote and db_cursor:
        # print(src_quote)
        try:
            db_cursor.execute(db_queries.get('INSERT_QUOTE', None),
                              (src_quote.cod, src_quote.name, src_quote.sizer,
                               src_quote.related_quotes[0], src_quote.related_quotes[1], src_quote.table_cod))
            row = db_cursor.fetchone()
            (id_in,) = row if row else None
            # print(f"расценка: {src_quote.cod} записана в БД. {row=} id: {id_in}")
            db_connect.commit()
            return id_in
        except sqlite3.Error as err:
            print(f"ошибка записи в БД Sqlite3: {err}, quote_write >> расценка: {src_quote.cod} {src_quote.name}")
    return None



def write_tables_to_db(db_file_name):
    connect = None
    cursor = None
    print(f"БД: {db_file_name}, таблиц для загрузки: {len(tables)}")
    try:
        connect = sqlite3.connect(db_file_name, check_same_thread=False)
        cursor = connect.cursor()
        cursor.execute('SELECT SQLITE_VERSION()')
        print(f"db name: {db_file_name}, connect: {connect}, cursor: {cursor}\nSQLite version: {cursor.fetchone()[0]}")

        result = cursor.execute(db_queries.get('CREATE_TABLE_QUOTE', None))
        print(f"создана таблица расценок. {result}")
        result = cursor.execute(db_queries.get('CREATE_TABLE_ATTRIBUTE_VALUE', None))
        print(f"создана таблица значений атрибутов. {result}")
        result = cursor.execute(db_queries.get('CREATE_TABLE_SET_ATTRIBUTE', None))
        print(f"создана таблица наборов атрибутов. {result}")


        quotes_count = 0
        for quote_i in quotes:
            row_id = quote_write(quote_i, cursor, connect)
            if row_id:
                print(f"записана расценка id:{row_id} {quote_i.cod}")
                quotes_count += 1
                list_attribute_id = []
                # записываем атрибуты в AttributeValue
                for x in quote_i.attributes_value:
                    attr_row_id = write_attributes_to_value_table((x.name, x.value), cursor, connect)

                    # записываем связь в SetAttribute
                    id_link = write_set_attribute(row_id, (x.name, x.value), cursor, connect)

        print(f"{quotes_count} расценок записано в БД")

    except sqlite3.Error as err:
        if connect:
            connect.rollback()
        print(f"ошибка открытия БД Sqlite3: {err}")
    else:
        connect.commit()
        cursor.close()
        connect.close()
        print(f"БД закрыта корректно.")
