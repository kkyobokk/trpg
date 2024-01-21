from Status import *
from tkinter import *
import tkinter.ttk as ttk
from Item import *
from Skill import *
from Event import *
from Inventory import *
import shutil, winsound, os, random

root = os.path.dirname(os.path.realpath(__file__))

def cache_rm():
    for (path,dir,files) in os.walk(os.getcwd()):
        for dirname in dir:
            cordir = f'{path}\{dirname}'
            if '__pycache__' in dirname:
                shutil.rmtree(cordir)

def dungeon_window(name):
    log_delete_all()
    log_append("일반던전에 입장하였습니다.")
    window.place(x=0,y=0)
    status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")
    monster_label.config(text=f"{name}")
    monster_hp_label.config(text=f"{Monster.hp} / {Monster.hp}")
    window.tkraise()

def boss_window():
    Monster.boss(1)
    log_append("보스던전에 입장하였습니다.")
    window.place(x=0,y=0)
    status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")
    monster_label.config(text="보스 몬스터")
    monster_hp_label.config(text=f"{Monster.hp} / {Monster.hp}")
    window.tkraise()

def stat_window():
    log_delete_all()
    try:
        for row in stat_tree.get_children():
            stat_tree.delete(row)
    except:
        0
    stat_list = Player.return_list()        
    for i in range(len(stat_list)):
        stat_tree.insert('','end',values=stat_list[i],iid=i)
    stat_frame.place(x=0,y=0)
    sp_label.config(text=f"잔여 스탯 : {Player.stat_point}")
    stat_name_label.config(text=f"스탯 : X")
    stat_amount_label.config(text="소모 잔여 스탯 : 0")
    stat_frame.tkraise()

def mission_window():
    try:
        for row in mission_tree.get_children():
            mission_tree.delete(row)
    except:
        0
    log_delete_all()
    mission_tree.insert('','end',values=[mission.slime_step1["name"],mission.slime_step1["level"]],iid=0)
    mission_tree.insert('','end',values=[mission.slime_step2["name"],mission.slime_step2["level"]],iid=1)
    mission_frame.place(x=0,y=0)
    mission_frame.tkraise()


def store_window():
    log_delete_all()
    cur_gold.config(text=f"보유한 골드 : {Player.gold}")
    store_frame.place(x=0,y=0)
    store_frame.tkraise()

def wpn_store_window():
    log_delete_all()
    try:
        for row in wpn_store_tree.get_children():
            wpn_store_tree.delete(row)
    except:
        0
    i = []
    for j in store.wpn_open().keys():
        i.append([j,store.wpn_open()[j]])
    for k in range(len(i)):
        wpn_store_tree.insert('','end',values=i[k],iid=k)
    wpn_store_frame.place(x=0,y=0)
    wpn_store_frame.tkraise()

def arm_store_window():
    log_delete_all()
    try:
        for row in arm_store_tree.get_children():
            arm_store_tree.delete(row)
    except:
        0
    i = []
    for j in store.arm_open().keys():
        i.append([j,store.arm_open()[j]])
    for k in range(len(i)):
        arm_store_tree.insert('','end',values=i[k],iid=k)
    arm_store_frame.place(x=0,y=0)
    arm_store_frame.tkraise()

def com_store_window():
    log_delete_all()
    try:
        for row in com_store_tree.get_children():
            com_store_tree.delete(row)
    except:
        0
    i = []
    for j in store.com_open().keys():
        i.append([j,store.com_open()[j]])
    for k in range(len(i)):
        com_store_tree.insert('','end',values=i[k],iid=k)
    com_store_frame.place(x=0,y=0)
    com_store_frame.tkraise()

def inv_window():
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    inv_frame.tkraise()

def ck_tab(event):
    ck = inv_note.tab(inv_note.select(),"text")
    if ck == "장비":
        try:
            for row in equip_tree.get_children():
                equip_tree.delete(row)
        except:
            0
        i = []
        for j in inv.equip_inv.keys():
            i.append([j,inv.equip_inv[j]])
        for k in range(len(i)):
            equip_tree.insert('','end',values=i[k],iid=k)
    elif ck == "소비":
        try:
            for row in use_tree.get_children():
                use_tree.delete(row)
        except:
            0
        i = []
        for j in inv.use_inv.keys():
            i.append([j,inv.use_inv[j]])
        for k in range(len(i)):
            use_tree.insert('','end',values=i[k],iid=k)
    elif ck == "재료":
        try:
            for row in mat_tree.get_children():
                mat_tree.delete(row)
        except:
            0
        i = []
        for j in inv.material_inv.keys():
            i.append([j,inv.material_inv[j]])
        for k in range(len(i)):
            mat_tree.insert('','end',values=i[k],iid=k)
    elif ck == "기타":
        try:
            for row in comm_tree.get_children():
                comm_tree.delete(row)
        except:
            0
        i = []
        for j in inv.common_inv.keys():
            i.append([j,inv.common_inv[j]])
        for k in range(len(i)):
            comm_tree.insert('','end',values=i[k],iid=k)

