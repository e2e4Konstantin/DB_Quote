import itertools

units_measure = {
    'метр': ["м", "метры", "метров", "метра"],
    'метр квадратный': ["м2", "м 2", "метр 2", "метров 2", "метра 2", "квадратный метр"],
    'метр кубический': ["м3", "м 3", "метр 3", "метров 3", "метра 3", "кубический метр"],
    'метр погонный': ["пог м", "п м", "пог метр"],
    'тонна': ["т", "тонн", "тонны", "тон"],
    'килограмм': ["кг", "килограммов", "килограмма"],
    'километр': ["км", "километров", "километра"],
    'миллиметр': ["мм", "миллиметра", "миллиметров"],
    'штука': ["шт", "штук", "штуков", "штука", "штуки"],
    'гектар': ["га", "гектаров", "гектары"],
    'сутки': ["суток", "сутков"],
    'час': ["часов", "часы", "часс", "чис"]
}

physical_property = {
    'длинна': (["метр", "километр", "миллиметр", "сантиметр", "миля", "дециметр", "метр погонный"], ["l", "Length"]),
    'площадь': (["метр квадратный", "миллиметр  квадратный", "километр квадратный", "сантиметр квадратный", "миля квадратная", "дециметр квадратный", "гектар", "сотка"], ["s", "square"]),
    'масса': (["килограмм", "тонна", "центнер"], ["m", "mass", "wight"]),
    'количество': (["штука", "единица"], ["q", "quantity"]),
    'время': (["секунда", "минута", "час", "сутки", "месяц", "год"], ["t", "time"]),
    'объем': (["метр кубический", "литр"], ["v", "volume"])
}


def add_dots(words: list[str]) -> list[str] | None:
    if len(words) > 0:
        dotted_words = []
        [dotted_words.append(f"{word}.") for word in words]
        return dotted_words
    return None


def mix_dot(src_text: str) -> list[str] | None:
    if src_text:
        words = src_text.strip().split(" ")[:2]
        dot_word = add_dots(words)
        # print(words, dot_word)
        if len(words) > 1:
            words[1], dot_word[0] = dot_word[0], words[1]
            result = []
            [result.extend(["".join(list(x)), " ".join(list(x))]) for x in itertools.product(words, dot_word) if
             x[0].replace('.', '') != x[1].replace('.', '')]
            # print(words, dot_word, result)
            return result
        else:
            words.extend(dot_word)
            return words
    return None


for x in units_measure:
    print(x, ': ', end='')
    dot_variant = []
    dot_variant.extend(mix_dot(x))
    for synonym in units_measure[x]:
        dot_variant.extend(mix_dot(synonym))
    # print(dot_variant)
    units_measure[x] = dot_variant

print(units_measure['метр квадратный'])
