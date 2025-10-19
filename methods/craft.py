from methods.dig import AutoDigger
from methods.mainos import s
import subprocess

def craft(item: str=None):
    i = s.Inventory
    if item==None:
        return print("You can craft: \n"
                "Iron wall - x5 Iron\n"
                "Golden wall - x5 Gold\n"
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
                         "+AutoDigger")

        else:
            return print("You wanna more resurses bro")

    elif item=="ATOMIC BOMB":
        if i["Uranium"]>=10:
            s.Inventory["Atomic bomb"]+=1
            s.Inventory["Uranium"]-=5
            return print("-10 Uranium \n"
                         "+Atomic Bomb")
        else:
            return print("You wanna more uranium bro")

    elif item=="GOLDEN WALL":
        if i["Gold"]>=5:
            s.Inventory["Golden wall"]+=1
            s.Inventory["Gold"]-=5
            return print("-5 Gold \n"
                         "+1 Golden wall")
        else:
            return print("You wanna more Iron bro")