def wpn_buy(event):
    selected = wpn_store_tree.focus()
    selected_name = wpn_store_tree.item(selected)["values"][0]
    result = store.wpn_buy(selected_name)
    if result == -1:
        log_append("골드가 부족합니다!")
    else:
        log_append(f"{selected_name}을(를) 구입하였습니다!")

def arm_buy(event):
    selected = arm_store_tree.focus()
    selected_name = arm_store_tree.item(selected)["values"][0]
    result = store.arm_buy(selected_name)
    if result == -1:
        log_append("골드가 부족합니다!")
    else:
        log_append(f"{selected_name}을(를) 구입하였습니다!")

def com_buy(event):
    selected = com_store_tree.focus()
    selected_name = com_store_tree.item(selected)["values"][0]
    result = store.com_buy(selected_name)
    if result == -1:
        log_append("골드가 부족합니다!")
    else:
        log_append(f"{selected_name}을(를) 구입하였습니다!")

def save():
    Player.save()
    inv.save()
    sk.save(skillset)

def close():
    Player.save()
    window.destroy()
    window.quit()
    inv.save()
    sk.save(skillset)

def attack():
    critical_per = random.randint(1,100)
    monster_label.config(fg="red")
    if critical_per <= Player.luk:
        if Player.atk*2 - Monster.defend < 0:
            log_append(f"{monster_label.cget('text')}이(가) 일반공격으로 아무런 피해도 입지 않았습니다!")
        else:
            Monster.attacked(1)
            log_append(f"{monster_label.cget('text')}이(가) 일반공격으로 {Player.atk*2 - Monster.defend}의 크리티컬 피해를 받았습니다!")
    else:
        if Player.atk - Monster.defend < 0:
            log_append(f"{monster_label.cget('text')}이(가) 일반공격으로 아무런 피해도 입지 않았습니다!")
        else:
            winsound.PlaySound('./1_sound/attack.mp3',winsound.SND_ASYNC)
            Monster.attacked(0)
            log_append(f"{monster_label.cget('text')}이(가) 일반공격으로 {Player.atk - Monster.defend}의 피해를 받았습니다!")
    attack_button.config(state="disabled")
    skill_button.config(state="disabled")
    item_button.config(state="disabled")
    run_button.config(state="disabled")
    if Monster.hp <= 0:
        window1.after(500,monster_dead)
    else:
        monster_hp_label.config(text=f"{Monster.hp} / {Monster.max_hp}")
        window1.after(500,attacked)
        
def attacked():
    critical_per = random.randint(1,100)
    if critical_per <= Monster.critical:
        if Monster.atk+2 < Player.defend:
            log_append("아무런 피해도 입지 않았습니다!")
        else:
            Player.attacked(Monster.atk*2)
            log_append(f"{Monster.atk*2 - Player.defend}의 크리티컬 피해를 받았습니다!")
    else:
        if Monster.atk < Player.defend:
            log_append("아무런 피해도 입지 않았습니다!")
        else:
            Player.attacked(Monster.atk)
            log_append(f"{Monster.atk - Player.defend}의 피해를 받았습니다!")
    if Player.hp <= 0:
        window1.after(500,dead)
    else:
        attack_button.config(state="normal")
        skill_button.config(state="normal")
        item_button.config(state="normal")
        run_button.config(state="normal")
        status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")

def monster_dead():
    Monster.hp = Monster.max_hp
    monster_hp_label.config(text=f"{Monster.hp} / {Monster.max_hp}")
    log_append(f"{monster_label.cget('text')}이(가) 처치되었습니다!")
    Player.get(Monster.exp,Monster.gold)
    log_append(f"{Monster.gold}G와 {Monster.exp}의 경험치를 획득했습니다.")
    if Player.exp >= Player.max_exp:
        window1.after(500,level_up)
    else:
        attack_button.config(state="normal")
        skill_button.config(state="normal")
        item_button.config(state="normal")
        run_button.config(state="normal")
        status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")

