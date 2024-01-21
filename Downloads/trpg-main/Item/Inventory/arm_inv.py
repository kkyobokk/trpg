import pickle
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

arm_equipped = {"helmet":"없음","chestplate":"없음","glove":"없음","leggings":"없음","boots":"없음"}
weapon_equipped = {"main":"없음"}

def init():
    global arm_equipped,weapon_equipped
    with open("./Inventory/ainv_list.pickle",'rb') as fr:
        arm_equipped = pickle.load(fr)
    with open("./Inventory/winv_list.pickle",'rb') as fr:
        weapon_equipped = pickle.load(fr)

def save():
    global arm_equipped,weapon_equipped
    with open("./Inventory/ainv_list.pickle",'wb') as fw:
        pickle.dump(arm_equipped,fw)
    with open("./Inventory/winv_list.pickle",'wb') as fw:
        pickle.dump(weapon_equipped,fw)

def equip(name):
    if "상의" in name:
        arm_equipped["chestplate"] = name
    elif "장갑" in name:
        arm_equipped["glove"] = name
    elif "하의" in name:
        arm_equipped["leggings"] = name
    elif "신발" in name:
        arm_equipped["boots"] = name
    elif "모자" in name:
        arm_equipped["helmet"] = name
    else:
        weapon_equipped["main"] = name

def unequip(name):
    if "상의" in name:
        arm_equipped["chestplate"] = "없음"
    elif "장갑" in name:
        arm_equipped["glove"] = "없음"
    elif "하의" in name:
        arm_equipped["leggings"] = "없음"
    elif "신발" in name:
        arm_equipped["boots"] = "없음"
    elif "모자" in name:
        arm_equipped["helmet"] = "없음"
    else:
        weapon_equipped["main"] = "없음"
