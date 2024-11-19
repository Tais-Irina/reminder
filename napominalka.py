from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import pygame
import time

def set_remind():
    pass

window = Tk()
window.title("Reminder")

label = Label(text = 'Установите напоминание', font = ('Georgia', 20, "bold"))
label.pack()

set_button = Button(text = 'Установить напоминание', font = ('Georgia', 15, "bold"),
                    command = set_remind)
set_button.pack()

window.mainloop()