def dead():
    log_append("사망했습니다...")
    log_append(f"사망 패널티로 {round(Player.exp*0.5)}의 경험치와 {round(Player.gold*0.4)}G를 잃었습니다...")
    Player.exp -= round(Player.exp*0.5)
    Player.gold -= round(Player.gold*0.4)
    Monster.hp = Monster.max_hp
    Player.hp = round(Player.max_hp*0.5)
    monster_hp_label.config(text=f"{Monster.hp} / {Monster.max_hp}")
    attack_button.config(state="normal")
    skill_button.config(state="normal")
    item_button.config(state="normal")
    run_button.config(state="normal")
    status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")

def level_up():
    while Player.exp >= Player.max_exp:
        Player.level_up()
        log_append("레벨 업!")
    attack_button.config(state="normal")
    skill_button.config(state="normal")
    item_button.config(state="normal")
    run_button.config(state="normal")
    status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")

def skill():
    skill_Frame.place(x=25,y=250)
    skill_Frame.tkraise()

def sk1():
    global skillset
    damage,Player.mana = sk.sk_call(skillset[0],Monster.defend, Player.mag, Player.mana)
    if damage == -1:
        log_append(f"스킬 : {skillset[0]}(을)를 사용할 수 없습니다!")
    else:
        Monster.hp -= damage
        log_append(f"스킬 : {skillset[0]}(으)로 {damage}의 피해를 입혔습니다.")
        window.tkraise()
        if Monster.hp <= 0:
            window1.after(500,monster_dead)
        else:
            monster_hp_label.config(text=f"{Monster.hp} / {Monster.max_hp}")
            window1.after(500,attacked)

def back():
    window.tkraise()

def item_screen():
    item_list_frame.place(x=25,y=250)
    try:
        for row in item_tree.get_children():
            item_tree.delete(row)
    except:
        0
    i = []
    for j in inv.use_inv.keys():
        i.append([j,inv.use_inv[j]])
    for k in range(len(i)):
        item_tree.insert('','end',values=i[k],iid=k)
    item_list_frame.tkraise()
    
def item_use(event):
    selected = item_tree.focus()
    selected_name = item_tree.item(selected)["values"][0]
    if selected == ():
        return 0
    num,type=item.use(selected_name)
    if type == "heal":
        log_append(f"체력을 {num}만큼 회복했습니다!")
    elif type == "mana":
        log_append(f"마나를 {num}만큼 회복했습니다!")
    elif type == "rand":
        log_append("당신은 맛있게 포션을 먹었지만, 아무런 효과도 없었습니다... 그래도 맛은 있네요!")
    status_label.config(text=f"HP : {Player.hp}/{Player.max_hp}  MP : {Player.mana}/{Player.max_mana}  Lv : {Player.lv}  {Player.exp}/{Player.max_exp}  {Player.gold}G")
    for row in item_tree.get_children():
            item_tree.delete(row)
    i = []
    for j in inv.use_inv.keys():
        i.append([j,inv.use_inv[j]])
    for k in range(len(i)):
        item_tree.insert('','end',values=i[k],iid=k)
    window.tkraise()
    window1.after(500,attacked)

def map_adrian():
    log_delete_all()
    map1 = Label(map_Frame,image=map_Adrian_img)
    map1.place(x=0,y=0)
    woods = Button(map_Frame,image=Woods_Adrian_img,background="white",bd=0,highlightthickness=0,command=Adrian_woods)
    town = Button(map_Frame,image=Town_Adrian_img,background="white",bd=0,highlightthickness=0,command=Adrian_town)
    mountain = Button(map_Frame,image=Mountain_Adrian_img,background="white",bd=0,highlightthickness=0,command=Adrian_mountain)
    woods.place(x=40,y=170)
    town.place(x=240,y=360)
    mountain.place(x=300,y=157)
    map_Frame.tkraise()

def Adrian_woods():
    name = log_list.get(1.0,1.6)
    if name == "아드리안 숲":
        dungeon_window(Monster.slime(1))
    else:
        log_delete_all()
        log_append("입장하려면 다시 한번 이미지를 눌러주세요")
        log_append("")
        log_append("설명 : 아드리안 왕국과 가장 가까운 숲이다. 깊게 들어가지 않도록 조심하자.")
        log_append("")
        log_append("적정 레벨 : 1Lv")
        log_append("")
        log_append("아드리안 숲")

