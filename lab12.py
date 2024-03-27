# Программа lab12
# Пример по теме множества
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 13.03.24
# Дан текст, состоящий из латинских букв. Вывести все буквы, входящие в текст не менее двух раз.
# переменные:
    # s - текст
    # M1, M2 - множества

s = input('Введите текст: ')
M1 = set()
M2 = set()
for el in s:
    if el not in M1:
        M1.add(el)
    elif el != ' ' or el != ',' or el != '.':
        M2.add(el)
print('Буквы, встречающиеся в тексте не менее двух раз', M2)
