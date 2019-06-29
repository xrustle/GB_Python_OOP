# Это задание продолжает практическое задание прошлого урока. За основу возьмите свой код с классами Word и Sentence.
# Выполним с ним следующие преобразования:
# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»). Для класса Noun укажите значение
# по умолчанию «сущ» (сокращение от существительное), а для Verb — «гл» (сокращение от глагол).
# Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
# Подсказка: теперь в нём не нужно хранить части речи.
# words = []
# words.append(Noun("собака"))
# words.append(Verb("ела"))
# words.append(Noun("колбасу"))
# words.append(Noun("кот"))
# По желанию добавьте ещё несколько глаголов и существительных.
# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
# Подсказка: ранее part был свойством класса Word, а теперь это метод классов Noun и Verb.


class Word:
    def __init__(self, text):
        self.text = text


class Noun(Word):
    __grammar = 'сущ'

    @staticmethod  # Это PyCharm рекомендует сделать эти методы статичными,
    def part():  # так как они не используют атрибуты экземпляров.
        return 'Существительное'


class Verb(Word):
    __grammar = 'гл'

    @staticmethod
    def part():
        return 'Глагол'


class Sentence:
    def __init__(self, arg):
        self.content = arg

    def show(self):
        a = []
        for i in self.content:
            a.append(words[i].text)
        return ' '.join(a)

    def show_parts(self):
        parts = set()
        for i in self.content:
            parts.add(words[i].part())
        return ' '.join(parts)


if __name__ == '__main__':
    words = [Noun("собака"),
             Verb("ела"),
             Noun("колбасу"),
             Noun("кот")]

    s = Sentence([0, 1, 2])
    print(f's.show():\t\t{s.show()}')
    print(f's.show_parts():\t{s.show_parts()}')
