from tkinter import *
from tkinter import messagebox
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
def deleteTask():
    lb.delete(ANCHOR)

def cross_off_item():
    lb.itemconfig(
        lb.curselection(),
        fg="#dedede")
    lb.selection_clear(0, END)

def uncross_item():
    lb.itemconfig(
        lb.curselection(),
        fg="#464646")
    lb.selection_clear(0, END)


root = Tk()
root.geometry('700x450+500+200')
root.title('PythonGuides')
root.config(bg='#3D0C11')
root.resizable(width=False, height=False)

frame = Frame(root)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Helvetica', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#7D7C7C',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    root,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Helvetica 14'),

    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Helvetica 14'),

    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

crossoff_btn=Button(
    button_frame,
    text='Crossoff',
    font=('Helvetica 14'),

    padx=20,
    pady=10,
    command=cross_off_item
)
crossoff_btn.pack()

uncross_btn=Button(
    button_frame,
    text='Uncross',
    font=('Helvetica 14'),

    padx=20,
    pady=10,
    command=uncross_item
)
uncross_btn.pack()

root.mainloop()