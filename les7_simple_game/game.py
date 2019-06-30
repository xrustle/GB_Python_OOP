from player import Player
from hamsters import Hamster

hamsters_count = 4

class Game:
    happy_message = 'You won!'
    map = '****\n****\n****\n****'
    game_on = True

    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(hamsters_count):
            self.hamsters.append(Hamster(i + 1, self.get_full_map()))

    @staticmethod
    def add_point(position, name, s):
        li = s.split('\n')
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return '\n'.join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, 'x', s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        print(s)

    def move_player(self, destination):
        if destination == 's':
            if self.player.position[1] == len(self.map.split('\n')) - 1:
                return False
            self.player.position[1] += 1
        elif destination == 'w':
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1
        elif destination == 'a':
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1
        elif destination == 'd':
            if self.player.position[0] == len(self.map.split('\n')[0]) - 1:
                return False
            self.player.position[0] += 1
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        s = self.add_point(self.player.position, 'x', s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        return s

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split('\n')[coords[1]][coords[0]]

    directions = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}

    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        if hamster not in ('*', 'x'):
            self.player.was_hit(int(hamster))

            if self.player.health <= 0:
                self.game_on = False
                print('Game over')
                return False

            print('Player\'s health:', self.player.health)
            killed = self.hamsters[int(hamster) - 1].on_shot()

            if not killed:
                print('Hamster wasn\'t killed')
                self.move_player(self.directions[direction])
            else:
                print(self.hamsters[int(hamster) - 1].id, 'was killed')

    def start(self):
        game.render_map()
        while self.game_on:
            for h in self.hamsters:
                if h.health > 0:
                    break
            else:
                print(self.happy_message)
                self.game_on = False
                return True

            command = input('Insert command: ')
            if command in ['w', 'a', 's', 'd']:
                self.move_player(command)
                self.render_map()
            elif command == 'e':
                self.player.wait()
                self.render_map()
            elif command == 'q':
                self.game_on = False


game = Game()
game.start()

# 1. Попробуйте выйти за границы поля.
#    Я код писал сам по видео урокам. И за границы мы не выходили.
#    Мы это на исправляли в методе Game move_player на одном из видео.
#    В любом случае такого бага сейчас нет
#    34-51 строки

# 2. У вас получается рождение под хомяком?
#    Исправлено. В get_full_map теперь помимо хомяков добавляется и игрок.
#    Чтобы хомяки не могли появиться на месте игрока
#    55 строка

# 3. Отличная концовка, не так ли?
#    Да, неплохая. Очень "интересная" игра)
#    Исправил концовку. Если убиваем последнего хомяка, то программа завершается  тестом You won!
#    93-95 строка в game.py
