import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Status import *
from Inventory import *
<<<<<<< HEAD
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
    
=======

heal = {"소형 체력물약":20,"중형 체력물약":50,"대형 체력물약":100,"특대형 체력물약":200}
mana = {"소형 마나물약":20,"중형 마나물약":50,"대형 마나물약":100,"특대형 마나물약":200}
wearable = {"조잡한 가죽 모자":[0,0,0,0,2],"조잡한 가죽 상의":[0,0,0,0,2],"조잡한 가죽 하의":[0,0,0,0,2],"조잡한 가죽 장갑":[0,0,0,0,2],"조잡한 가죽 신발":[0,0,0,0,2],"나무 검":[0,5,0,0,0],"나무 단검":[0,3,2,0,0],"나무 활":[-10,3,5,0,0],"나무 완드":[0,0,0,5,0]}

def use(name):
    if "체력" in name:
        if Player.max_hp == Player.hp:
            inv.use(name)
            return 0,"rand"
        Player.hp += heal[name]
        if Player.max_hp < Player.hp:
            Player.hp = Player.max_hp
        inv.use(name)
        return heal[name],"heal"
    elif "마나" in name:
        if Player.max_mana == Player.mana:
            inv.use(name)
            return 0,"rand"
        Player.mana += mana[name]
        if Player.max_mana <= Player.mana:
            Player.mana = Player.max_mana
        inv.use(name)
        return mana[name],"mana"
>>>>>>> 859928f8eb14e1b36927ada5b5ea8e966fcb71e1
