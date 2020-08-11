from tkinter import *
import tkinter.messagebox as tmsg
import random
player=random.randint(1,2)

root=Tk()
Label(text='Welcome',font='comicsams 20',fg='red',bg='yellow').pack(pady=5,fill=X)

player_frame=Frame(root,bd=10, relief=SUNKEN)
player_frame.pack(pady=10)
Label(player_frame,text='Choose the playing mode',font='comicsams 15',fg='green').grid(row=1,column=1,columnspan=2)

db=Frame(root,bd=5)
db.pack()
scr1,scr2=0,0
plscr1=Label(db,text=f'Player 1 score:\n{scr1}')
plscr2=Label(db,text=f'Player 2 score:\n{scr2}')
play=Label(db,text=f'It is time of player {player}',bg='violet')

mode=0
def single():
	global mode
	mode=1
	new()
	p1.config(state='disable',bg='green')
	p2.config(state=NORMAL,bg='grey')
def double():
	global mode
	mode=2
	new()
	p2.config(state='disable',bg='green')
	p1.config(state=NORMAL,bg='grey')
	play.grid(row=2,column=1,columnspan=2,pady=5)

p1=Button(player_frame,text='Single',command=single)
p1.grid(row=2,column=1,pady=50)
p2=Button(player_frame,text='Double',command=double)
p2.grid(row=2,column=2,pady=50)

def test(h):
	global l1,l2,l3,player
	if (mode==1):
		h.config(bg='green',state='disable')
		l1.remove(h)
		l2.append(h)
		check(l2)
	else:
		if player==1:
			h.config(bg='green',state='disable')
			l1.remove(h)
			l2.append(h)
			check(l2)
			player=2
			
		else:
			l1.remove(h)
			h.config(bg='red',state='disable')
			l3.append(h)
			check(l3)
			player=1
		play.config(text=f'It is time of player {player}')
def c1():
	test(b1)
		
def auto():
	global l1,l3
	rc=random.choice(l1)
	l1.remove(rc)
	rc.config(bg='red',state='disable')
	l3.append(rc)
	check(l3)
	
series=0
def new():
	global series
	global l1,l2,l3,b_com,b1,b2,b3,b4,b5,b6,b7,b8,b9,f1,b_com,b_new
	if series==1:
		f1.pack_forget()
	series=1
	f1=Frame(root)
	b1=Button(f1,padx=100,pady=50,command=lambda:test(b1),bd=10)
	b1.grid(row=1,column=1)
	b2=Button(f1,padx=100,pady=50,command=lambda:test(b2),bd=10)
	b2.grid(row=1,column=2)
	b3=Button(f1,padx=100,pady=50,command=lambda:test(b3),bd=10)
	b3.grid(row=1,column=3)
	b4=Button(f1,padx=100,pady=50,command=lambda:test(b4),bd=10)
	b4.grid(row=2,column=1)
	b5=Button(f1,padx=100,pady=50,command=lambda:test(b5),bd=10)
	b5.grid(row=2,column=2)
	b6=Button(f1,padx=100,pady=50,command=lambda:test(b6),bd=10)
	b6.grid(row=2,column=3)
	b7=Button(f1,padx=100,pady=50,command=lambda:test(b7),bd=10)
	b7.grid(row=3,column=1)
	b8=Button(f1,padx=100,pady=50,command=lambda:test(b8),bd=10)
	b8.grid(row=3,column=2)
	b9=Button(f1,padx=100,pady=50,command=lambda:test(b9),bd=10)
	b9.grid(row=3,column=3)
	b_com=Button(f1,command=auto,pady=50,text='Coumputerer\'s turn')
	b_com.grid(row=4,column=1,columnspan=3,pady=50)
	
	b_new=Button(f1,text='New Game',command=new)
	b_new.grid(row=5,column=1,columnspan=3,pady=10)
	l1=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
	l2=[]
	l3=[]
	f1.pack()
	global player
	if mode==2:
		b_com.grid_forget()
		player=random.randint(1,2)
		
		plscr1.grid(row=1,column=1,padx=20)
		plscr2.grid(row=1,column=2,padx=20)
		play.config(text=f'It is time of player {player}')
	else:
		plscr1.grid_forget()
		plscr2.grid_forget()
		play.grid_forget()
		b_com.grid(row=4,column=1,columnspan=3,pady=50)
		



	
def check(list):
	match=[[b1,b2,b3],[b1,b4,b7],[b1,b5,b9],[b2,b5,b8],[b3,b6,b9],[b3,b5,b7],[b4,b5,b6],[b7,b8,b9]]
	global scr1,scr2
	for cl in match:
		i=0
		for item in cl:
			if item in list:
				i+=1
		if i==3:
			if list==l2:
				if mode==1:
					tmsg.showinfo('Match result','Congratulatio,You won')
				else:
					tmsg.showinfo('Match result','Congratulation player1,You won')
					scr1+=1
					plscr1.config(text=f'Player 1 score:\n{scr1}')
			else:
				if mode==1:
					tmsg.showinfo('Match result','Sorry,You loose')
				else:
					tmsg.showinfo('Match result','Congratulation player2,You won')
					scr2+=1
					plscr2.config(text=f'Player 2 score:\n{scr2}')
			new()

root.mainloop()