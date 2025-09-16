class agent:
    def __init__(self, name, age):
        print("Welcome to the game")
        self.name = name
        self.age = age
        self.health = 100
        self.alive = True
    def curr_health(self):
        print(f"Health: {self.health}")
    def shoot(self):
        self.health -= 20
    def punch(self):
        self.health += 50
    def isAlive(self):
        if self.health <=0:
            self.alive = False
    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nHealth: {self.health}\nAlive: {self.alive}")
class Boss(agent):
    def blowFire(self):
        print("blow fire!")
bs = Boss('Kans',202)
bs.info()