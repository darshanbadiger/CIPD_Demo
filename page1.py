from tkinter import *
from PIL import ImageTk, Image
import os
import sys
import subprocess
os.system('clear')
from tkinter import filedialog
from io import StringIO
from contextlib import redirect_stdout
from tkinter import messagebox
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
import sqlite3

root = Tk()
root.title("BREED Tool")
root.geometry("1250x700")

top1 = Frame(root, width=1350,height=700,bd=8,bg="white",relief="raise")
top1.pack()

f1 = Frame(top1, width=1350,height=250,bd=8,bg="blue",relief="raise")
f1.pack()

f2 = Frame(top1, width=1350,height=300,bd=8,bg="white",relief="raise")
f2.pack(side=LEFT)

#f3 = Frame(top1, width=700,height=300,bd=8,bg="white",relief="raise")
#f3.pack(side=RIGHT)


def op_f():
        root.file1 = filedialog.askopenfilename(initialdir="/home/darshan/", title="select files",filetypes=(("Mesh Files","*.pcd"),("all files","*.*")))
        db=sqlite3.connect('mysq.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO image VALUES(?,?)",[None,root.file1])
        db.commit()
        img = cursor.execute("SELECT geo_image from geometry")
        for x in img:
            y = list(x)
            for li in y:
                print(li)
                c2m = subprocess.Popen(["/snap/bin/cloudcompare.CloudCompare","-SILENT", "-AUTO_SAVE", "ON", "-NO_TIMESTAMP", "-M_EXPORT_FMT", "STL","-COMPUTE_NORMALS", "-O", root.file1, "-O", li, "-ICP","-DELAUNAY"])

                sys.stdout = open('file.txt', 'w')
                print('test')      

    #    lab = Label(f2aa,font=('arial', 10, 'bold'), text ="Selected file : "+li).pack()
        res = messagebox.askquestion("Upload Successful!", "Files are Uploaded successfully.View Result in Blender?")
        if res=='yes':
            print("Success")
        #    import test_blend_export

'''
#Insert into the table
def ins():
    x1 = e1.get()
    x2 = e2.get()

#    print(x1, x2)
    db = sqlite3.connect('mysq.db')
    cursor = db.cursor()
    insrt = cursor.execute("INSERT INTO fun_tags VALUES (?, ?, ?)",(None, x1, x2))
    db.commit()
    print(x1, x2)
'''

#Display the table Data
def f_view_data():
    db = sqlite3.connect('mysq.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM fun_tags')
    for row in cursor.fetchall():
        print(row)
    #    lab = Label(root, text=row).pack(padx=10,pady=10)

#Search Data from the table
def f_search():
    simp = search_tag.get()
    print(simp)
    db=sqlite3.connect('mysq.db')
    cursor=db.cursor()
    srch = cursor.execute('SELECT * FROM fun_tags WHERE Functionality LIKE (?)',['%'+simp+'%'])
    
    for data in srch:
        print(data)
        lab= Label(f2, text=data, font=("italic", 15)).pack()

def view_list():
    db=sqlite3.connect('mysq.db')
    cursor=db.cursor() 
    view_d = cursor.execute("SELECT * FROM geometry")
    for v_data in view_d:
        print(v_data)
        lab=Label(f2, text=v_data,font=("italic",15)).pack(padx=10,pady=10)

def open_m():
    import page2

'''
l1 = Label(root, text="Form:").place(x=20,y=20)
e1 = Entry(root)
e1.place(x=150,y=20)

l2 = Label(root, text="Functionality:").place(x=20,y=40)
e2 = Entry(root)
e2.place(x=150,y=40)

b4 = Button(root, text="Insert", command=ins).place(x=50, y=60)
'''
s1 = Label(root, text="Search functional Tag:", font=("italic", 15)).place(x=60, y=100)
search_tag = Entry(root, width=30, font=("italic",15))
search_tag.place(x=300,y=100)
b1 = Button(root, text="Search",font=('italic',15),command=f_search).place(x=650, y=95)

s2 = Label(root, text="Insert file for Comparision:", font=("italic", 15)).place(x=60, y=150)
b2 = Button(root, text="Upload File",font=('italic',15), command=op_f).place(x=400, y=145)
b3 = Button(root, text="Open Model",font=('italic',15), command=open_m).place(x=1000, y=600)
b4 = Button(root, text="View Geometry files",font=('italic',15),command=view_list).place(x=400, y=200)



root.mainloop()