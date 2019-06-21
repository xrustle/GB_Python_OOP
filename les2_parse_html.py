import re
from bs4 import BeautifulSoup

with open('les2_geekbrains_ru.html', encoding='utf-8') as f:
    s = f.read()

# C помощью RegExp
spam = re.findall(r'<span class=\"total-users\">\D+([\d\s]+)\D+</span>', s)
counter = int(re.sub(' ', '', spam[0]))
print(counter)

# C помощью BeautifulSoup
soup = BeautifulSoup(s, 'html.parser')
text = soup.find_all("span", {"class": "total-users"})[0].string
# Далее с помощью RegExp достаем то же число аналоогично первому способу
eggs = re.findall(r'([\d\s]+\d)', text)
counter2 = int(re.sub(' ', '', eggs[0]))
print(counter2)