def Adrian_mountain():
    name = log_list.get(1.0,1.7)
    if name == "아드리안 설산":
        dungeon_window(Monster.rock_slime(2))
    else:
        log_delete_all()
        log_append("입장하려면 다시 한번 이미지를 눌러주세요")
        log_append("")
        log_append("설명 : 아드리안 왕국과 가장 가까운 산이다. 산에서 실종된 등반가들이 많으니 조심하자.")
        log_append("")
        log_append("적정 레벨 : 10Lv")
        log_append("")
        log_append("아드리안 설산")

def Adrian_town():
    log_delete_all()
    log_append("입장")
    log_append("")
    log_append("설명 : 주변에 몬스터가 약해 평화로운 마을이다. 초보 모험가에게 알맞은 왕국으로 불리운다.")
    log_append("")
    log_append("아드리안 왕국")


def stat_name_clicked(event):
    selected = stat_tree.focus()
    selected_name = stat_tree.item(selected)["values"][0]
    stat_name_label.config(text=f"스탯 : {selected_name}")

def statup1():
    num = int(stat_amount_label.cget("text").split()[4])
    if num +1 <= Player.stat_point:
        stat_amount_label.config(text=f"소모 잔여 스탯 : {num+1}")
    else:
        log_append("잔여 스탯이 부족합니다!")

def statup10():
    num = int(stat_amount_label.cget("text").split()[4])
    if num +10 <= Player.stat_point:
        stat_amount_label.config(text=f"소모 잔여 스탯 : {num+10}")
    else:
        log_append("잔여 스탯이 부족합니다!")

def statupall():
    stat_amount_label.config(text=f"소모 잔여 스탯 : {Player.stat_point}")

def statup_check():
    name = stat_name_label.cget("text").split()[2]
    num = int(stat_amount_label.cget("text").split()[4])
    if name == "X":
        log_append("증가시킬 스탯을 선택해주세요!")
        return 0
    if num == 0:
        log_append("소모할 잔여 스탯을 선택해주세요!")
        return 0
    Player.stat_up(name,num)
    for row in stat_tree.get_children():
        stat_tree.delete(row)
    stat_list = Player.return_list()
    stat_amount_label.config(text="소모 잔여 스탯 : 0")
    sp_label.config(text=f"잔여 스탯 : {Player.stat_point}")     
    for i in range(len(stat_list)):
        stat_tree.insert('','end',values=stat_list[i],iid=i)

def statup_reset():
    stat_name_label.config(text=f"스탯 : X")
    stat_amount_label.config(text="소모 잔여 스탯 : 0")

def log_append(log):
    log_list.config(state="normal")
    log_list.insert(0.0,f"{log}\n")
    log_list.config(state="disabled")

def log_delete_all():
    log_list.config(state="normal")
    log_list.delete(0.0,END)
    log_list.config(state="disabled")

def mission_detail(event):
    log_delete_all()
    selected = mission_tree.focus()
    selected_name = mission_tree.item(selected)["values"][0]
    if selected_name == mission.slime_step1["name"]:
        log_append("*********************************************************")
        log_append("")
        log_append("")
        log_append(mission.slime_step1["detail"])
        log_append("")
        log_append(mission.slime_step1["mission"])
        log_append("")
        log_append(str(mission.slime_step1["reward"])+"G")
        log_append("")
        log_append(mission.slime_step1["level"])
        log_append("")
        log_append(mission.slime_step1["name"])
        log_append("")
        log_append("")
        log_append("*********************************************************")
    if selected_name == mission.slime_step2["name"]:
        log_append("*********************************************************")
        log_append("")
        log_append("")
        log_append(mission.slime_step2["detail"])
        log_append("")
        log_append(mission.slime_step2["mission"])
        log_append("")
        log_append(str(mission.slime_step2["reward"])+"G"+" + "+mission.slime_step2["+reward"])
        log_append("")
        log_append(mission.slime_step2["level"])
        log_append("")
        log_append(mission.slime_step2["name"])
        log_append("")
        log_append("")
        log_append("*********************************************************")

