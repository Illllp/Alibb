data = open('Data.txt', 'r+', encoding='utf-8')
count = 1
All = (f'Сотрудник {count}\n'
       f'Имя: {input("Имя: ")}\n'
       f'Фамилия: {input("Фамилия: ")}\n'
       f'Номер телефонв: +7{int(input("Номер телефона: +7"))}\n\n')
data.write(All)

while True:
    a = input('Желаете добавить кого-то еще?\n')
    if a == 'да':
        count += 1
        All = (f'Сотрудник {count}\n'
               f'Имя: {input("Имя: ")}\n'
               f'Фамилия: {input("Фамилия: ")}\n'
               f'Номер телефонв: +7{int(input("Номер телефона: +7"))}\n\n')
        data.write(All)
    else:
        break
data.close()
