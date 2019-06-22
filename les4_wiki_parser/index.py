import re
from wiki_requests import get_topic_page


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall(r'[а-яА-Я][а-яА-Я\-\']+[а-яА-Я]', html_content)
    return [w.capitalize() for w in words]  # Добавил капитализацию, потому что Дерево и дерево считались разными


def get_common_words(topic):
    word_list = get_topic_words(topic)
    rate = {}
    for word in word_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def vizualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[100:110]:
        print(w[0])


def main():
    topic = input('Topic: ')
    vizualize_common_words(topic)
