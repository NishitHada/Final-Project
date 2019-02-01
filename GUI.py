from tkinter import *
from backend import Analyze
import sqlite3

conn = sqlite3.connect('dtab.db')
conn.execute("'create table User(User_Id int primary key, Name text not null);'")
conn.execute("'create table Post(Post_Id int primary key, Posted_Text text not null, Posting_Date date, User_Id int foreign key references User(User_Id);'")

root = Tk()
root.title('Sentiment Analysis using Dictionary Method')

text = StringVar()
sen = StringVar()
sender = StringVar()
time_hr = IntVar()
time_min = IntVar()

def Calculate(event):
    t=text.get()
    print(t)
    o=Analyze(t)
    sen.set(o)
    print(sen.get())

def Insert(event):
    t = text.get()
    s = sender.get()
    h = time_hr.get()
    m = time_min.get()
    conn.execute("insert into User(User_Id, Name) values(?, ?)", (User_Id, Name))
    conn.execute("insert into Post(Post_Id, Posted_Text, Posting_Date, User_Id) values (?, ?, ?, ?)",
                 (Post_Id, Posted_Text, Posting_Date, User_Id))

def Exit(event):
    conn.close()
    quit()

L1 = Label(root, text='Enter text:')
L1.grid(row=1, column=0)
E1= Entry(root, textvariable=text)
E1.grid(row=1, column=1)

L2 = Label(root, text="Sentiment Polarity:")
L2.grid(row=2, column=0)
L3 = Label(root, textvariable=sen)
L3.grid(row=2, column=1)

B1 = Button(root, text='Calculate')
B1.grid(row=2, column=3)
B1.bind('<Button-1>', Calculate)

L4 = Label(root, text="Sender:")
L4.grid(row=3, column=0)
E2 = Entry(root, textvariable=sender)
E2.grid(row=3, column=1)

L6 = Label(root, text="Hour:")
L6.grid(row=4, column=0)
E3 = Entry(root, textvariable=time_hr)
E3.grid(row=4, column=1)
L8 = Label(root, text="Min:")
L8.grid(row=4, column=2)
E4 = Entry(root, textvariable=time_min)
E4.grid(row=4, column=3)

B1 = Button(root, text='Insert')
B1.grid(row=5, column=3)
B1.bind('<Button-1>', Calculate)

B2 = Button(root, text='Exit')
B2.grid(row=5, column=4)
B2.bind('<Button-1>', Exit)


root.mainloop()