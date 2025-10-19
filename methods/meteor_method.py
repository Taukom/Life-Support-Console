from random import randint
from colorama import Fore, Back, Style, init
from methods.mainos import s
init(autoreset=True)

def meteor():
    r = randint(0, 1000)
    di = randint(1, 50)
    if r>950:
        print(Fore.RED+f"\n\n[System] Meteorite {di} kg crashed into a shutle!"+ Style.RESET_ALL)
        print(Fore.RED+Style.DIM+f"{s.HP} HP >>> {s.HP-di} HP, repair your ship!\n"+ Style.RESET_ALL)
        print("::: ", end="")
        s.HP-=di