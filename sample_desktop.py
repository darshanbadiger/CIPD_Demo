from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog
import subprocess
os.system('clear')
import ICP

root = Tk()
root.title('Sample Desktop')

def op_file1():
	root.file1 = filedialog.askopenfilename(initialdir="/home/darshan/", title="select files",filetypes=(("Mesh Files","*.pcd"),("all files","*.*")))
	lab = Label(text = root.file1).pack()
	root.file2 = filedialog.askopenfilename(initialdir="/home/darshan/", title="select files",filetypes=(("3D files","*.stl"),("all files","*.*")))
	lab = Label(text = root.file2).pack()
	
#	Using ICP Algorithm
#	C2M=subprocess.Popen(["/snap/bin/cloudcompare.CloudCompare","-SILENT", "-AUTO_SAVE", "ON", "-NO_TIMESTAMP", "-M_EXPORT_FMT", "STL","-COMPUTE_NORMALS", "-O", root.file1, "-O", root.file2, "-ICP","-DELAUNAY"])
#	Using C2M_DIST Algorithm
	C2M=subprocess.Popen(["/snap/bin/cloudcompare.CloudCompare","-SILENT", "-AUTO_SAVE", "ON", "-NO_TIMESTAMP", "-M_EXPORT_FMT", "STL","-COMPUTE_NORMALS", "-O", root.file1, "-O", root.file2, "-c2m_dist","-DELAUNAY"])

def op_file3():
	root.file3 = filedialog.askopenfilename(initialdir="/home/darshan/", title="select files",filetypes=(("3D files","*.stl"),("all files","*.*")))
	lab = Label(text = root.file3).pack()
	path_to_open3 = '/usr/bin/blender'
	path_to_file3=os.path.dirname(__file__), root.file3
	print(path_to_file3)
	subprocess.Popen([path_to_open3,root.file3])


myLabel = Label(root, text="Enter Name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

button1 = Button(text="open 3D Files", command=op_file1).pack()
button2 = Button(text="Export to Blender", command=op_file3).pack()






root.mainloop()
