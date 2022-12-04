'''
1-е задание
[1,2,3,] ---> [2,4,6]
'''
print('\nЗадание 1')
l1 = [1, 2, 3]
l2 = [i * 2 for i in l1]  # каждый элимент листа удвоен
print(l2)

'''
2-е задание
[1,2,3] --->    14 ---> 1^2 + 2^2 + 3^2 = 14
'''
print('\nЗадание 2')
l2 = [1, 2, 3]
l3 = [i ** 2 for i in l2]  # каждый элемент в листе возводим во вторую степень
print(sum(l3))  # суммируем каждый элемент в листе

'''
3-е задание
timel = 3 ---> litres = 1
timel = 6.7 ---> litres = 3
timel = 11.8 ---> litres = 5
'''
print('\nЗадание 3')
water = 0.5
time = 1
while time <= 24:  # 24 количество часов
    print(f'Выпил {int(time * water)} л. за {time} часов.')
    time += 1

'''
4-е задание
s = 'Hello world'
if stm:
    pass
else:
    pass
'''
print('\nЗадание 4')
s = 'Helloworld'
if ' ' in s:
    print(s.upper())  # HELLO WORLD
else:
    print(s.lower())  # helloworld