def equip(event):
    selected = equip_tree.focus()
    selected_name = equip_tree.item(selected)["values"][0]
    arm_inv.equip(selected_name)
    Player.arm_stat(item.wearable[selected_name])
    inv.equip_remove(selected_name)
    helmet_label.config(text=f"모자 : {arm_inv.arm_equipped['helmet']}")
    chestplate_label.config(text=f"상의 : {arm_inv.arm_equipped['chestplate']}")
    glove_label.config(text=f"장갑 : {arm_inv.arm_equipped['glove']}")
    leggings_label.config(text=f"하의 : {arm_inv.arm_equipped['leggings']}")
    boots_label.config(text=f"신발 : {arm_inv.arm_equipped['boots']}")
    weapon_label.config(text=f"무기 : {arm_inv.weapon_equipped['main']}")
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)

def helmet_unequip(event):
    name = helmet_label.cget("text").split(":")[1][1:]
    arm_inv.unequip(name)
    inv.equip_add(name)
    Player.unequip_arm_stat(item.wearable[name])
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    helmet_label.config(text=f"모자 : {arm_inv.arm_equipped['helmet']}")

def chestplate_unequip(evnet):
    name = chestplate_label.cget("text").split(":")[1][1:]
    arm_inv.unequip(name)
    inv.equip_add(name)
    Player.unequip_arm_stat(item.wearable[name])
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    chestplate_label.config(text=f"상의 : {arm_inv.arm_equipped['chestplate']}")
    
def leggings_unequip(event):
    name = leggings_label.cget("text").split(":")[1][1:]
    arm_inv.unequip(name)
    inv.equip_add(name)
    Player.unequip_arm_stat(item.wearable[name])
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    leggings_label.config(text=f"하의 : {arm_inv.arm_equipped['leggings']}")

def glove_unequip(event):
    name = glove_label.cget("text").split(":")[1][1:]
    arm_inv.unequip(name)
    inv.equip_add(name)
    Player.unequip_arm_stat(item.wearable[name])
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    glove_label.config(text=f"장갑 : {arm_inv.arm_equipped['glove']}")

def boots_unequip(event):
    name = boots_label.cget("text").split(":")[1][1:]
    arm_inv.unequip(name)
    inv.equip_add(name)
    Player.unequip_arm_stat(item.wearable[name])
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    boots_label.config(text=f"신발 : {arm_inv.arm_equipped['boots']}")

def weapon_unequip(event):
    name = weapon_label.cget("text").split(":")[1][1:]
    arm_inv.unequip(name)
    inv.equip_add(name)
    Player.unequip_arm_stat(item.wearable[name])
    try:
        for row in equip_tree.get_children():
            equip_tree.delete(row)
    except:
        0
    i = []
    for j in inv.equip_inv.keys():
        i.append([j,inv.equip_inv[j]])
    for k in range(len(i)):
        equip_tree.insert('','end',values=i[k],iid=k)
    weapon_label.config(text=f"무기 : {arm_inv.weapon_equipped['main']}")


#-------------------------------------스탯-------------------------------------------
Player.init()
inv.init()
skillset = sk.init()
#------------------------------------------------------------------------------------

#-------------------------------------메인-------------------------------------------
window1 = Tk()
window1.title("TRPG")
window1.geometry("1000x500")
window1.resizable(False,False)
#------------------------------------------------------------------------------------

#-------------------------------------전투-------------------------------------------
window = Frame(window1, width=500, height=500, relief="solid", background="white")
status_label = Label(window, background="white", font=("Aria",12))
status_label.pack()
monster_label = Label(window, font=("Aria", 20), width=31,height=7, background="white",)
monster_label.pack()
monster_hp_label = Label(window, font=("Aria", 15), width=31,height=1, background="white")
monster_hp_label.pack()
white_space = Label(window, width=50,height=50, background="white")
white_space.pack()

#공격
attack_button = Button(window, text="공격", command=attack, width=30, height=5)
attack_button.place(x=25,y=290)

#스킬
skill_button = Button(window, text="스킬", command=skill, width=30, height=5)
skill_button.place(x=255, y=290)
skill_Frame = Frame(window1, width=450, height=300, relief="solid", bg="white")
skill1 = Button(skill_Frame, text=f"{skillset[0]}", width=30, height=5, command=sk1)
skill2 = Button(skill_Frame, text=f"{skillset[1]}", width=30, height=5)
skill3 = Button(skill_Frame, text=f"{skillset[2]}", width=30, height=5)
skill4 = Button(skill_Frame, text=f"{skillset[3]}", width=30, height=5)
skill_back = Button(skill_Frame, text="X", width=3,height=1, font=("Aria",14), command=back)
skill_back.place(x=410,y=0)
skill1.place(x=0,y=40)
skill2.place(x=230,y=40)
skill3.place(x=0,y=140)
skill4.place(x=230,y=140)

