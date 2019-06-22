from requests import get
from json import loads


def get_iata(city):
    s = get(f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{city}%20в%20Лондон').text
    dct = loads(s).get('origin', '-')
    iata = dct['iata'] if dct != '-' else '<код не найден>'
    return iata


if __name__ == '__main__':
    print('IATA-код: ' + get_iata(input('Введите город c аэропортом на русском: ')))
