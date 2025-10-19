
from methods.mainos import s


def repair():
    i = s.Inventory["Iron wall"]
    g = s.Inventory["Golden wall"]
    hp = 0
    z = s.HP
    if i>=1 or g>=1:
        s.HP+= i*20
        hp+= i*20
        s.Inventory["Iron wall"]=0
        s.HP+= g*50
        hp+= g*50
        s.Inventory["Golden wall"]=0
        print(f"> HP {z} => {z+hp}\n"
              f"-x{i} Iron wall\n"
              f"-x{g} Golden wall")
    else:
        print("You need more thing..")
