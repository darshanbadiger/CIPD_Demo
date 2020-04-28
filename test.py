from tkinter import *
from tkinter import ttk
import random
import time, datetime
import os
from tkinter import filedialog
import subprocess
os.system('clear')


root = Tk()
root.title('Design from Nature')
root.geometry("1350x750+0+0")
#root.configure(background='black')
'''
my_menu = Menu(root)
root.config(menu=my_menu)

#click command
def our_command():
	pass

#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(Label="File", menu=file_menu)

file_menu.add_command(Label="New..", command=our_command)
file_menu.add_separator()
file_menu.add_command(Label="Exit", command=root.quit)


#Create an edit menu item
edit_menu=Menu(my_menu)
my_menu.add_cascade(Label="Edit", menu=edit_menu)
edit_menu.add_command(Label="Cut", command=our_command)
edit_menu.add_command(Label="Copy", command=our_command)'''

Tops = Frame(root, width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

#=======================Frame=================
f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width=440, height=650, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=50, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=450, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=450, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='steel blue')
f1.configure(background='black')
f2.configure(background='black')

labtop = Label(Tops, font=('arial', 50, 'bold'), text="Project on Design From Nature", bd=10)
labtop.grid(row=0,sticky=W)

name_1 = Label(f1aa,font=('arial', 16, 'bold'), text = "What is Biomimicry?",fg='red' ,bd=10)
name_1.grid(row=0,column=0)
name_2 = Label(f1aa,font=('arial', 10, 'bold'), text = "Biomimicry is a practice that learns from and", bd=10)
name_2.grid(row=1,sticky=W)
name_2 = Label(f1aa,font=('arial', 10, 'bold'), text = "mimics the strategies found in nature to solve", bd=10)
name_2.grid(row=2,sticky=W)
name_2 = Label(f1aa,font=('arial', 10, 'bold'), text = "human design challenges and find hope along the way.", bd=10)
name_2.grid(row=3,sticky=W)


name_3 = Label(f1ab,font=('arial', 10, 'bold'), text = "Biomimicry is about valuing nature for what ewe can learn," ,bd=10)
name_3.grid(row=0,column=0, sticky=W)
name_4 = Label(f1ab,font=('arial', 10, 'bold'), text = "not what we can extract, harvest, or domesticate. In the", bd=10)
name_4.grid(row=1,sticky=W)
name_7 = Label(f1ab,font=('arial', 10, 'bold'), text = "process, we learn about ourselves, our purpose, and our", bd=10)
name_7.grid(row=2,sticky=W)
name_8 = Label(f1ab,font=('arial', 10, 'bold'), text = "connection to each other and our home on earth.", bd=10)
name_8.grid(row=3,sticky=W)


def op_file1():
	root.file1 = filedialog.askopenfilename(initialdir="/home/darshan/", title="select files",filetypes=(("Mesh Files","*.pcd"),("all files","*.*")))
	lab = Label(f2aa, font=('arial', 10, 'bold'),text = root.file1).pack()
	root.file2 = filedialog.askopenfilename(initialdir="/home/darshan/", title="select files",filetypes=(("3D files","*.stl"),("all files","*.*")))
	lab = Label(f2aa,font=('arial', 10, 'bold'), text = root.file2).pack()
	
#	Using ICP Algorithm
#	C2M=subprocess.Popen(["/snap/bin/cloudcompare.CloudCompare","-SILENT", "-AUTO_SAVE", "ON", "-NO_TIMESTAMP", "-M_EXPORT_FMT", "STL","-COMPUTE_NORMALS", "-O", root.file1, "-O", root.file2, "-ICP","-DELAUNAY"])

#	Using C2M_DIST Algorithm
	C2M=subprocess.Popen(["/snap/bin/cloudcompare.CloudCompare","-SILENT", "-AUTO_SAVE", "ON", "-NO_TIMESTAMP", "-M_EXPORT_FMT", "STL","-COMPUTE_NORMALS", "-O", root.file1, "-O", root.file2, "-c2m_dist","-DELAUNAY"])


btn_1 = Button(ft2, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'),width=5, text="3D File", command=op_file1).grid(row=0, column=0)
name_5 = Label(ft2,font=('arial', 10, 'bold'), text = "Upload Mesh File & Geometry file for process. ", bd=10)
name_5.grid(row=1,sticky=W)


def op_f():
	os.system('blender --python sample1.py')

btn_2 = Button(fb2, padx=16, pady=1, bd=4, fg='black', font=('arial', 10, 'bold'),width=20, text="Extract to Blender", command=op_f).grid(row=0, column=0)
name_6 = Label(fb2,font=('arial', 10, 'bold'), text = "File will open in Blender.\t\t     ", bd=10)
name_6.grid(row=1,sticky=W)

'''
var1 = IntVar()
var1.set("0")
a1 = Checkbutton(f1aa, text='Function Tag', variable = var1, onvalue=1, offvalue=0, 
				font=('arial',18,'bold')).grid(row=0,column=0)

txtentry = Entry(f1aa, font=('arial',16, 'bold'),bd=8, width=6,justify='left',state=DISABLED)
txtentry.grid(row=0,column=1)
'''

root.mainloop()