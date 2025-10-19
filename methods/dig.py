import threading
import time
from random import randint, uniform

from methods.mainos import s, Mineral, telldot
from colorama import Fore, Style


autd = True

def povez():
    n = randint(0, len(Mineral)-1)
    povez = randint(0, 10)
    if povez < 10:
        s.Inventory[Mineral[n]]+=1
        return str(Mineral[n])
    return None


def do_dig():
    telldot(Fore.GREEN + Style.DIM +"\n> > > Your dig a rock and find"+ Style.RESET_ALL)
    if s.Planet=="Earth":
        n = povez()
        b = s.Fuel
        z = round(uniform(0, 2), 1)
        if n!=None:
            print(Fore.GREEN + Style.DIM + str(round(z, 1)) + " kg of Fuel! + " + n + Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM + str(round(s.Fuel, 1)) + " >>> " + str(round(b + z, 1)) + Style.RESET_ALL)
        else:
            print(Fore.GREEN + Style.DIM + str(round(z, 1)) + " kg of Fuel!" + Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM + str(round(s.Fuel, 1)) + " >>> " + str(round(b + z, 1)) +"\n"+ Style.RESET_ALL)
        s.Fuel+=z


def AutoDigger():
    if s.AutoDiggerActive:
        print("AutoDigger working bro!")
        return

    s.AutoDiggerActive = True


    def dig_loop():
        while True:
            time.sleep(10)
            mineral = povez()
            s.Fuel += round(uniform(0, 2), 1)

    threading.Thread(target=dig_loop, daemon=True).start()
    print("AutoDigger has arrived on your ship!")
