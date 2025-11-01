import tkinter as tk
import os
import multiprocessing
from function import grf
from playsound import playsound

root = tk.Tk()
root.config(bg="gray5")
root.title("")

label = tk.Label(root, text="Hor1eblePlayer")
label.pack()
label2 = tk.Label(root, text=" ")
label2.pack()


def button_start():
    global p
    os.chdir("music")
    directory_path = os.getcwd()
    sound = grf(directory_path)
    
    if sound:
        print(f"Случайный файл: {sound}")
    else:
        print("Папка пуста или не существует.")
    p = multiprocessing.Process(target=playsound, args=(sound,))
    p.start()
    label2.config(text = sound)
    
    os.chdir("..")
    
def button_stop():
    
    p.terminate()
    label2.config(text = "")
    print(os.getcwd())

def scale_volume():
    pass

    
    



button = tk.Button(root, text="click me to start music :3", command=button_start)
button.pack()
button2 = tk.Button(root, text="click me to stop music :3", command=button_stop)
button2.pack()
scale = tk.Scale(root, length = 100,from_=100,to=0, command=scale_volume)
scale.pack()
root.mainloop()