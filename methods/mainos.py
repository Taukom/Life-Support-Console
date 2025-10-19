import time
from random import randint

Mineral = ["Gold", "Uranium", "Iron", "Iron", "Iron", "Iron"]

class Status:
    def __init__(self, Oxygen: float, Energy: float, Fuel: float, HP: float, Planet: str, Score: int, Inventory: dict,  AutoDiggerActive: bool):
        self.Planet = Planet
        self.Oxygen = Oxygen
        self.Energy = Energy
        self.Fuel = Fuel
        self.HP = HP
        self.Score = Score
        self.Inventory = Inventory
        self.AutoDiggerActive = False

s = Status(Planet="Earth", Oxygen=randint(60, 100,), Energy=randint(500, 1000), Fuel=randint(30, 100), HP=100, Score=0, Inventory={},  AutoDiggerActive = False)



s.Inventory = {
    "Iron": 0,
    "Gold": 0,
    "Uranium": 0,
    "Iron wall": 0,
    "Atomic bomb": 0,
    "Golden wall": 0
}



def telldot(z):
    print(z, end="")
    for _ in range(2):
        print(".", end="")
        time.sleep(1)
    print(".")

def tellslow(message, tim: int=2):
    message = str(message)
    time.sleep(tim)
    print(message)