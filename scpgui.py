#import modules
from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename
import getpass
import sys
import os
Dir = askopenfilename()
def execute():
	global status
	status = ("copying...")
	server = serverentry.get()
	password = passwordentry.get()
	username = usernameentry.get()
	path = pathentry.get()
	
	os.system("sshpass -p " + str(password) + " scp "+ str(Dir) +" "+ str(username) +"@"+ str(server) +":"+ str(path) +"")
	 
	status = ("file: %s copied" %(Dir))
def change():
	global Dir
	Dir = askopenfilename()
def update():
	copylabel.config(text="copying: %s" %(Dir))
	statuslabel.config(text=status)
	root.after(1000, update)
#initialize window, and frame
root = Tk()
root.title("scp graphical")

#take input from entryboxes
serverentry = Entry(root)
serverentry.pack(fill=X)

passwordentry = Entry(root, show='*')
passwordentry.pack(fill=X)

usernameentry = Entry(root)
usernameentry.pack(fill=X)

pathentry = Entry(root)
pathentry.pack(fill=X)

status = ("not copying")

copybutton = Button(root, text="COPY", command=execute)
copybutton.pack(fill=X)

changedir = Button(root, text="change file to copy", command=change)
changedir.pack(fill=X)
copytext = ("copying: %s" %(Dir))
copylabel = Label(root, text=copytext)
copylabel.pack(fill=X)
statuslabel = Label(root, text=status)
statuslabel.pack()
serverentry.insert(0, "ip address")
passwordentry.insert(0, "password")
usernameentry.insert(0, "username")
pathentry.insert(0, "/var/www")

root.after(1000, update)
root.configure(background='grey')	
root.title("scp graphical")
root.geometry('500x450')
root.mainloop()

