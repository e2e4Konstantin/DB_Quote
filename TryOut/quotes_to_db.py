import re
from data_tools import SourceData

from db_tools import dbControl, build_tables, write_quote

paths = {
    "home": r"F:\Kazak\Google Диск\1_KK\Job_CNAC\Python_projects\DB_Quote\src_data",
    "office": r"C:\Users\kazak.ke\PycharmProjects\Quotes_Parsing\output",
}
source_files = {
    3: (r"template_3_68_output.xlsx", "Quote"),
    4: (r"template_4_68_output.xlsx", "Quote"),
    5: (r"template_5_67_output.xlsx", "Quote"),
}

fn = 5
pl = "office"  # "office" "home"
dset = (source_files[fn][0], paths[pl], source_files[fn][1])

# group, cod, name, item, metric

test_quote = [
    ("4.3-5-1-0-37", "4.3-37-1", "Монтаж балансира двухроликового подвесной кресельной канатной дороги", 1, "комплект"),
    ("4.6-3-1-0-35", "4.6-35-23",
     "Фильтр-регенератор для фисд с наружной регенерацией, высота фильтрующей загрузки 1,5 м, диаметр 1600 мм", 1, "т"),
]

data = SourceData(*dset)
print(data, "\n")
print(data.df.info(verbose=True))
print(f"непустых значений в столбце 'A': {data.df[data.df.columns[0]].count()}", "\n")

digit_pattern = re.compile(r"^\d+")


def get_just_digits(src_data: str, pattern) -> tuple[int, str]:
    src_data = src_data.strip()
    result = pattern.match(src_data)
    if result:
        number: int = int(src_data[result.span()[0]:result.span()[1]])
        text: str = src_data[result.span()[1]:].strip()
        return number, text
    return 0, src_data


def get_quote(row) -> tuple | None:
    result = list()
    for column_name in ["B", "C", "D", "E", "F", "H", "I"]:
        column = data.column_number.get(column_name, None)
        value = data.cell_value(row, column)
        if value:
            result.append(value)
        else:
            result.append(None)
    if None in result[:3]:                      # есть пустые значения в столбцах B, C, D
        print(f"плохая расценка: {result}")
        return None
    else:
        index_column_e = 3
        unit = get_just_digits(result[index_column_e], digit_pattern) if result[index_column_e] else (0, "")
        result.pop(3)
        result[3:2] = list(unit)
        return tuple(result)



def main():
    # for row in range(1, data.row_max+1):
    #     quote: tuple = get_quote(row)
    #     print(row, quote)

    x = dbControl("quote.sqlite")
    with x as db:
        build_tables(db)
        for row in range(1, data.row_max + 1):      # data.row_max + 1
            quote: tuple = get_quote(row)
            write_quote(quote, db)

        # write_quote(test_quote[0], db)
        # write_quote(test_quote[1], db)
        x.inform_db()



if __name__ == "__main__":
    main()
