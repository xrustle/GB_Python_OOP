from requests import get
from bs4 import BeautifulSoup as bs
from re import compile

URL = 'https://ru.wikipedia.org'
WIKI = '/wiki/'


def get_link(topic):
    link = URL + WIKI + topic.capitalize()
    return link


def get_topic_page(topic):
    link = get_link(topic)
    html_content = get(link).text

    # Вот в этом месте добавлен поиск ссылок /wiki/...
    # Функция теперь возвращает сумму всех связанных страниц вместе с исходной страницей
    soup = bs(html_content, 'html.parser')
    for l in soup.findAll('a', attrs={'href': compile('^' + WIKI)}):
        html_content += get(URL + l.get('href')).text

    return html_content
