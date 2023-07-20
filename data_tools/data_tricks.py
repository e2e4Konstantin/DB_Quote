


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

