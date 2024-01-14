import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tkinter import *
import random

max_hp = 0
hp = 0
atk = 0
luk = 0
mag = 0
defend = 0
gold = 0
lv = 0
exp = 0
max_exp = 0
stat_point = 0
mana = 0
max_mana = 0
status = []

def init():
    global max_hp,hp,atk,luk,mag,defend,gold,lv,exp,max_exp,stat_point,mana,max_mana,status
    with open("./Status/Player_Status.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = int(line.strip())
            status.append(line)
    max_hp,hp,atk,luk,mag,defend,gold,lv,exp,max_exp,stat_point,mana,max_mana = status
    return status

def save():
    with open("./Status/Player_Status.txt","w") as f:
        f.write(f"{max_hp}\n{hp}\n{atk}\n{luk}\n{mag}\n{defend}\n{gold}\n{lv}\n{exp}\n{max_exp}\n{stat_point}\n{mana}\n{max_mana}")

def atk_up(num):
    global stat_point, atk
    stat_point -= num
    atk += num
    
def luk_up(num):
    global stat_point, luk
    stat_point -= num
    luk += num
    
def mag_up(num):
    global stat_point, mag
    stat_point -= num
    mag += num
    
def hp_up(num):
    global stat_point, hp,max_hp
    stat_point -= num
    max_hp += 5*num
    hp += 5*num

def def_up(num):
    global stat_point, defend
    stat_point -= num
    defend += num

def stat_up(name,num):
    if name == "체력":
        hp_up(num)
    elif name == "힘":
        atk_up(num)
    elif name == "운":
        luk_up(num)
    elif name == "마력":
        mag_up(num)
    elif name == "방어력":
        def_up(num)
    else:
        0

def return_list():
    global max_hp,atk,luk,mag,defend
    stat_list = [["체력",max_hp],["힘",atk],["운",luk],["마력",mag],["방어력",defend]]
    return stat_list

def level_up():
    global stat_point, exp, lv, hp, max_hp, max_exp
    lv += 1
    exp -= max_exp
    if lv < 10:
        max_exp += 20
    elif lv < 20 and lv >= 10:
        max_exp += 50
    elif lv < 40 and lv >= 20:
        max_exp += 100
    else:
        max_exp = max_exp*2
    stat_point += 3
    hp = max_hp

def attacked(atk):
    global hp, defend
    hp -= atk - defend

def get(gexp,ggold):
    global exp, gold
    exp += gexp
    gold += ggold

def arm_stat(stat):
    print(stat)
    global max_hp,hp,atk,luk,mag,defend
    max_hp += stat[0]
    if max_hp < hp:
        hp = max_hp
    atk += stat[1]
    luk += stat[2]
    mag += stat[3]
    defend += stat[4]
    print(atk)

def unequip_arm_stat(stat):
    global max_hp,hp,atk,luk,mag,defend
    max_hp -= stat[0]
    if max_hp < hp:
        hp = max_hp
    atk -= stat[1]
    luk -= stat[2]
    mag -= stat[3]
    defend -= stat[4]