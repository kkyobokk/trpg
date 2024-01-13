import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Status import *
from Inventory import *
import json

items = {}

def init():
    global items
    with open('./Item/items.json','r',encoding='UTF-8-sig') as f:
        data = json.load(f)
        items = data

def save():
    global items
    with open('./Item/items.json','w',encoding='UTF-8-sig') as f:
        json.dump(items,f,ensure_ascii=False,indent=2)

def use(name):
    if name["종류"] == "체력":
        if Player.max_hp == Player.hp:
            inv.use(name)
            return 0,"rand"
        Player.hp += items[name]["특수"]
        if Player.max_hp < Player.hp:
            Player.hp = Player.max_hp
        inv.use(name)
        return items[name]["특수"],"heal"
    elif name["종류"] == "마나":
        if Player.max_mana == Player.mana:
            inv.use(name)
            return 0,"rand"
        Player.mana += items[name]["특수"]
        if Player.max_mana <= Player.mana:
            Player.mana = Player.max_mana
        inv.use(name)
        return items[name]["특수"],"mana"
    