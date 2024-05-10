# Программа lab16_2
# Пример по теме бинарные файлы
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 09.05.24
# Сформировать текстовый файл Data.txt из заглавных букв A, B, C, D, E, F латинского алфавита и десятичных цифр.
# Найти номер строки, в которой находится самое большое нечётное число, и определить в ней самую длинную возрастающую
# последовательность из букв. Если строк с максимальным нечётным числом несколько, то выбрать ту, которая находится
# в файле позже.
# переменные:
    # m - номер меню
    # n - кол-во строк
    # f - файловая переменная
    # cnt - диапозон кол-ва эл. в строке
    # s, s1, w - вспомогательные переменные
    # nmin - самое большое нечетное число
    # imin - номер строки в котором самое большое нечетное число
    # s2 - самая длинная возрастающая псоледовательность в строке imin


from random import randrange, randint, choice


while True:
    print('1. Режим формирования файла')
    print('2. Режим обработки файла')
    print('3. Выход')
    m = int(input('Введите номер меню: '))
    match m:
        case 1:

            f = open('Data.txt', 'w')
            n = int(input('Введите кол-во строк '))

            for _ in range(n):
                cnt = randrange(10, 100)
                s = ''.join([choice((chr(randint(65, 90)), str(randint(0, 9)))) for _ in range(cnt)])
                f.write(s + '\n')
            f.close()

        case 2:

            f = open('Data.txt', 'r')
            s = f.readlines()

            nmin = 0
            num = '0'
            for i in range(len(s)):
                for j in range(len(s[i])):
                    if s[i][j].isdigit():
                        num += s[i][j]
                    else:
                        if int(num) >= nmin and int(num) % 2 != 0:
                            nmin = int(num)
                            imin = i
                        num = '0'
            s1 = s[imin]
            s2 = w = ' '
            for j in range(len(s1)):
                if s1[j].isalpha() and ord(s1[j]) > ord(s2[-1]):
                    w += s1[j]
                else:
                    if len(w) > len(s2):
                        s2 = w
                    w = ' '
            print(f'Строка {imin+1} - {s2}')

        case 3:
            break
