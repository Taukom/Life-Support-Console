# Oxygen / Fuel / Energy / HP
# STATUS / GO /
import random
import threading
import time
from dataclasses import asdict
from threading import Thread
import os

import time
import os

from aiogram.fsm.scene import SceneConfig
from click import clear
from random import *

from pydantic import constr

Plents = ["Mars", ]
class Planet():
    def __init__


class Status:
    def __init__(self, Oxygen: float, Energy: float, Fuel: float, HP: float, Planet: str, Score: int):
        self.Planet = Planet
        self.Oxygen = Oxygen
        self.Energy = Energy
        self.Fuel = Fuel
        self.HP = HP
        self.Score = Score

def normal_energy():
    b = s.Energy
    if b<1000: return str(b)+" Wh"
    elif b>=1000 and b<1000000 : return str(round(b/1000, 1))+ " kWH"
    else: return str(round(b/1000000, 1))+"MWh"

s = Status(Planet="Earth", Oxygen=randint(60, 100,), Energy=randint(500, 1000), Fuel=randint(30, 100), HP=100, Score=0)

def get_status():
    print("Planet >>",s.Planet)
    print("Oxygen >>", round(s.Oxygen, 3), "kg ("+str(s.Oxygen//0.09)+" sec)")
    print("Energy >>", normal_energy())
    print("Fuel >>",round(s.Fuel, 1), "kg")
    print("HP >>", round(s.HP, 1))

def do_dig():
    telldot("> > > Your dig a rock and find")
    if s.Planet=="Earth":
        b = s.Fuel
        z = round(uniform(0, 2), 1)
        print(z, "kg of Fuel!")
        print(s.Fuel,">>>",round(b+z, 1))
        s.Fuel+=z


def command():
    print("::: ", end='')
    c = input()
    if c.upper()=="STATUS" or c.upper()=="S":
        get_status()
    elif c.upper()=="FULL ENERGY":
        print(s.Energy)
    elif c.upper()=="DIG":
        do_dig()
    elif c.upper()=="PI" or c.upper()=="PLANET INFO":
        ppr


def tellslow(message, tim: int=2):
    message = str(message)
    time.sleep(tim)
    print(message)


def telldot(z):
    print(z, end="")
    for _ in range(2):
        print(".", end="")
        time.sleep(1)
    print(".")

# telldot("Hello, you're in a space shuttle, in a deep space")
# tellslow("You have command: STATUS(S) | DIG | GO [planet] | RELOAD(R) | PLANET INFO(PI) ")

def oxygen_lost():
    score = 0
    while s.Oxygen>0:
        time.sleep(1)
        s.Oxygen-=0.09
        s.Score+=1

threading.Thread(target=oxygen_lost, daemon=True).start()

while s.Oxygen>0:
    command()
telldot("Oxygen is lost, your death")
print("You score: ", s.Score)


