from methods.mainos import s


def normal_energy():
    b = s.Energy
    if b<1000: return str(b)+" Wh"
    elif b>=1000 and b<1000000 : return str(round(b/1000, 1))+ " kWH"
    else: return str(round(b/1000000, 1))+"MWh"