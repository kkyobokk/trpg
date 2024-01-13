import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pickle
import json

inv = {"use_inv":{},"equip_inv":{},"material_inv":{},"common_inv":{},"equipped_inv":{"helmet":"없음","chestplate":"없음","glove":"없음","leggings":"없음","boots":"없음","weapon":"없음"}}

def init():
    global inv
    with open('./Inventory/inv.json','r',encoding='UTF-8-sig') as f:
        data = json.load(f)
        inv = data

def save():
    global inv
    with open("./Inventory/inv.json",'w',encoding='UTF-8-sig') as f:
        json.dump(inv,f,ensure_ascii=False,indent=2)

def equip_add(name,stat):
    global inv
    if name.keys in inv["equip_inv"]:
        inv["equip_inv"][name]["수량"] += 1
    else:
        inv["equip_inv"][name] = {"수량":1,"스탯":stat,"등급":"조잡"}

def equip_remove(name):
    global inv
    inv["equip_inv"][name]["수량"] -= 1
    if inv["equip_inv"][name]["수량"] == 0:
        del inv["equip_inv"][name]
    print(inv["equip_inv"])

def use_add(name):
    global inv
    if name in inv["use_inv"]:
        inv["use_inv"][name] += 1
    else:
        inv["use_inv"][name] = 1

def use(name):
    global inv
    inv["use_inv"][name] -= 1
    if inv["use_inv"][name] == 0:
        del inv["use_inv"][name]

def equip(name):
    if name["종류"] == "상의":
        inv["equipped_inv"]["chestplate"] = name.keys[0]
    elif name["종류"] == "장갑":
        inv["equipped_inv"]["glove"] = name.keys[0]
    elif name["종류"] == "하의":
        inv["equipped_inv"]["leggings"] = name.keys[0]
    elif name["종류"] == "신발":
        inv["equipped_inv"]["boots"] = name.keys[0]
    elif name["종류"] == "모자":
        inv["equipped_inv"]["helmet"] = name.keys[0]
    elif name["종류"] == "무기":
        inv["equipped_inv"]["weapon"] = name.keys[0]
    else:
        return 0

def unequip(name):
    if name["부위"] == "상의":
        inv["equipped_inv"]["chestplate"] = "없음"
    elif name["부위"] == "장갑":
        inv["equipped_inv"]["glove"] = "없음"
    elif name["부위"] == "하의":
        inv["equipped_inv"]["leggings"] = "없음"
    elif name["부위"] == "신발":
        inv["equipped_inv"]["boots"] = "없음"
    elif name["부위"] == "모자":
        inv["equipped_inv"]["helmet"] = "없음"
    elif name["부위"] == "무기":
        inv["equipped_inv"]["weapon"] = "없음"
    else:
        return 0