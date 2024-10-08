# Программа lab6_2
# Пример по теме условные операторы
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 16.11.23
# переменные:
    #a - константа формулы
    #p1, p2 - произведения ряда
    #p - сумма произведений ряда
    #i, k - параметр цикла

a = float(input('Введите значение а '))
p1 = p2 = 1

for i in range(1, 11):
    p1 *= (i * (i + a))/(i * i + a * a)

for k in range(2, 5):
    p2 *= k**3/(k+a)

p = p1 + p2
print('При %.2f результат произведения %f' % (a,p))
