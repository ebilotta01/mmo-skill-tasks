from tkinter import *
from tkinter import ttk
from skillListBuilder import skLst, get_key, get_val

def updateSkillUI():
    for i in range(0, len(skLst)):
        ttk.Label(frm, text=get_key(skLst, i)).grid(column=0, row=i+1)
        ttk.Label(frm, text=get_val(skLst, i)['Xp']).grid(column=1, row =i+1)
        ttk.Label(frm, text=get_val(skLst, i)['Level']).grid(column=2, row =i+1)




root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Skill").grid(column=0, row=0)
ttk.Label(frm, text="Experience").grid(column=1, row=0)
ttk.Label(frm, text="Level").grid(column=2, row=0)

updateSkillUI()


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)
root.mainloop()
