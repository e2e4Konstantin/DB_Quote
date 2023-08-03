import sys
import os
import pickle
import inspect
from setting import SourceData

YELLOW = "\u001b[38;5;11m"
RESET = "\u001b[0m"


def scope(module_name: str, module_info):
    print(f'1: {module_name} -->> {__name__ = }')
    print(f"2: {module_name} -->> dir() ={[x for x in dir() if x[:2] != '__']}")
    print(f'3: {module_name} -->> {sys.modules.keys() = }')
    print(f'4. {module_name} -->> {inspect.getfile(module_info) = }')
    modules_x = inspect.getmembers(module_info)
    results_x = filter(lambda m: inspect.ismodule(m[1]), modules_x)
    [print(f'импортируемый модуль:{x}') for x in results_x]


def file_route(place: str, file_number: int) -> tuple[str, str, str]:
    """ Формирует маршрут и название файла в зависимости от места работы офис или дом"""
    valid_places = {"HOME", "OFFICE"}
    if place not in valid_places:
        print(f"file_route >> Место дислокации: '{YELLOW}{place}{RESET}' не найдено!")
        sys.exit()
        # raise ValueError(f"Место дислокации: '{place}' не найдено!")

    source_files = {
        1: (r"template_all_output.xlsx", "Quote"),
        3: (r"template_3_68_output.xlsx", "Quote"),
        4: (r"template_4_68_output.xlsx", "Quote"),
        5: (r"template_5_67_output.xlsx", "Quote"),
        0: (r"template.pickle", "Pickle")
    }
    if file_number not in set(source_files.keys()):
        print(f"file_route >> Файл с номером '{YELLOW}{file_number}{RESET}' не найден!")
        sys.exit()

    local_paths = {
        "OFFICE": r"C:\Users\kazak.ke\PycharmProjects\DB_Quote\src_data",
        "HOME": r"F:\Kazak\Google Диск\1_KK\Job_CNAC\Python_projects\DB_Quote\src_data",
    }
    return source_files[file_number][0], local_paths[place], source_files[file_number][1]


def pull_data(where_from: str = "FILE", place: str = "HOME", file_number: int = 3) -> SourceData | None:
    """ Читает данные из источника excel/picle. Возвращает ссылку на датафрейм. """
    pickle_file = f"template.pickle"
    match where_from:
        case "FILE":
            file_options = file_route(place, file_number)
            print(f"данные читаем из файла: {file_options}.")
            data = SourceData(*file_options)
            print(data, "\n")
            print(data.df.info(verbose=False))
            fullpath = os.path.abspath(os.path.join(file_options[1], pickle_file))
            with open(fullpath, 'wb') as handle:
                pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"данные записаны в: {fullpath}")
            return data
        case "PICLE":
            file_options = file_route(place, 0)
            fullpath = os.path.abspath(os.path.join(file_options[1], file_options[0]))

            with open(fullpath, 'rb') as handle:
                data = pickle.load(handle)

            if data:
                print(f"данные прочитаны из: '{YELLOW}{file_options[0]}{RESET}', '{file_options[1]}'")
                print(data, "\n")
                print(data.df.info(verbose=False))
            return data
        case _:
            print(f"Непонятно откуда брать данные '{YELLOW}{where_from}{RESET}'.")
    return None


if __name__ == '__main__':
    x = pull_data("FILE", "HOME", 3)
    y = pull_data("PICLE", "HOME")
