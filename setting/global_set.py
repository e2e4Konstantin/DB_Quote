import os

console_colors = {
    "YELLOW": "\u001b[38;5;11m",
    "RESET": "\u001b[0m"
}

BASIC = 1
RELATED = 0

physical_properties_data = {
    ('напряжение', 'voltage', 'v'),
    ('площадь', 'square', 's'),
    ('масса', 'mass', 'n'),
    ('количество', 'quantity', 'n'),
    ('время', 'time', 't'),
    ('расстояние', 'length', 'l'),
    ('объем', 'volume', 'v'),
    ('температура', 'temperature', 't')
}

measurement_units = {
    ('вольт', 'volt', 'в', 'v', BASIC, 1, 'напряжение'),
    ('киловольт', 'kilovolt', 'кВ', 'kV', RELATED, 1_000, 'напряжение'),
    ('килограмм', 'kilogram', 'кг', 'kg', BASIC, 1, 'масса'),
    ('тонна', 'ton', 'тон', 'ton', RELATED, 1_000, 'масса'),
    ('метр', 'metr', 'м', 'm', BASIC, 1, 'расстояние'),
    ('миллиметр', 'millimeter', 'мм', 'mm', RELATED, 0.001, 'расстояние'),
    ('километр', 'kilometer', 'км', 'km', RELATED, 1_000.0, 'расстояние'),
    ('метр погонный', 'meter linea', 'мп', 'lm', RELATED, 1, 'расстояние'),
    ('метр квадратный', 'meter square', 'м2', 'm2', BASIC, 1, 'площадь'),
    ('гектар', 'hectare', 'га', 'ha', RELATED, 10_000, 'площадь'),
    ('сотка', 'ar', 'а', 'a', RELATED, 100, 'площадь'),
    ('метр кубический', 'cubic meter', 'м3', 'm3', BASIC, 1, 'объем'),
    ('штука', 'unit', 'шт', 'u', RELATED, 1, 'количество'),
    ('единица', 'one', 'ед', '1', BASIC, 1, 'количество')
}




def get_full_file_name(file_name: str, file_path: str = "") -> str | None:
    test_path = os.path.abspath(os.path.join(file_path, file_name))
    if os.path.exists(test_path):
        return test_path
    return None


def check_db_file(db_file_name: str, db_file_path: str = ""):
    full_path_db_name = get_full_file_name(db_file_name, db_file_path)
    if not full_path_db_name:
        print(f"Файл БД '{console_colors['YELLOW']}{db_file_name}{console_colors['RESET']}' "
              f"в папке '{db_file_path}' не найден.\nСоздается новый файл в папке '{os.getcwd()}'")
        return db_file_name
    return full_path_db_name
