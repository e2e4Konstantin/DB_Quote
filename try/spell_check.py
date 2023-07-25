from spellchecker import SpellChecker

spell = SpellChecker(language='ru')

word = "мтр"

if spell.correction(word) == word:
    print("Слово написано верно!")
else:
    print("Ошибка в написании слова")
    print("Возможные варианты:")
    print(spell.candidates(word))

text = 'Это предлжение содержт ошибку метр'

mistakes = spell.unknown(text.split())

for mistake in mistakes:
    print(f'Ошибка: "{mistake}" \nПравильное написание: {spell.correction(mistake)}')
