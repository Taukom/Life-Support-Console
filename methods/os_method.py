import time
from random import randint

from animation import explode_ship, atomic_city
from methods.craft import craft
from methods.dig import do_dig
from methods.energy import normal_energy
from methods.mainos import s
from methods.shuttle import repair
from colorama import Fore, Style


def get_status():
    print(Fore.GREEN + Style.DIM +f"Planet >> {s.Planet}"+ Style.RESET_ALL)
    print(Fore.GREEN + Style.DIM +f"Oxygen >> {round(s.Oxygen, 3)} kg {s.Oxygen//0.09} sec"+ Style.RESET_ALL)
    print(Fore.GREEN + Style.DIM +f"Energy >>  {normal_energy()}"+ Style.RESET_ALL)
    print(Fore.GREEN + Style.DIM +f"Fuel >> {round(s.Fuel, 1)} kg {get_inv()}"+ Style.RESET_ALL)
    print(Fore.GREEN + Style.DIM +f"HP >> {round(s.HP, 1)}"+ Style.RESET_ALL)


def get_inv():
    st = ''
    i = s.Inventory
    date = list(i.keys())
    date2 = list(i.values())
    for x in range(len(date)):
        if date2[x]!=0:
            st += " x" + str(date2[x]) + " " + str(date[x])

    return st


def help():
    print("> STATUS(s)\n"
          "> PLANET INFO(PI)\n"
          "> DIG\n"
          "> GO [planet]\n"
          "> CRAFT\n"
          "> FULL ENERGY\n"
          "> PLANET LIST(PL)\n"
          "> ATTACK\n"
          "> REPAIR\n"
          "> AUTODIGGER")




def command():
    print("::: ", end='')
    c = input()
    if c.upper()=="STATUS" or c.upper()=="S":
        get_status()
    elif c.upper()=="FULL ENERGY":
        print(s.Energy)
    elif c.upper()=="DIG":
        do_dig()
    elif c.upper()=="SYS" or c.upper()=="SS" or c.upper()=="SYSTEM":
        help()
    elif c.upper()=="ATOMIC BOMB":
        if s.Inventory["Atomic bomb"]>=1:
            explode_ship(score=s.Score)
        else:
            print("\n You need 1x Atomic Bomb")

    elif c.upper()=="REPAIR":
        repair()
    elif c.upper().count("CRAFT")==1:
        if len(c)==5:
            craft()
        else:
            craft(c[6:].upper())
    elif c.upper()=="ATOMIC BOMB CITY":
        if s.Inventory["Atomic bomb"]>=1:
            s.Inventory["Atomic bomb"]-=1
            atomic_city( width=120, height=50, fps=8, duration=15)
            i = randint(60, 200)
            b = randint(12, 58)
            print(f"> > > +x{i} Iron\n"
                  f"> > > +x{b} Gold")
            s.Inventory["Iron"]+=i
            s.Inventory["Gold"]+=b
        else:
            print("\n You need 1x Atomic Bomb")

