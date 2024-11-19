from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import pygame
import time

def set_remind():
    rem = sd.askstring('Время напоминания','Введите время напоминания в формате чч:мм')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(hour, minute, now)
            dt = now.replace(hour = hour, minute = minute, second=0)
            print(dt)
            t=dt.timestamp()
            label.config(text = f"Напоминание установлено на {hour:02} : {minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неправильный формат времени")

window = Tk()
window.title("Reminder")

label = Label(text = 'Установите напоминание', font = ('Georgia', 20, "bold"))
label.pack()

set_button = Button(text = 'Установить напоминание', font = ('Georgia', 15, "bold"),
                    command = set_remind)
set_button.pack()

window.mainloop()