'''
1-е задание
[1,2,3,] ---> [2,4,6]
'''

print('\nЗадание 1')


def l1(a, b, c):
    l3 = [a, b, c]
    l2 = [i * 2 for i in l3]
    print(l2)


l1(1, 2, 3)

'''
2-е задание
[1,2,3] --->    14 ---> 1^2 + 2^2 + 3^2 = 14
'''
print('\nЗадание 2')


def i1(a, b, c):
    i3 = [a, b, c]
    i2 = [i ** 2 for i in i3]
    print(sum(i2))


i1(1, 2, 3)

'''
3-е задание
timel = 3 ---> litres = 1
timel = 6.7 ---> litres = 3
timel = 11.8 ---> litres = 5
'''
print('\nЗадание 3')


def water_consumed_per_hour(time, water):
    print(f'Выпил {int(time * water)} л. за {time} часов.')


water_consumed_per_hour(4, 3)

'''
4-е задание
s = 'Hello world'
if stm:
    pass
else:
    pass
'''

print('\nЗадание 4')


def s(he):
    if ' ' in he:
        print(he.upper())
    else:
        print(he.lower())


s('hello world')
