import itertools


units_measure = {
    'метр': ["м", "метры", "метров", "метра"],
    'метр квадратный': ["м2", "м 2", "метр 2", "метров 2", "метра 2"],
    'метр кубический': ["м3", "м 3", "метр 3", "метров 3", "метра 3"],
    'метр погонный': ["пог м", "п м",  "пог метр"],
    'тонна': ["т", "тонн", "тонны"],
    'килограмм': ["кг", "килограммов", "килограмма"],
    'километр': ["км", "километров", "километра"],
    'миллиметр': ["мм", "миллиметра", "миллиметров"],
}

#
# def add_dots(sentence: str) -> list[str] | None:
#     words = sentence.split(" ")
#     if words:
#         dotted_words = []
#         [dotted_words.append(f"{word}.")for word in words]
#         return dotted_words
#     return None


def add_dots(words: list[str]) -> list[str] | None:
    if len(words) > 0:
        dotted_words = []
        [dotted_words.append(f"{word}.")for word in words]
        return dotted_words
    return None


# s = 'пог метр'
# s1 = s.split(" ")
# s2 = add_dots(s)
# print(s1, s2)

# st = [x for x in itertools.product(s1, s2)]
# print(st)
#
# st2 = [x for x in itertools.product(s2, s1)]
# print(st2)


# length = len(s1)
# s1.extend(add_dots(s))
#
# b = [x for x in itertools.permutations(s1, length) if x[0].replace('.', '') != x[1].replace('.', '')]
# print(b)


# unit_measure_guide = dict()


s = 'м 2'
s1 = s.split(" ")
length = len(s1)
s2 = add_dots(s1)
print(s1, s2)

s1[1], s2[0] = s2[0], s1[1]
s3 = []

[s3.extend(["".join(list(x))," ".join(list(x))]) for x in itertools.product(s1, s2) if x[0].replace('.', '') != x[1].replace('.', '')]

# s3 = [("".join(list(x))," ".join(list(x))) for x in itertools.product(s1, s2) if x[0].replace('.', '') != x[1].replace('.', '')]
# s4 = []
# [s4.extend(list(x)) for x in s3]
print(s1, s2)
print(s3)
# print(s4)


# s1.extend(add_dots(s1))
# print(s1)
# b = [x for x in itertools.permutations(s1, length) if x[0].replace('.', '') != x[1].replace('.', '')]
# print(b)








def words_permutations(synonyms: list[str]) -> list[str] | None:
    print(synonyms)
    result = []
    for synonym in synonyms:
        synonym_words = synonym.split(" ")
        length = len(synonym_words)
        synonym_words.extend(add_dots(synonym))
        result.extend(synonym_words)
    if len(result) > 0:
        return result
    return None


# a = words_permutations(units_measure['метр квадратный'])
# print(a)


# for x in units_measure:
#     print(x, ': ', end='')

#
#
#     # unit_measure_guide[x]

