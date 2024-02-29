# Программа lab6_3
# Пример по теме условные операторы
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 16.11.23
# переменные:
    #x0 - начальное значение x
    #hx - шаг
    #xn - конечное значение x
    #nx - количество шагов
    #i - параметр цикла

from math import trunc

print('Введите x = x0(hx)xn')
x0 = float(input())
hx = float(input())
xn = float(input())

s = 0
p = 1
x = x0
nx = trunc((xn-x0)/hx + 1E-6)+1

for i in range(nx):
    if (x > -3) and (x <= 0):
        y = x + 3
    elif (x > 0) and (x < 6):
        y = -0.5*x + 3
    else:
        y = 0
    s += y
    p *= y
    print('x = %.2f\ty = %.2f' % (x, y))
    x += hx

print ('Сумма всех y = %.2f\nПроизведение всех y = %.2f' % (s, p))