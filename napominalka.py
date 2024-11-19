from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import pygame
import time


def set_remind():
    # время напоминания
    global t
    rem = sd.askstring('Время напоминания',
                       'Введите время напоминания в формате чч:мм')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            #print(hour, minute, now)
            dt = now.replace(hour = hour, minute = minute, second=0)
            #print(dt)
            # формат понятный пайтону.
            t=dt.timestamp()
            label.config(text = f"Напоминание установлено на {hour:02} : {minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неправильный формат времени")

# каждые 10с проверка наступления времени
def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
    # рекурсия - сама себя вызывает
    window.after(10000,check)

def play_snd():
    global music_plaing
    music_plaing = True
    pygame.mixer.init()
    pygame.mixer.music.load('Michael Jackson - The Way You Make Me Feel.mp3')
    pygame.mixer.music.play()


def stop_music():
    global music_plaing
    if music_plaing:
        pygame.mixer.music.stop()
        music_plaing = False
        label.config(text = 'Установить новое напоминание')


#переменные глобальные
t = None
music_plaing = False


window = Tk()
window.title("Reminder")

label = Label(text = 'Установите напоминание', font = ('Georgia', 20, "bold"))
label.pack(pady = 10)

set_button = Button(text = 'Установить напоминание', font = ('Georgia', 15, "bold"),
                    command = set_remind)
set_button.pack(pady = 10)

stop_button = Button(text = 'Остановить музыку', font = ('Georgia', 15, "bold"),
                    command = stop_music)
stop_button.pack(pady=10)
check()

window.mainloop()