#아이템
item_button = Button(window, text="아이템", command=item_screen,width=30, height=5)
item_button.place(x=25, y=390)
item_list_frame = Frame(window1, width=450, height=300, relief="solid", bg="white")
item_list_back = Button(item_list_frame, text="X", width=3,height=1, font=("Aria",14), command=back)
item_list_back.place(x=410,y=0)
item_tree = ttk.Treeview(item_list_frame, columns=["name","amount"], displaycolumns=["name","amount"],show="headings",padding=0,height=4)
item_tree.column("name",anchor="center",width=355)
item_tree.column("amount",anchor="center",width=89)
item_tree.heading("name",text="아이템",anchor="center")
item_tree.heading("amount",text="수량",anchor="center")
item_tree.bind('<Double-Button>',item_use)
item_tree.place(x=0,y=37)

#도망
run_button = Button(window, text="도망가기", width=30, height=5 )
run_button.place(x=255, y=390)
#------------------------------------------------------------------------------------

#------------------------------------스탯창------------------------------------------
stat_frame = Frame(window1, width=500, height=500, relief="flat", background="white")
stat_space = Label(stat_frame, width=71, height=70, bg="white")
stat_space.place(x=-1,y=0)

sp_label = Label(stat_frame,text=f"잔여 스탯 : {Player.stat_point}",background="white",height=3,font=(None,16))
sp_label.place(x=190,y=0)

stat_tree = ttk.Treeview(stat_frame, columns=["name","current"], displaycolumns=["name","current"],show="headings",padding=0,height=5)
stat_tree.place(x=0,y=70)

style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 12))
style.configure("Treeview", font=(None, 12))
style.configure("Treeview",rowheight=40)

stat_tree.column("name",anchor="center",width=249)
stat_tree.column("current",anchor="center",width=250)

stat_tree.heading("name",text="스탯 목록",anchor="center")
stat_tree.heading("current",text="현재 스탯",anchor="center")

stat_list = Player.return_list()
for i in range(len(stat_list)):
    stat_tree.insert('','end',values=stat_list[i],iid=i)

stat_tree.bind("<ButtonRelease-1>",stat_name_clicked)

stat1 = Button(stat_frame,text="스탯 +1",relief="groove",bg="white",width=10,height=2,font=(None,12),command=statup1)
stat1.place(x=50,y=320)
stat10 = Button(stat_frame,text="스탯 +10",relief="groove",bg="white",width=10,height=2,font=(None,12),command=statup10)
stat10.place(x=200,y=320)
stat_all = Button(stat_frame,text="스탯 +all",relief="groove",bg="white",width=10,height=2,font=(None,12),command=statupall)
stat_all.place(x=350,y=320)

stat_name_label = Label(stat_frame,text="스탯 : X",font=(None,12),background="white")
stat_name_label.place(x=20,y=380)
stat_amount_label = Label(stat_frame,text="소모 잔여 스탯 : 0",font=(None,12),background="white")
stat_amount_label.place(x=200,y=380)

stat_check = Button(stat_frame,text="결정",relief="groove",bg="white",width=33,height=3,font=(None,12),command=statup_check)
stat_reset = Button(stat_frame,text="초기화",relief="groove",bg="white",width=13,height=3,font=(None,12),command=statup_reset)
stat_check.place(x=20,y=420)
stat_reset.place(x=350,y=420)

#------------------------------------------------------------------------------------

#------------------------------------의뢰--------------------------------------------
mission_frame = Frame(window1, width=500, height=500, relief="flat", background="white")
mission_frame.place(x=0,y=0)


mission_tree = ttk.Treeview(mission_frame, columns=["name","level"], displaycolumns=["name","level"],show="headings",padding=0,height=10)
mission_tree.place(x=5,y=10)



mission_tree.column("name",anchor="center",width=244)
mission_tree.column("level",anchor="center",width=245)
mission_tree.heading("name",text="의뢰 목록",anchor="center")
mission_tree.heading("level",text="난이도",anchor="center")
mission_tree.bind("<ButtonRelease-1>",mission_detail)

#------------------------------------------------------------------------------------

