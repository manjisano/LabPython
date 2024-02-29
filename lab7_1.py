# Программа lab7_1
# Пример по теме цикл с предусловием
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 21.11.23
# переменные:
    #x0 - начальное значение x
    #hx - шаг
    #xn - конечное значение x
    #s - сумма
    #p - произведение

print('Введите x = x0(hx)xn')
x0 = float(input())
hx = float(input())
xn = float(input())

s = 0
p = 1
x = x0

while x <= xn + hx/3:
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