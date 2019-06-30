from random import randint


class Player:
    health = 10
    max_health = 10
    position = [2, 0]

    def was_hit(self, hid):
        self.health -= randint(1, hid + 1)

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player's health", self.health)
