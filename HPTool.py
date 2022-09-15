import tkinter as tk
import os

def enable_hf():
    os.system('cmd /c "powercfg /s SCHEME_MIN"')
    return enable_hf

def disable_hf():
    os.system('cmd /c "powercfg.exe /setactive 381b4222-f694-41f0-9685-ff5bb260df2e"')
    return disable_hf

root = tk.Tk()
root.iconbitmap("icon.ico")
root.title("High Performance Tool")

banner = tk.PhotoImage(file="banner.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack(padx=20, pady=20)

enable = tk.Button(root, text="Enable High Performance Mode", font=("Roboto", 10), relief="solid", command=enable_hf)
enable.pack(padx=20)

disable = tk.Button(root, text="Disable High Performance Mode", font=("Roboto", 10), relief="solid", command=disable_hf)
disable.pack(padx=20, pady=5)

bottom_text = tk.Label(root, text="Created by FaishalKC", font=("Roboto", "8"))
bottom_text.pack()

root.mainloop()