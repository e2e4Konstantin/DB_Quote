import csv
import re

units_measure = {
    'метр': ["м", "м.", "метры", "метров", "метра", "m"],
    'метр квадратный': ["м2", "м.2", "м2.", "м 2", "метр 2", "метров 2", "метра 2", "квадратный метр",
                        "метров квадратных", "m2", "m2."],
    'метр кубический': ["м3", "м 3", "метр 3", "метров 3", "метра 3", "кубический метр", "кубических метров", "m3"],
    'метр погонный': ["пог м", "пог. м", "пог м.", "пог. м.", "пог.м.", "п м", "п.м.", "пог метр", "погонных метров"],
    'тонна': ["т", "т.", "тонн", "тонны", "тон", "t", "t."],
    'килограмм': ["кг", "кг.", "килограммов", "килограмма", "kg", "kg."],
    'километр': ["км", "км." "километров", "километра", "km", "km."],
    'миллиметр': ["мм", "мм.", "миллиметра", "миллиметров", "mm", "mm."],
    'штука': ["шт.", "шт", "штук", "штуков", "штука", "штуки"],
    'гектар': ["га", "га.", "гектаров", "гектары"],
    'сутки': ["суток", "сутков"],
    'час': ["ч", "ч.", "часов", "часы", "часс", "чис"]
}

lm = []
# check_unit = ['м3', 'шт.', 'м', 'м.', 'км', 'м2', 'кг', 'т', 'га', 'пог. м', 'пог.м.']
check_unit = []

for unit in units_measure:
    check_unit.append(unit)
    for synonym in units_measure[unit]:
        check_unit.append(synonym)


def full_unit_name(unit_name: str) -> str:
    if unit_name in check_unit:
        if units_measure.get(unit_name, None):
            return unit_name
        else:
            for full_name, values in units_measure.items():
                if unit_name in values:
                    return full_name
    return ""


def first_digit_get(src_data: str) -> tuple[float, str]:
    separate = src_data.split(" ")
    digits_slice = separate[0]
    if digits_slice.isdigit():
        return float(digits_slice), " ".join(separate[1:]) if len(separate) > 1 else ""
    else:
        look_result = re.match("^\d+[,.]?\d*", digits_slice)
        if look_result:
            found_string = look_result.group()
            found_string.replace(",", ".")
            if len(digits_slice) > len(found_string):
                tail = digits_slice.replace(found_string, "")
            else:
                tail = ""
            separate[0] = tail
            return float(found_string), " ".join(separate) if len(separate) > 1 else ""
    return 0.0, src_data


def second_unit_get(src_data: str) -> tuple[str, str]:
    if src_data:
        separate = src_data.split(" ")
        unit_slice_one = separate[0]
        if unit_slice_one not in check_unit:
            if len(separate) > 1:
                unit_slice_two = separate[1]
                res_try = f"{unit_slice_one} {unit_slice_two}"
                if res_try in check_unit:
                    return full_unit_name(res_try), src_data.replace(res_try, "", 1).strip()
            return full_unit_name("штука"), src_data
        else:
            return full_unit_name(unit_slice_one), src_data.replace(unit_slice_one, "", 1).strip()
    return "", ""


def main():
    # print(check_unit)
    with open(r'F:\Kazak\Google Диск\1_KK\Job_CNAC\Python_projects\DB_Quote\src_data\единицы.csv') as f:
        reader = csv.reader(f, delimiter=',')
        [lm.append(row[0].strip().lower()) for row in reader if row]

    print(lm[:10])

    print(first_digit_get("100 m ggg"))
    print(second_unit_get('бетона полости сваи'))
    print(full_unit_name("м 3"))
    print(full_unit_name("пог. м"))

    for x in lm:
        d = first_digit_get(x)
        u = second_unit_get(d[1])
        print(d[0], u[0], u[1])


if __name__ == "__main__":
    print(f"main -->> dir() ={[x for x in dir() if x[:2] != '__']}")
    main()
