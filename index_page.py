import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import subprocess
os.system('clear')

root = tk.Tk()
root.title("BREED Tool")
root.geometry("1250x700")
#root.configure(background='white')

def start_b():
    import page1


a = Label(root, text="BREED Tool for Bionic Design", font=("italic",40)).place(x=350,y=20)
b = Label(root, text="Instructions", font=("bold", 25)).place(x=200, y=100)
i1 = Label(root, text="1.Upload your STL file or search using functional keywords",font=('italic',15)).place(x=30, y=140)
i2 = Label(root, text="2.Let the system suggest the inspirations in nture",font=('italic',15)).place(x=30, y=180)
i3 = Label(root, text="3.Modify the model for your use, analyse and export model",font=('italic',15)).place(x=30, y=220)

i4 = Label(root, text="An initiative by CIPD",font=('italic',15)).place(x=950, y=550)

b1 = Button(root, text="Start Button",font=('italic',15),command=start_b).place(x=900, y=150)



root.mainloop()
