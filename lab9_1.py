# Программа lab9_1
# Пример по теме одномерные массивы
# Программист: Гомелаури Е.А., гр. 344
# Проверил: Дмитриева Т. А.
# Дата написания: 14.02.24
# переменные:
    #n - размер массива
    #a - одномерный массив
    #i - индекс элемента
    #p - произведение положительных элементов
    #el - элемент массива

#Ввод массива
n = int(input('Введите размер массива: '))
print('Введите', n,'элементов массива')
a = []
for i in range(n):
    print('a[',i,'] = ', sep='', end='')
    a.append(float(input()))

#Эхо-вывод массива
print('Массив: ')
for el in a:
    print(el, end=' ')
print()

#Поиск произведения положительных элементов
p = 1
for el in a:
    if el > 0:
        p*=el

print('Произведение всех положительных элементов: ', p)