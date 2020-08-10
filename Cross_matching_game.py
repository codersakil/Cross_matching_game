from tkinter import *
import tkinter.messagebox as tmsg
import random

root=Tk()
Label(text='Welcome',font='comicsams 20',fg='red').pack(pady=50)


	
def c1():
	global l1,l2
	h=b1
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c2():
	global l1,l2
	h=b2
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c3():
	global l1,l2
	h=b3
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c4():
	global l1,l2
	h=b4
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c5():
	global l1,l2
	h=b5
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c6():
	global l1,l2
	h=b6
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c7():
	global l1,l2
	h=b7
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c8():
	global l1,l2
	h=b8
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
def c9():
	global l1,l2
	h=b9
	h.config(bg='green')
	l1.remove(h)
	l2.append(h)
	auto()
	check(l2)
	
f1=Frame(root)
b1=Button(f1,padx=100,pady=50,command=c1,bd=10)
b1.grid(row=1,column=1)
b2=Button(f1,padx=100,pady=50,command=c2,bd=10)
b2.grid(row=1,column=2)
b3=Button(f1,padx=100,pady=50,command=c3,bd=10)
b3.grid(row=1,column=3)
b4=Button(f1,padx=100,pady=50,command=c4,bd=10)
b4.grid(row=2,column=1)
b5=Button(f1,padx=100,pady=50,command=c5,bd=10)
b5.grid(row=2,column=2)
b6=Button(f1,padx=100,pady=50,command=c6,bd=10)
b6.grid(row=2,column=3)
b7=Button(f1,padx=100,pady=50,command=c7,bd=10)
b7.grid(row=3,column=1)
b8=Button(f1,padx=100,pady=50,command=c8,bd=10)
b8.grid(row=3,column=2)
b9=Button(f1,padx=100,pady=50,command=c9,bd=10)
b9.grid(row=3,column=3)		

f1.pack()
l1=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
l2=[]
l3=[]

def check(list):
	match=[[b1,b2,b3],[b1,b4,b7],[b1,b5,b9],[b2,b5,b8],[b3,b6,b9],[b3,b5,b7],[b4,b5,b6],[b7,b8,b9]]
	for cl in match:
		i=0
		for item in cl:
			if item in list:
				i+=1
		if i==3:
			if list==l2:
				tmsg.showinfo('Match result','Congratulatio,You won')
			else:
				tmsg.showinfo('Match result','Sorry,You loose')
		
def auto():
	global l1,l3
	rc=random.choice(l1)
	l1.remove(rc)
	rc.config(bg='red')
	l3.append(rc)
	check(l3)



root.mainloop()