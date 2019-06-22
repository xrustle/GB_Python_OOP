from requests import get


def get_link(topic):
    link = 'https://ru.wikipedia.org/wiki/' + topic.capitalize()
    return link


def get_topic_page(topic):
    link = get_link(topic)
    html_content = get(link).text
    return html_content
