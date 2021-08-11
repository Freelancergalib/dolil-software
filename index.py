from tkinter import *
from tkinter import messagebox
import datetime

# corfirmation on closing the root window
def on_close():
	if messagebox.askyesno("Quit",'Do you really want to quit?'):
		root.destroy()

# ---------------button commands---------------
def save():
	try:
		usr_ammount = ammount.get()
	except Exception as e:
		messagebox.showerror("Error","Invalid input in 'ammonut' field!")
	else:
		usr_name = name.get()
		usr_stamp = stamp.get()
		usr_date = date.get()

		# creating a csv file
		csv = open('saved.csv','a')
		csv.write(f"\n{usr_name}, {usr_ammount}, {usr_stamp}, {usr_date}");
		csv.close()
		reset()


def reset():
	name.set("")
	stamp.set("")
	ammount.set(1)
	

def new_quit(*args):
	global new_window
	new_window.destroy()
	del new_window


def show():
	try:
		global new_window
		if(new_window.state()=='normal'):
			new_window.focus()
		elif(new_window.state()=='iconic'):
			new_window.state('normal')
			new_window.focus()
	except NameError as e:
		new_window = Toplevel(root)
		new_window.title("Saved infos")
		new_window.geometry("400x250")
		# new_window.resizable(False,False)
		new_window.focus()
		new_window.bind("<FocusOut>",new_quit)

		csv_r = open('saved.csv','r')
		i = 0
		for line in csv_r:
			l = line.split(', ')
			for col in range(0,4):
				e = Entry(new_window,relief=GROOVE)
				e.insert(END,l[col])
				e.config(state=DISABLED)
				e.grid(row=i,column=col)
			i+=1
		csv_r.close()
	
# ---------------button commands---------------

# main root
root = Tk()

# resizing window
root.geometry("400x250")
root.resizable(False,False)
root.protocol('WM_DELETE_WINDOW',on_close)

#-----------------gui logics-------------------
root.title("দলিল")

# main frame
mf = Frame(root,padx=10,pady=10)
mf.pack(fill='both',side='left',anchor='ne')

Label(mf,text="name:").grid(row=0,column=0)
Label(mf,text="ammount:").grid(row=1,column=0)
Label(mf,text="stamp:").grid(row=2,column=0)
Label(mf,text="date:").grid(row=3,column=0)

name = StringVar()
stamp = StringVar()
date = StringVar()
ammount = IntVar()
Entry(mf,textvariable=name).grid(row=0,column=1)
Entry(mf,textvariable=ammount).grid(row=1,column=1)
Entry(mf,textvariable=stamp).grid(row=2,column=1)
Entry(mf,textvariable=date).grid(row=3,column=1)

Button(mf,text="সংরক্ষণ করুন",command=save).grid(row=4,column=0)
Button(mf,text="Reset",command=reset).grid(row=4,column=1)
Button(mf,text="Show",command=show).grid(row=4,column=2)

# setting the some fields automitically
ammount.set(1)
date.set(datetime.datetime.now().strftime("%d / %m / %Y"))
#-----------------gui logics-------------------

root.mainloop()