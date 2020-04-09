from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog
import subprocess
os.system('clear')

root = Tk()
root.title('Test Desktop')


def hello():
	hello_label = Label(root, text="hello" + myTextbox.get())
	hello_label.pack()

def op_file():
	file1 = filedialog.askopenfile()
	#f = file1.get(ACTIVE)
	lab = Label(text = file1).pack()
	
	#os.system('/snap/bin/cloudcompare.CloudCompare'+ f)
	#path_to_open = '/snap/bin/cloudcompare.CloudCompare'
	#path_to_file = file1
	#subprocess.call([path_to_open, path_to_file])
	os.system('/snap/bin/cloudcompare.CloudCompare')

def get_file():
	file2 = filedialog.askopenfile()
	subprocess.Popen('/usr/share/man/man1/blender.1.gz')

myLabel = Label(root, text="Enter Name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

button1 = Button(text="open first file", command=op_file).pack()
button2 = Button(text="open second file", command=op_file).pack()
button3 = Button(text="Export from blender", command=get_file).pack()


myButton = Button(root, text="Submit", command=hello)
myButton.pack()




root.mainloop()