#-------------------------------------상점-------------------------------------------
#기본 상점
store_frame = Frame(window1, width=500, height=500, relief="flat", background="white")
cur_gold = Label(store_frame, text=f"보유한 골드 : {Player.gold}", bg="white",font=(None,13))
cur_gold.place(x=170,y=20)
wpn_button = Button(store_frame, text="무기 상점", width=32, height=6, command=wpn_store_window, font=("Aria",15))
wpn_button.place(x=70, y=55)
wpn_button = Button(store_frame, text="방어구 상점",width=32, height=6, command=arm_store_window, font=("Aria",15))
wpn_button.place(x=70, y=195)
wpn_button = Button(store_frame, text="잡화 상점", width=32, height=6, command=com_store_window, font=("Aria",15))
wpn_button.place(x=70, y=335)

#무기 상점
wpn_store_frame = Frame(window1, width=500, height=500, relief="flat", background="white")
wpn_store_tree = ttk.Treeview(wpn_store_frame, columns=["name","gold"], displaycolumns=["name","gold"],show="headings",padding=0,height=11)
wpn_store_tree.column("name",anchor="center",width=350)
wpn_store_tree.column("gold",anchor="center",width=140)
wpn_store_tree.heading("name",text="아이템",anchor="center")
wpn_store_tree.heading("gold",text="가격",anchor="center")
wpn_store_tree.bind('<Double-Button>',wpn_buy)
wpn_store_tree.place(x=5,y=10)

#방어구 상점
arm_store_frame = Frame(window1, width=500, height=500, relief="flat", background="white")
arm_store_tree = ttk.Treeview(arm_store_frame, columns=["name","gold"], displaycolumns=["name","gold"],show="headings",padding=0,height=11)
arm_store_tree.column("name",anchor="center",width=350)
arm_store_tree.column("gold",anchor="center",width=140)
arm_store_tree.heading("name",text="아이템",anchor="center")
arm_store_tree.heading("gold",text="가격",anchor="center")
arm_store_tree.bind('<Double-Button>',arm_buy)
arm_store_tree.place(x=5,y=10)

#집화 상점
com_store_frame = Frame(window1, width=500, height=500, relief="flat", background="white")
com_store_tree = ttk.Treeview(com_store_frame, columns=["name","gold"], displaycolumns=["name","gold"],show="headings",padding=0,height=11)
com_store_tree.column("name",anchor="center",width=350)
com_store_tree.column("gold",anchor="center",width=140)
com_store_tree.heading("name",text="아이템",anchor="center")
com_store_tree.heading("gold",text="가격",anchor="center")
com_store_tree.bind('<Double-Button>',com_buy)
com_store_tree.place(x=5,y=10)
#------------------------------------------------------------------------------------

#-------------------------------------지도-------------------------------------------
map_Frame = Frame(window1,width=500,height=500,relief="flat",background="white")
map_Frame.place(x=0,y=0)
map_Adrian_img = PhotoImage(file=".\\Img\\Map_Adrian.png")
Town_Adrian_img = PhotoImage(file=".\\Img\\Town.png")
Woods_Adrian_img = PhotoImage(file=".\\Img\\Woods.png")
Mountain_Adrian_img = PhotoImage(file=".\\Img\\Mountain.png")
#------------------------------------------------------------------------------------

#-------------------------------------가방-------------------------------------------
inv_frame = Frame(window1,width=500,height=500,relief="flat",background="white")
inv_frame.place(x=0,y=0)
inv_note = ttk.Notebook(inv_frame, width=500, height=500)
inv_note.bind("<ButtonRelease-1>",ck_tab)
inv_note.place(x=0,y=0)

equip_inv_frame = Frame(inv_frame, background="white")
use_inv_frame = Frame(inv_frame,background="white")
mat_inv_frame = Frame(inv_frame,background="white")
comm_inv_frame = Frame(inv_frame,background="white")
inv_note.add(equip_inv_frame, text="장비")
inv_note.add(use_inv_frame,text="소비")
inv_note.add(mat_inv_frame,text="재료")
inv_note.add(comm_inv_frame, text="기타")

