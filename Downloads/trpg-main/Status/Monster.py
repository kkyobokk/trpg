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
    name = f"슬라임 Lv{level*level*level}"
    max_hp = 10*level*level
    hp = 10*level*level
    atk = 7*level
    defend = 2*level*level
    critical = 10
    gold,exp = 10*level*level*level,10*level*level*level
    return name

def rock_slime(level):
    global max_hp, hp, atk, defend, critical, gold, exp
    name = f"바위 슬라임 Lv{level*level*level}"
    max_hp = 20*level*level
    hp = 20*level*level
    atk = 5*level
    defend = 4*level*level
    critical = 10
    gold,exp = 40*level*level*level,20*level*level*level
    return name

def boss(level):
    global max_hp, hp, atk, defend, critical, gold, exp
    max_hp = 1000*level*level
    hp = 1000*level*level
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
        