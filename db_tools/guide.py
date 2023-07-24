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


def add_dots(sentence: str) -> list[str] | None:
    words = sentence.split(" ")
    if words:
        dotted_words = []
        [dotted_words.append(f"{word}.")for word in words]
        return dotted_words
    return None

s = 'пог метр'
s1 = s.split(" ")
s2 = add_dots(s)
print(s1, s2)

# st = [x for x in itertools.product(s1, s2)]
# print(st)
#
# st2 = [x for x in itertools.product(s2, s1)]
# print(st2)

s1.extend(s2)
print(s1)
a = list(itertools.permutations(s1, 2))
print(a)

b = [x for x in a if x[0].replace('.', '')!=x[1].replace('.', '')]
print(b)


# unit_measure_guide = dict()
# for x in units_measure:
#     print(x, ': ', end='')
#     for synonym in units_measure[x]:
#         wd = synonym.split(" ")
#         if len(synonym.split(" ")) > 1:
#             for w in
#
#
#         print(synonym, synonym.split(" "), ' ', end='')
#     print()
#
#
#     # unit_measure_guide[x]

