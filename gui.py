from tkinter import *
from tkinter import ttk
from skillListBuilder import skLst, get_key, get_val
from collapsiblepane import CollapsiblePane as cp

def updateSkillUI():
    for i in range(0, len(skLst)):
        cp(frm, get_key(skLst, i), get_key(skLst, i)).grid(column=0, row=i+1, pady=10)
        ttk.Label(frm, text=get_val(skLst, i)['Xp']).grid(column=1, row =i+1)
        ttk.Label(frm, text=get_val(skLst, i)['Level']).grid(column=2, row =i+1)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Skill").grid(column=0, row=0, pady=10)
ttk.Label(frm, text="Experience").grid(column=1, row=0, pady = 10)
ttk.Label(frm, text="Level").grid(column=2, row=0, pady =10)

updateSkillUI()

# cpane = cp(root, 'Expanded', 'Collapsed')
# cpane.grid(row = 0, column = 0)
 
# # Button and checkbutton, these will
# # appear in collapsible pane container
# b1 = Button(cpane.frame, text ="GFG").grid(
#             row = 1, column = 2, pady = 10)
 
# cb1 = Checkbutton(cpane.frame, text ="GFG").grid(
#                   row = 2, column = 3, pady = 10)

#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)
root.mainloop()
