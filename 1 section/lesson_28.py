'''
Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd".
Напишите функцию, которая будет возвращать True или False, соответственно.
'''
print('Задание 1')


def odd_ball(arr):
    '''
    :param arr: принимает список
    :return: выводит 'odd' и число одинаковое по индексу
    '''
    return arr.index('odd') in arr


print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
print(odd_ball(["even", 10, "odd", 2, "even"]))  # True

'''
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент 2
последовательности включительно. Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5.
Попробуйте решить задачу двумя способами (один из способов в одну строчку кода)
'''
print('\nЗадание 2')


def find_sum(n):
    '''
    :param n: int принимает количество цифр
    :return: вывод суммы всех чисел кратные 3 и 5
    '''
    a = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            a += i
    return a


print(find_sum(5))
print(find_sum(10))

'''
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names - ["Rya", "Kieran", "Nark", "John", "David", "Paul"I # ["Ryan", "Mark", "John", "Paul"]
'''

print('\nЗадание 3')


def get_numes(a):
    '''
    :param a: принимает список
    :return: выводит слова равные 4 буквам
    '''
    return [i for i in a if len(i) == 4]


print(get_numes(["Rya", "Kieran", "Nark", "John", "David", "Paul"]))
