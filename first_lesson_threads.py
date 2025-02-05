"""
Используем потоки
Источник урока:  https://www.youtube.com/watch?v=_4QY1nGFRY8&t=2156s
"""

from tkinter import ttk
import tkinter as tk
import time
from threading import Thread


def thread_sleep():
    """Имитирую работаэщий поток
    """
    time.sleep(10)
    lab["text"] = str(int(lab["text"]) + 10)  # pylint: disable=E0606

def new_threed():
    """Запускаю поток
    """
    t1 = Thread(target=thread_sleep)
    t1.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300+150+150")

    btn = ttk.Button(root, text="Run", command = new_threed)
    btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    lab = ttk.Label(root, text="0")
    lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()
