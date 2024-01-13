from tkinter import *
import tkinter.ttk as ttk
root = Tk()
root.geometry("500x500")

log_list = Text(root,width=50,height=34, relief="solid",background="white", font=("Aria",12),bd=0,wrap="word")
log_list.place(x=0,y=0)
log_list.insert(0.0,"게임에 접속했습니다.")
root.mainloop()