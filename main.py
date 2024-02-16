class Rat():
    lenght = 20
    max_age = 2
    weight = 450
    energy = 100

    def __init__(self):
        print(f"Rat's lenght {self.lenght} centimetres")
        print(f"Rat's max age {self.max_age} years")
        print(f"Rat's weight {self.weight} grams")

    def to_sleep(self):
        if self.energy <= 20:
            self.to_sleep()


class Hamster(Rat):
    lenght = 10
    weight = 45
    hunger = 100

    def __init__(self):
        print(f"Hamster's lenght {self.lenght} centimetres")
        print(f"Hamster's max age {self.max_age} years")
        print(f"Hamster's weight {self.weight} grams")

    def to_eat(self):
        if self.hunger <= 30:
            self.to_eat()

class Jerboa(Hamster):
    weight = 250
    max_age = 1
    mood = 100

    def __init__(self):
        print(f"Jerboa's lenght {self.lenght} centimetres")
        print(f"Jerboa's max age {self.max_age} years")
        print(f"Jerboa's weight {self.weight} grams")

    def to_play(self):
        if self.mood <= 50:
            self.to_play()

oscar = Jerboa()
homa = Hamster()
greg = Rat()