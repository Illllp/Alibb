from random import randint

count = 0  # Количество попыток
a = randint(1, 100)  # загаданное число
print('Это игра: угадай число\nЯ загадал число от 1 до 100, если угадаешь то...')

while True:
    try:
        number = int(input('Введите число: '))  # Запрос числоа у пользователя
        if number > a:
            print('Загаданное число меньше')
            count += 1  # Подсчет попыток
        elif number < a:
            print('Загаданное число больше')
            count += 1
        else:
            count += 1
            print(f'Ты угадал загаданное число с {count} попытки.\nСпасибо за игру!!!')
            continuation = input('Хочешь продолжить?\n')
            if continuation == 'да':
                a = randint(1, 100)
                count = 0
            else:
                print('Жаль, а так хорошо играли.')
                break
    except ValueError:  # Искать ошибку несоответствия с int в number = int(input('Введите число: '))
        print('Не видишь?\nА то и видно. Там сказанно "Введите ЧИСЛО", а что вводишь?\nПробуй заного.')
