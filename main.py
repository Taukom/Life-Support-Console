
import threading

import time

from random import *
from planets_data import planets
from animation import explode_ship, meteorite_destruction, oxygen_box_scene


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


Mineral = ["Gold", "Uranium", "Iron", "Iron", "Iron", "Iron", ]


def normal_energy():
    b = s.Energy
    if b<1000: return str(b)+" Wh"
    elif b>=1000 and b<1000000 : return str(round(b/1000, 1))+ " kWH"
    else: return str(round(b/1000000, 1))+"MWh"

s = Status(Planet="Earth", Oxygen=randint(60, 100,), Energy=randint(500, 1000), Fuel=randint(30, 100), HP=100, Score=0, Inventory={},  AutoDiggerActive = False)

s.Inventory = {
    "Iron": 0,
    "Gold": 0,
    "Uranium": 0,
    "Iron wall": 0,
    "Atomic bomb": 0
}


def get_status():
    print("Planet >>",s.Planet)
    print("Oxygen >>", round(s.Oxygen, 3), "kg ("+str(s.Oxygen//0.09)+" sec)")
    print("Energy >>", normal_energy())
    print("Fuel >>",round(s.Fuel, 1), "kg"+ get_inv())
    print("HP >>", round(s.HP, 1))

def povez():
    n = randint(0, len(Mineral)-1)
    povez = randint(0, 10)
    if povez < 10:
        s.Inventory[Mineral[n]]+=1
        return str(Mineral[n])
    return None

def get_inv():
    st = ''
    i = s.Inventory
    date = list(i.keys())
    date2 = list(i.values())
    for x in range(len(date)):
        if date2[x]!=0:
            st += " x" + str(date2[x]) + " " + str(date[x])

    return st

def do_dig():
    telldot("> > > Your dig a rock and find")
    if s.Planet=="Earth":
        n = povez()
        b = s.Fuel
        z = round(uniform(0, 2), 1)
        if n!=None:
            print(round(z, 1), "kg of Fuel! + "+n)
            print(round(s.Fuel, 1), ">>>", round(b + z, 1))
        else:
            print(round(z, 1), "kg of Fuel!")
            print(round(s.Fuel, 1),">>>",round(b+z, 1))
        s.Fuel+=z





def name_planets() -> str:
    return ", ".join([p['name'] for p in planets])





def get_planet_info(name: str) -> str:
    name = name[12:]
    planet = next((p for p in planets if p["name"].lower() == name.lower()), None)
    if planet:
        return (f"Planet: {planet['name']} | Safety: {planet['safety']} | "
                f"Resources: {planet['resources']} | Settlements: {planet['settlements']} | "
                f"Travel Cost: {planet['travel_cost']} credits")
    return f"Planet '{name}' not found."

def buy_pet():

    return





def craft(item: str=None):
    i = s.Inventory
    if item==None:
        return print("You can craft: \n"
                "Iron wall - x5 Iron\n"
                "AutoDigger - x5 Iron + x2 Gold\n"
                "AntiMeteor - x7 Iron + x2 Gold\n"
                "AutoRepair - x20 Iron + x10 Gold + x2 Uranium\n"
                "SystemUpgrade - x20 Gold + x50 Iron + x5 Uranium\n"
                "Atomic Bomb - 10 Uranium 10 Gold\n")
    elif item=="IRON WALL":
        if i["Iron"]>=5:
            s.Inventory["Iron wall"]+=1
            s.Inventory["Iron"]-=5
            return print("-5 Iron \n"
                         "+1 Iron wall")
        else:
            return print("You wanna more Iron bro")
    elif item=="AUTODIGGER":
        if i["Iron"]>=5 and i["Gold"]>=2:
            AutoDigger()
            s.Inventory["Iron"]-=5
            s.Inventory['Gold']-=2
            return print("-5 Iron \n"
                         "-2 Gold \n"
                         "+1 AutoDigger, check STATUS ")
        else:
            return print("You wanna more resurses bro")

    elif item=="Atomic Bomb":
        if i["Uranium"]>=10:
            s.Inventory["Atomic Bomb"]+=1
            s.Inventory["Uranium"]-=5
            return print("-10 Uranium \n"
                         "+Atomic Bomb")
        else:
            return print("You wanna more Iron bro")




def command():
    print("::: ", end='')
    c = input()
    if c.upper()=="STATUS" or c.upper()=="S":
        get_status()
    elif c.upper()=="FULL ENERGY":
        print(s.Energy)
    elif c.upper()=="DIG":
        do_dig()
    elif c.upper()=="PLANET INFO {planet}":
        get_planet_info(input())
    elif c.upper()=="SYS" or c.upper()=="SS" or c.upper()=="SYSTEM":
        help()
    elif c.upper()=="ATOMIC BOMB":
        explode_ship(score=s.Score)
    elif c.upper()=="REPAIR":
        repair()
    elif c.upper().count("CRAFT")==1:
        if len(c)==5:
            craft()
        else:
            craft(c[6:].upper())

s.Inventory["Atomic bomb"]+=1
s.Inventory["Iron wall"]+=10


def help():
    print("> STATUS(s)\n"
          "> PLANET INFO(PI)\n"
          "> DIG\n"
          "> GO [planet]\n"
          "> CRAFT\n"
          "> FULL ENERGY\n"
          "> PLANET LIST(PL)\n"
          "> ATTACK\n"
          "> REPAIR")

def repair():
    if s.Inventory["Iron wall"]>=1:
        s.HP+=10
        s.Inventory["Iron wall"]-=1
        print("+10HP\n"
              "-1 Iron wall")
    else:
        print("You need x1 Iron wall")

def meteor():
    r = randint(0, 1000)
    di = randint(1, 50)
    if r>950:
        print(f"[System] Meteorite {di} kg crashed into a shutle!")
        print(f"{s.HP} HP >>> {s.HP-di} HP, repair your ship!")
        s.HP-=di



#Текстовые приколы

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


def AutoDigger():
    if s.AutoDiggerActive:
        print("AutoDigger working bro!")
        return

    s.AutoDiggerActive = True

    def dig_loop():
        while True:
            time.sleep(10)
            mineral = povez()
            if mineral:
                print(f"[System] + {mineral}!")
            s.Fuel += round(uniform(0, 2), 1)

    threading.Thread(target=dig_loop, daemon=True).start()
    print("AutoDigger has arrived on your ship!")







# telldot("Hello, you're in a space shuttle, in a deep space")
# tellslow("You have command: SYSTEM(SS) | STATUS(S) ")

def oxygen_lost():
    score = 0
    while s.Oxygen>0:
        time.sleep(1)
        s.Oxygen-=0.09
        s.Score+=1
        meteor()

threading.Thread(target=oxygen_lost, daemon=True).start()

while s.Oxygen>0 and s.HP>0:
    command()

if s.Oxygen<=0:
    oxygen_box_scene(oxygen_box_scene(score=s.Score, width=120, height=50, fps=8))
elif s.HP<=0:
    meteorite_destruction(score=s.Score, width=120, height=50, fps=8)