helmet_label = Label(equip_inv_frame,text=f"모자 : {arm_inv.arm_equipped['helmet']}", background="white", font=(None,12))
chestplate_label = Label(equip_inv_frame,text=f"상의 : {arm_inv.arm_equipped['chestplate']}", background="white", font=(None,12))
glove_label = Label(equip_inv_frame,text=f"장갑 : {arm_inv.arm_equipped['glove']}", background="white", font=(None,12))
leggings_label = Label(equip_inv_frame,text=f"하의 : {arm_inv.arm_equipped['leggings']}", background="white", font=(None,12))
boots_label = Label(equip_inv_frame,text=f"신발 : {arm_inv.arm_equipped['boots']}", background="white", font=(None,12))
weapon_label = Label(equip_inv_frame,text=f"무기 : {arm_inv.weapon_equipped['main']}", background="white", font=(None,12))
helmet_label.place(x=5,y=10)
chestplate_label.place(x=5,y=40)
glove_label.place(x=5,y=70)
leggings_label.place(x=5,y=100)
boots_label.place(x=5,y=130)
weapon_label.place(x=5,y=160)

equip_tree = ttk.Treeview(equip_inv_frame, columns=["name","amount"], displaycolumns=["name","amount"],show="headings",padding=0,height=6)
use_tree = ttk.Treeview(use_inv_frame, columns=["name","amount"], displaycolumns=["name","amount"],show="headings",padding=0,height=10)
mat_tree = ttk.Treeview(mat_inv_frame, columns=["name","amount"], displaycolumns=["name","amount"],show="headings",padding=0,height=10)
comm_tree = ttk.Treeview(comm_inv_frame, columns=["name","amount"], displaycolumns=["name","amount"],show="headings",padding=0,height=10)
equip_tree.place(x=5,y=200)
use_tree.place(x=5,y=10)
mat_tree.place(x=5,y=10)
comm_tree.place(x=5,y=10)

equip_tree.column("name",anchor="center",width=244)
equip_tree.column("amount",anchor="center",width=245)
equip_tree.heading("name",text="아이템",anchor="center")
equip_tree.heading("amount",text="수량",anchor="center")
use_tree.column("name",anchor="center",width=244)
use_tree.column("amount",anchor="center",width=245)
use_tree.heading("name",text="아이템",anchor="center")
use_tree.heading("amount",text="수량",anchor="center")
mat_tree.column("name",anchor="center",width=244)
mat_tree.column("amount",anchor="center",width=245)
mat_tree.heading("name",text="아이템",anchor="center")
mat_tree.heading("amount",text="수량",anchor="center")
comm_tree.column("name",anchor="center",width=244)
comm_tree.column("amount",anchor="center",width=245)
comm_tree.heading("name",text="아이템",anchor="center")
comm_tree.heading("amount",text="수량",anchor="center")

equip_tree.bind('<Double-Button>',equip)
helmet_label.bind('<Double-Button>',helmet_unequip)
chestplate_label.bind('<Double-Button>',chestplate_unequip)
leggings_label.bind('<Double-Button>',leggings_unequip)
glove_label.bind('<Double-Button>',glove_unequip)
boots_label.bind('<Double-Button>',boots_unequip)
weapon_label.bind('<Double-Button>',weapon_unequip)

#------------------------------------------------------------------------------------

#-------------------------------------로그-------------------------------------------
log_list = Text(window1,width=50,height=34, relief="solid",background="white", font=("Aria",12),bd=0,wrap="word")
log_list.place(x=520,y=10)
log_list.insert(0.0,"게임에 접속했습니다.")
log_list.config(state="disabled")
#------------------------------------------------------------------------------------

#-------------------------------------메뉴-------------------------------------------
menubar = Menu(window1)
vil_menu = Menu(menubar, tearoff=0)
vil_menu.add_command(label="상점", command=store_window, font=("Aria", 15))
vil_menu.add_command(label="의뢰", command=mission_window, font=("Aria", 15))

menubar.add_cascade(label="종료", command=close)
menubar.add_cascade(label="마을", menu=vil_menu)
menubar.add_cascade(label="스탯", command=stat_window)
menubar.add_cascade(label="가방", command=inv_window)
#menubar.add_cascade(label="던전", command=dungeon_window)
#menubar.add_cascade(label="보스", command=boss_window)
#menubar.add_cascade(label="테스트",command=cache_rm)
menubar.add_cascade(label="지도",command=map_adrian)
#------------------------------------------------------------------------------------

#------------------------------------메인 윈도우-------------------------------------
start_frame = Frame(window1, width=1000,height=500,background="white")
start_frame.place(x=0,y=0)
log_list.tkraise()
window1.config(menu=menubar)
window1.mainloop()
#------------------------------------------------------------------------------------
