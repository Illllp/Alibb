import urllib.request

from bs4 import BeautifulSoup

a = urllib.request.urlopen('https://www.kommersant.ru/?from=logo')

html = a.read()  # Читаем ссылку
soup = BeautifulSoup(html, "html.parser")

# Вставляю нужный мне блок с новостями
news = soup.find_all('div', class_='multimedia__item slider-item slider-multimedia-resizable-item')
results = []

# Сортирую в списки на: заголовок, текст, ссылка
for i in news:
    results.append({
        'heading': i.find('a', class_='uho__link uho__link--overlay slider-link').get_text(),
        'text': i.find('a', class_='uho__link slider-link').get_text(),
        'href': i.a.get('href'),
    })
# Создаю новый файл
file = open('Коммерсантъ.txt', 'w', encoding='utf-8')

# Вставляю отдельно списки в созданный файл
for i in results:
    file.write(f"Новость: {i['heading']}\n"
               f"Описание: {i['text']}\n\n"
               f"Ссылка: {i['href']}\n"
               f"******************************\n\n")
file.close()
