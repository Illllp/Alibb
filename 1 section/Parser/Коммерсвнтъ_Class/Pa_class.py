import urllib.request

from bs4 import BeautifulSoup


class Parser:
    '''
    Парсинг новостей
    '''
    raw_html = ''
    html = ''
    res = []

    def __init__(self, url, path):
        '''
        Запрос ссылки новстей и путь сохранения
        :param url: Ссылка
        :param path: Путь
        '''
        self.url = url
        self.path = path

    def get_html(self):
        '''
        Приображение html с помощью "html.parser"
        :return: Призентабельный вид html
        '''
        a = urllib.request.urlopen(self.url)
        self.raw_html = a.read()  # Читаем ссылку
        self.html = BeautifulSoup(self.raw_html, "html.parser")

    def parsing(self):
        '''
        Парсинг новстной ленты по 3-м переменным:
        Заголовок
        Текст
        Ссылка
        '''
        news = self.html.find_all('div', class_='multimedia__item slider-item slider-multimedia-resizable-item')
        for i in news:
            self.res.append({
                'heading': i.find('a', class_='uho__link uho__link--overlay slider-link').get_text(),
                'text': i.find('a', class_='uho__link slider-link').get_text(),
                'href': i.a.get('href'),
            })

    def save(self):
        '''
        Сохранение в текстовый файл весь парсинг
        '''
        with open(self.path, 'w', encoding='utf-8') as f:
            for i in self.res:
                f.write(f"Новость: {i['heading']}\n"
                        f"Описание: {i['text']}\n\n"
                        f"Ссылка: https://www.kommersant.ru{i['href']}\n"
                        f"******************************\n\n")

    def run(self):
        '''
        Ввывод полученных данных
        '''
        self.get_html()
        self.parsing()
        self.save()
