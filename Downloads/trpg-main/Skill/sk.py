import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pickle

skillset = ["파이어볼","없음","없음","없음"]

def init():
    global skillset
    with open("./Skill/skillset.pickle",'rb') as fr:
        skillset = pickle.load(fr)
    return skillset

def save(skillset):
    with open("./Skill/skillset.pickle",'wb') as fw:
        pickle.dump(skillset,fw)

def sk_call(sk,m_def,mag,mana):
    if sk == "없음":
        res = sk1()
    elif sk == "파이어볼":
        damage,mana = fire_ball(m_def,mag,mana)
        return damage,mana

def sk1():
    return 1

def fire_ball(m_def,mag,mana):
    if mana < 10:
        return -1,mana
    else:
        damage = mag*1.5 - m_def
        mana -= 10
        if damage < 0:
            damage = 0
        return damage,mana
