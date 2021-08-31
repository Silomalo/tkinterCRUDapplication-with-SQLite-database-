import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog
import sqlite3
from typing import List

root = Tk()
root.geometry('660x540')
root.title("Student Records Management System")
root.configure(background='white')
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
""" create table """
tablecreation = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, regno VARCHAR, fname VARCHAR, sname VARCHAR,surname VARCHAR,ctitle VARCHAR,courseCode VARCHAR,gender VARCHAR)"
cursor.execute(tablecreation)
conn.commit()

title = Label(root, text="Student Records Management System",width=30,font=("Helvetica",20,"bold"),bg='lightblue',fg='white')
title.place(x=70,y=20)
regno = Label(root, text="Registration Number",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
regno.place(x=70,y=100)
regnoInput = Entry(root,width=25,font=("Arial",14),bd=2, fg='blue')
regnoInput.place(x=308,y=100)
fName = Label(root, text="First Name",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
fName.place(x=70,y=150)
fNameInput = Entry(root,width=25,font=("Arial",14),bd=2, fg='blue')
fNameInput.place(x=308,y=150)
sName = Label(root, text="Second Name",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
sName.place(x=70,y=200)
sNameInput = Entry(root,width=25,font=("Arial",14),bd=2, fg='blue')
sNameInput.place(x=308,y=200)
surname = Label(root, text="Surname",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
surname.place(x=70,y=250)
surnameInput = Entry(root,width=25,font=("Arial",14),bd=2, fg='blue')
surnameInput.place(x=308,y=250)
course = Label(root, text="Course Title",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
course.place(x=70,y=300)
courseInput = Entry(root,width=25,font=("Arial",14),bd=2, fg='blue')
courseInput.place(x=308,y=300)
code = Label(root, text="Course Code",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
code.place(x=70,y=350)
codeInput = Entry(root,width=25,font=("Arial",14),bd=2, fg='blue')
codeInput.place(x=308,y=350)
idcode = Entry(root,width=5,font=("Arial",14),bd=2, fg='blue')
idcode.place(x=180,y=450)
# gender dropdown
gender=Label(root, text="Select Gender",width=20,font=("times",14,"bold"),anchor="w",bg='black', fg='white')
gender.place(x=70,y=380)
n = tk.StringVar()
monthchoosen = ttk.Combobox(root,width=24,font=("Arial",14), textvariable = n)
monthchoosen['values'] = (' Male',' Female',' Other')
monthchoosen.place(x=308,y=380)

save = Button(root, text='Save',command=lambda:addStudent(), width=10,bg='green',fg='white',font=("Arial",12,"bold"))
save.place(x=70,y=450)
clear = Button(root, text='Change',command=lambda:saveupdate(),width=10,bg='maroon',fg='white',font=("Arial",12,"bold"))
clear.place(x=180,y=450)
add = Button(root, text='show',command=lambda:show(),width=10,bg='lightgreen',fg='grey',font=("Arial",12,"bold"))
add.place(x=280,y=450)
update = Button(root, text='Update',command=lambda:update(),width=10,bg='blue',fg='white',font=("Arial",12,"bold"))
update.place(x=380,y=450)
delete = Button(root, text='Delete',command=lambda:delete(), width=10,bg='red',fg='white',font=("Arial",12,"bold"))
delete.place(x=480,y=450)

def addStudent():
        try:
            regno = regnoInput.get()
            fname = fNameInput.get()
            sname=sNameInput.get()
            surname=surnameInput.get()
            course=courseInput.get()
            courseCode=codeInput.get()
            sex=monthchoosen.current()
            print(sex)
            records=(regno, fname,sname,surname, course, courseCode, sex)
            query = "INSERT INTO users (regno, fname,sname,surname,ctitle,courseCode,gender) VALUES (?, ?,?,?,?,?,?)"
            cursor.execute(query,records)
            conn.commit()
            mb.showinfo("Record;", "Saved successfully")

        except ValueError:
            print("error")
            return False
        regnoInput.delete(0,END)
        fNameInput.delete(0,END)
        sNameInput.delete(0,END)
        surnameInput.delete(0,END)
        courseInput.delete(0,END)
        codeInput.delete(0,END)
def show():
    class Table(tk.Frame):
        def __init__(self, parent=None, headings=tuple(), rows=tuple()):
            super().__init__(parent)

            table = ttk.Treeview(self, show="headings", selectmode="browse")
            table["columns"] = headings
            table["displaycolumns"] = headings

            for head in headings:
                table.heading(head, text=head, anchor=tk.CENTER)
                table.column(head, anchor=tk.CENTER)

            for row in rows:
                table.insert('', tk.END, values=tuple(row))

            scrolltable = tk.Scrollbar(self, command=table.yview)
            table.configure(yscrollcommand=scrolltable.set)
            scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
            table.pack(expand=tk.YES, fill=tk.BOTH)
    data = ()
    with sqlite3.connect('students.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        data = (row for row in cursor.fetchall())

    root = tk.Tk()
    table = Table(root, headings=('#','RegNo', 'FirstName', 'SecondName','Surname','Title','CourseCode','Gender'), rows=data)
    table.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()
def update():
    answer=simpledialog.askinteger("Input","which index to update?:",parent=root)
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    values=cursor.execute("SELECT * FROM users WHERE id=?", (answer,))
    records=list(values)
    regnoInput.insert(END, records[0][1])
    fNameInput.insert(END,  records[0][2])
    sNameInput.insert(END, records[0][3])
    surnameInput.insert(END, records[0][4])
    courseInput.insert(END, records[0][5])
    codeInput.insert(END, records[0][6])
    idcode.insert(END, records[0][0])
    print(records)
def saveupdate():
        try:
            userid = idcode.get()
            regno = regnoInput.get()
            fname = fNameInput.get()
            sname=sNameInput.get()
            surname=surnameInput.get()
            course=courseInput.get()
            courseCode=codeInput.get()
            sex=monthchoosen.current()
            records=(regno, fname,sname,surname, course, courseCode, sex,userid)
            query = "UPDATE users SET regno= ?,fname= ?,sname= ?,surname= ?, ctitle= ?,courseCode = ?,gender = ? WHERE id = ?"
            cursor.execute(query,records)
            conn.commit()
            mb.showinfo("Records;", "Updated successfully")

        except ValueError:
            print("error")
            return False
        regnoInput.delete(0,END)
        fNameInput.delete(0,END)
        sNameInput.delete(0,END)
        surnameInput.delete(0,END)
        courseInput.delete(0,END)
        codeInput.delete(0,END)
        idcode.delete(0,END)
def delete():
    answer=simpledialog.askinteger("Input","which index to Delete?:",parent=root)
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (answer,))
    mb.showwarning("Record;", "Deleted successfully")
    conn.commit()

root.mainloop()