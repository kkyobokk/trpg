import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pickle

use_inv = {}
equip_inv = {}
material_inv = {}
common_inv = {}

def init():
    global use_inv,equip_inv,material_inv,common_inv
    with open("./Inventory/inv_list.pickle",'rb') as fr:
        use_inv = pickle.load(fr)
    with open("./Inventory/einv_list.pickle",'rb') as fr:
        equip_inv = pickle.load(fr)
    with open("./Inventory/minv_list.pickle",'rb') as fr:
        material_inv = pickle.load(fr)
    with open("./Inventory/cinv_list.pickle",'rb') as fr:
        common_inv = pickle.load(fr)

def save():
    global use_inv, equip_inv,material_inv,common_inv
    with open("./Inventory/inv_list.pickle",'wb') as fw:
        pickle.dump(use_inv,fw)
    with open("./Inventory/einv_list.pickle",'wb') as fw:
        pickle.dump(equip_inv,fw)
    with open("./Inventory/minv_list.pickle",'wb') as fw:
        pickle.dump(material_inv,fw)
    with open("./Inventory/cinv_list.pickle",'wb') as fw:
        pickle.dump(common_inv,fw)

def equip_add(name):
    global equip_inv
    if name in equip_inv:
        equip_inv[name] += 1
    else:
        equip_inv[name] = 1
    print(equip_inv)

def equip_remove(name):
    global equip_inv
    if name in equip_inv:
        equip_inv[name] -= 1
        if equip_inv[name] == 0:
            del equip_inv[name]
    else:
        equip_inv[name] = 1
    print(equip_inv)

def use_add(name):
    global use_inv
    if name in use_inv:
        use_inv[name] += 1
    else:
        use_inv[name] = 1

def use(name):
    global use_inv
    use_inv[name] -= 1
