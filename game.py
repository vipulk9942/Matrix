from tkinter import *
import random
from tkinter import messagebox as msg
class game(Frame):
    def __init__(self,ms):
        super().__init__(ms)
        
        self.l1=Label(self,text='ROCK PAPER SCISSOR',fg='black',bg='light gray',font=('algerian',16,'bold'),justify='center')
        self.l5=Label(self,text='YOU ARE PLAYING AGAINST JARVIS',fg='white',bg='light green',font=('times new roman',10,'bold'),justify='center')
        self.l2=Label(self,text='Your choice',fg='white',bg='magenta',font=('garamond',12,'bold'),justify='center')
        self.l3=Label(self,text='Jarvis choice',fg='white',bg='magenta',font=('garamond',12,'bold'),justify='center')
        self.l4=Label(self,text='Result',fg='white',bg='magenta',font=('garamond',12,'bold'),justify='center')
        
        self.b1=Button(self,text='ROCK',fg='white', width=10,bg='blue',font=('trajan',10,'bold'),justify='center',command=self.rock)
        self.b2=Button(self,text='PAPER',fg='white',width=10,bg='blue',font=('trajan',10,'bold'),justify='center',command=self.paper)
        self.b3=Button(self,text='SCISSOR',fg='white',width=10,bg='blue',font=('trajan',10,'bold'),justify='center',command=self.scissor)
        self.b4=Button(self,text='RESET',fg='white',width=10,bg='red',font=('trajan',10,'bold'),justify='center',command=self.reset)
        
        self.t2=Entry(self,fg='red',font=('garamond',12,'bold'),justify='center')
        self.t3=Entry(self,fg='red',font=('garamond',12,'bold'),justify='center')
        self.t4=Entry(self,fg='red',font=('garamond',12,'bold'),justify='center')
        
        self.rowconfigure(index=0,pad=15)
        self.rowconfigure(index=1,pad=15)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=6,pad=15)
        self.rowconfigure(index=7,pad=15)
        self.rowconfigure(index=8,pad=15)
        
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.l1.grid(row=1,column=1)
        self.l5.grid(row=2,column=1)        
        self.l2.grid(row=6,column=0)
        self.t2.grid(row=6,column=1)
        
        self.l3.grid(row=7,column=0)
        self.t3.grid(row=7,column=1)
        
        self.l4.grid(row=8,column=0)
        self.t4.grid(row=8,column=1)
        
        self.b1.grid(row=3,column=0)
        self.b2.grid(row=4,column=0)
        self.b3.grid(row=5,column=0)
        self.b4.grid(row=9,column=0)
        
        self.b1.grid(columnspan=2)
        self.b2.grid(columnspan=2)
        self.b3.grid(columnspan=2)
        self.b4.grid(columnspan=2)
        
        self.pack()
        
    def rock(self):
        self.t2.insert(0,'rock')
        uc=random.choice(['rock','paper','scissor'])
        self.t3.insert(0,uc)
        
        if uc=='rock':
            self.t4.insert(0,'Draw')
        elif uc=='paper':
            self.t4.insert(0,'Jarvis Win')
        elif uc=='scissor':
            self.t4.insert(0,'You Win')
        else:
            self.t4.insert(0,'Invalid')
        
    def paper(self):
        self.t2.insert(0,'paper')
        uc=random.choice(['rock','paper','scissor'])
        self.t3.insert(0,uc)
        
        if uc=='rock':
            self.t4.insert(0,'You Win')
        elif uc=='paper':
            self.t4.insert(0,'Draw')
        elif uc=='scissor':
            self.t4.insert(0,'Jarvis Win')
        else:
            self.t4.insert(0,'Invalid')
            
    def scissor(self):
        self.t2.insert(0,'scissor')
        uc=random.choice(['rock','paper','scissor'])
        self.t3.insert(0,uc)
        
        if uc=='rock':
            self.t4.insert(0,'Jarvis Win')
        elif uc=='paper':
            self.t4.insert(0,'You Win')
        elif uc=='scissor':
            self.t4.insert(0,'Draw')
        else:
            self.t4.insert(0,'Invalid')
        
    def reset(self):
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
            self.t4.delete(0,'end')
root=Tk()
obj=game(root)
root.title('Game')
root.configure()
root.geometry('650x400')
root.mainloop()