# Программа lab8
# Пример по теме вложенные циклы
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 05.12.23
# переменные:
    # x0 - начальное значение x
    # hx - шаг
    # xn - конечное значение x
    # t, a - параметры функции
    # p - степень числа

from math import cos

print('Введите x = x0(hx)xn')
x0 = float(input())
hx = float(input())
xn = float(input())

x = x0
while x <= xn + hx/3:
    t = 0
    p = 1
    for n in range(16):
        p *= x*x
        t += p / (3 * n + 2)
    if abs(x) <= 1:
        a = 2.5
    else:
        a = 0.5

    z = x * x * cos(a * x + t)
    print('x = %.2f\tz = %.2f' % (x, z))
    x += hx

