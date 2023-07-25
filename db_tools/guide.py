import itertools

units_measure = {
    'метр': ["м", "метры", "метров", "метра"],
    'метр квадратный': ["м2", "м 2", "метр 2", "метров 2", "метра 2"],
    'метр кубический': ["м3", "м 3", "метр 3", "метров 3", "метра 3"],
    'метр погонный': ["пог м", "п м", "пог метр"],
    'тонна': ["т", "тонн", "тонны"],
    'килограмм': ["кг", "килограммов", "килограмма"],
    'километр': ["км", "километров", "километра"],
    'миллиметр': ["мм", "миллиметра", "миллиметров"],
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

# unit_measure_guide = dict()
for x in units_measure:
    print(x, ': ', end='')
    dot_variant = []
    dot_variant.extend(mix_dot(x))
    for synonym in units_measure[x]:
        dot_variant.extend(mix_dot(synonym))
        # wd = synonym.split(" ")
        # if len(synonym.split(" ")) > 1:
        #     for w in

        # print(f"{synonym}, ", end='')
    print(dot_variant)


    # unit_measure_guide[x]
