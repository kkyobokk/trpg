import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from Status import *
from Inventory import *

weapons = {"나무 검":100,"나무 단검":100,"나무 활":100,"나무 완드":100}
armors = {"조잡한 가죽 모자":250,"조잡한 가죽 상의":250,"조잡한 가죽 하의":250,"조잡한 가죽 장갑":250,"조잡한 가죽 신발":250}
commons = {"소형 체력물약":50,"중형 체력물약":100,"대형 체력물약":200,"특대형 체력물약":500,"소형 마나물약":100,"중형 마나물약":200,"대형 마나물약":500,"특대형 마나물약":1000}

def wpn_open():
    return weapons

def arm_open():
    return armors

def com_open():
    return commons

def wpn_buy(name,data):
    if data["가격"] > Player.gold:
        return -1
    Player.get(0,-data["가격"])
    inv.equip_add(name,data)
    return 1

def arm_buy(name,data):
    if data["가격"] > Player.gold:
        return -1
    Player.get(0,-data["가격"])
    inv.equip_add(name,data)
    return 1

def com_buy(name):
    if name["가격"] > Player.gold:
        return -1
    Player.get(0,-name["가격"])
    inv.use_add(name)
    return 1