# Программа lab13
# Пример по теме множества
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 27.03.24
# Составить подпрограмму подсчета количества n элементов одномерного массива, значения которых больше числа р.
# С помощью подпрограммы подсчитать количество элементов больших р в каждом столбце двухмерной матрицы.
# переменные:

import random


CONST_D = 100


def input_matrix(n: int, m: int):
    """Функция заполнения матрицы случайными числами
    Входные параметры:
    n - число строк,
    m - число столбцов
    Выходные параметры:
    a - матрицы"""
    a = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            a[i][j] = random.randint(-CONST_D, CONST_D)
    return a


def output_matrix(n: int, m: int, a: list):
    """Процедура вывода матрицы
    Входные параметры:
    n - число строк
    m - число столбцов
    a - матрица"""
    for i in range(n):
        for j in range(m):
            print(a[i][j], end='\t')
        print()


def find_more_p(n: int, a: list, p: int):
    """Функция поиска в одномерном массиве кол-во элементов больших p
    Входные параметры:
    n - размер одномерного массива
    a - одномерный массив
    p - число больше, которого элементы массива считаются
    Выходные параметры:
    k - кол-во элементов больших p"""
    k = 0

    for i in range(n):
        if a[i] > p:
            k += 1
    return k


n = int(input('Введите число строк матрицы: '))
m = int(input('Введите число столбцов матрицы: '))
p = int(input('Введите число p: '))

a = input_matrix(n, m)
print('Матрица: ')
output_matrix(n, m, a)

for j in range(m):
    b = [0 for _ in range(n)]
    for i in range(n):
        b.append((a[i][j]))
    k = find_more_p(n, b, p)
    print(f'Кол-во элементов больших p в {j+1} столбце равно', k)
