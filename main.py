import signal

from methods.dig import *
from methods.meteor_method import *
from methods.os_method import *

from animation import *


s.Inventory["Uranium"]+=10
s.Inventory["Iron"]+=10
s.Inventory["Gold"]+=5


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


