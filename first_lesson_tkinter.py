"""
ИСточник урока:  https://www.youtube.com/watch?v=_4QY1nGFRY8&t=2156s
"""

import tkinter
import time
import tkinter.ttk

root = tkinter.Tk()
root.geometry("300x300+150+150")

def sleep_func():
    time.sleep(10)
    lab:dict={}
    lab['text'] = "После сна"


btn = tkinter.ttk.Button(root, text="Run", command = sleep_func)
btn.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

lab = tkinter.ttk.Label(root, text="Текст до нажатия")
lab.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


root.mainloop()