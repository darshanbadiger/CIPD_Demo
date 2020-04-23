from tkinter import *
from tkinter import filedialog
import subprocess
import os
os.system('clear')


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

def op_f():
	os.system('blender --python sample1.py')

button1 = Button(text="open 3D Files", command=op_file1).pack()
button2 = Button(text="Export to Blender", command=op_f).pack()


root.mainloop()