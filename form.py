from tkinter import *
import mysql.connect
from tkinter import ttk
root=Tk()
root.title("STUDENT_FORM")
root.geometry('400x400')
root.configure(background="grey")
a=Label(root,text='NAME').grid(row = 0,column = 0)
a1=Entry(root).grid(row = 0,column = 1)

b=Label(root,text='ID').grid(row = 1,column = 0)
b1=Entry(root).grid(row = 1,column = 1)

c=Label(root,text='DEPARTMENT').grid(row = 2,column = 0)
c1=Entry(root).grid(row = 2,column = 1)

d=Label(root,text='AGE').grid(row = 3,column = 0)
d1=Entry(root).grid(row = 3,column = 1)

e=Label(root,text='GENDER').grid(row=4,column=0)
e1=Radiobutton(root,text='male',value=2).grid(row=4,column=1)
e1=Radiobutton(root,text='female',value=1).grid(row=4,column=2)

def database():
    conn=connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        port='',
        database='Harry')
    mycursor=conn.cursor(),
    mycursor.execute("insert into form values(%s,%s,%s,%s,%s)"),
        (a1.get(),b1.get(),c1.get(),d1.get(),d1.get(),e1.get())
    conn.commit()

btn=ttk.Button(root,text="SUBMIT",command=database).grid(row=6,column=0)


root.mainloop()


