# Программа lab7_1
# Пример по теме цикл с предусловием
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 21.11.23
# переменные:
    # x0 - начальное значение x
    # hx - шаг
    # xn - конечное значение x
    # c - кол-во точек

def func(x):
    f = 3 * x * x + 2 * x + 1
    return f

def yfunc(x):
    y = x + 3
    return y

print('Введите x0(hx)xn: ')
x0 = float(input())
hx = float(input())
xn = float(input())

x = x0
c = 0

while x <= xn + hx/2:
    f = func(x)
    y = yfunc(x)
    if f > y:
        c += 1
    print('x = %.2f,\t f(x) = %5.2f,\t y(x) = %5.2f' % (x, f, y))
    x += hx

print('Кол-во точек: ', c)
