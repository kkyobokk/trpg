import os,sys,random
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Status import Player

max_hp = 0
hp = 0
atk = 0
defend = 0
critical = 0
gold, exp = 0,0

def slime(level):
    global max_hp, hp, atk, defend, critical, gold, exp
    name = f"슬라임 Lv{level**3}"
    max_hp = 10*level**2
    hp = 10*level**2
    atk = 7*level
    defend = 2*level**2
    critical = 10
    gold,exp = 10*level**3,10*level**3
    return name

def rock_slime(level):
    global max_hp, hp, atk, defend, critical, gold, exp
    name = f"바위 슬라임 Lv{level**3}"
    max_hp = 20*level**2
    hp = 20*level**2
    atk = 5*level
    defend = 4*level**2
    critical = 10
    gold,exp = 40*level**3,20*level**3
    return name

def boss(level):
    global max_hp, hp, atk, defend, critical, gold, exp
    max_hp = 1000*level**2
    hp = 1000*level**2
    atk = 100*level
    defend = 100*level
    critical = 10
    gold, exp = 1000*level,1000*level

def attacked(t):
    global hp,defend
    if t == 1:
        hp -= Player.atk*2 - defend
    else:
        hp -= Player.atk - defend
        