from tkinter import *
from PIL import ImageTk, Image
import os
import subprocess
os.system('clear')

root = Tk()
root.title("BREED Tool")
root.geometry("1350x750")
#root.configure(background='white')

def open_blender():
    blend = "/snap/bin/cloudcompare.CloudCompare"
    sam = (f1,(os.system('"%s"' % blend)))

top1 = Label(root, text="Blender Window",font=("italic",15))
top1.pack()

f1  = Frame(root, width=1350,height=600,bd=8,bg="white",relief="raise")
f1.pack()
b1 = Button(root, text="Export Model",font=('italic',15)).place(x=100, y=650)
b2 = Button(root, text="Analysis",font=('italic',15)).place(x=1000, y=650)
b3 = Button(root, text="Blender", font=("italic",15),command=open_blender).place(x=500,y=650)



root.mainloop()