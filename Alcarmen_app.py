"""
    Name:Alcarmen, Brandon V.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
from dbhelper import *

class UserLogin():
    def __init__(self):
        self.root = Tk()
        self.root.title("ALCARMEN, BRANDON V.")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#ADD8E6")
        self.frame = Frame(self.root, bd=20, bg="#ADD8E6")
        self.frame.grid()

        # >>>>IDNO<<<<<
        self.lbl_idno = Label(self.frame, text="IDNO", font="Verdana,20", bd=20, bg="#ADD8E6")
        self.lbl_idno.grid(row=0, column=0)

        # >>>>LastName<<<<
        self.lbl_Lastname = Label(self.frame, text="LASTNAME", font="Verdana,20", bd=20, bg="#ADD8E6")
        self.lbl_Lastname.grid(row=1, column=0)

        # >>>FirstName<<<<
        self.lbl_Firstname = Label(self.frame, text="FIRSTNAME", font="Verdana,20", bd=20, bg="#ADD8E6")
        self.lbl_Firstname.grid(row=2, column=0)

        # >>>>Course<<<<
        self.lbl_Course = Label(self.frame, text="COURSE:", font="Verdana,20", bd=20, bg="#ADD8E6")
        self.lbl_Course.grid(row=3, column=0)
        n = tk.StringVar()
        self.Course = ttk.Combobox(self.frame, width=27, textvariable=n)
        self.Course['values'] = ('BSIT', 'CCS', 'COMP-E')
        self.Course.grid(column=1, row=3)
        self.Course.current()

        # >>>>>Level<<<<<
        self.lbl_Level = Label(self.frame, text="LEVEL:", font="Verdana,20", bd=20, bg="#ADD8E6")
        self.lbl_Level.grid(row=4, column=0)
        L = tk.StringVar()
        self.Level = ttk.Combobox(self.frame, width=27, textvariable=L)
        self.Level['values'] = ('1', '2', '3', '4')
        self.Level.grid(column=1, row=4)
        self.Level.current()

        # ---------------------------------------------------------
        self.txt_idno = Entry(self.frame, text="idno", font="Verdana,20")
        self.txt_idno.grid(row=0, column=1)
        self.txt_Lastname = Entry(self.frame, text="Lastname", font="Verdana,20")
        self.txt_Lastname.grid(row=1, column=1)
        self.txt_Firstname = Entry(self.frame, text="Firstname", font="Verdana,20")
        self.txt_Firstname.grid(row=2, column=1)



        self.Butt = Frame(self.frame, bd=30, bg="Blue")
        self.Butt.grid(row=10, column=0, columnspan=2)
        
        self.btn_Find = Button(self.frame, text="Find", font="Verdana,20", bg="Gold", command= self.findstudent)
        self.btn_Find.grid(row=0, column=3, columnspan=2, padx=10, sticky="w")

        self.btn_New = Button(self.Butt, text="New", font="Verdana,20", bg="Gold", command=self.newstudent)
        self.btn_New.grid(row=0, column=0, padx=10, sticky="w")
        self.btn_Save = Button(self.Butt, text="Save", font="Verdana,20", bg="Gold", command=self.savestudent)
        self.btn_Save.grid(row=0, column=2, padx=10, sticky="w")
        self.btn_Delete = Button(self.Butt, text="Delete", font="Verdana,20", bg="Gold", command=self.deletestudent)
        self.btn_Delete.grid(row=0, column=4, padx=10, sticky="w")
        self.btn_Update = Button(self.Butt, text="Update", font="Verdana,20", bg="Gold", command= self.updatestudent)
        self.btn_Update.grid(row=0, column=6, padx=10, sticky="w")

        self.root.eval("tk::PlaceWindow . center")
        self.root.mainloop()

    def findstudent(self):
        idno=self.txt_idno.get()
        if idno:
            data = getrecord('student', idno = idno)
            if data:
                student = data[0]
                self.txt_Lastname.delete(0, END)
                self.txt_Firstname.delete(0, END)
                self.txt_Lastname.insert(0, student['lastname'])
                self.txt_Firstname.insert(0, student['firstname'])
                self.Course.set(student[course])
                self.Level.set(student[level])
                messagebox.showinfo("Student", "Student Found!")
                message = f" Student Idno:\t\t {student['idno']}\n Student Lastname:\t {student['lastname']}\n Student Firstname:\t {student['firstname']}\n Student Course:\t\t {student['course']}\n Student Level:\t\t {student['level']}"
                messagebox.showinfo("Student Info", message)
            else:
                messagebox.showerror("Student", f"Student IDNO:{idno} doesn't exist.")
        else:
            messagebox.showerror("Find", f"Student IDNO:{idno} doesn't exist.")
    def savestudent(self):
        print("Saved")
        idno = self.txt_idno.get()
        lastname = self.txt_Lastname.get()
        firstname = self.txt_Firstname.get()
        course = self.Course.get()
        level = self.Level.get()
        
        check = getrecord('student', idno=idno)
        if check:
            messagebox.showerror("Notify","Error! IDno already exist!")
        else:
            okey = addrecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)
            if okey:
                messagebox.showinfo("Status", "STUDENT SAVED")
            else:
                messagebox.showerror("Status", "ERROR!")

    def newstudent(self):
        self.txt_idno.delete(0, 'end')
        self.txt_Lastname.delete(0, 'end')
        self.txt_Firstname.delete(0, 'end')
        self.Course.set('')
        self.Level.set('')
    
    def deletestudent(self):
        idno = self.txt_idno.get()
        if idno:
            confirm = messagebox.askyesno("Confirmation", "Would you like to delete this student?")
            if confirm:
                deleterecord('student', idno=idno)
                messagebox.showinfo("UPDATE:","Student Deleted")
            else:
                messagebox.showerror("UPDATE", "Deletion Canceled.")
        else:
            messagebox.showerror("Deletion Canceled.")
    def updatestudent(self):
        idno = self.txt_idno.get()
        check = getrecord('student',idno=idno)
        if check:
            if idno:
                confirm = messagebox.askyesno("Confirmation","Would you like to update this student?")
                data = getrecord('student', idno = idno)
                if confirm:
                    idno = self.txt_idno.get()
                    lastname = self.txt_Lastname.get()
                    firstname = self.txt_Firstname.get()
                    course = self.Course.get()
                    level = self.Level.get()
                    updaterecord('student', idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
                    student = data[0]
                    message = f" Student Idno:\t\t {student['idno']}\n Student Lastname:\t {student['lastname']}\n Student Firstname:\t {student['firstname']}\n Student Course:\t\t {student['course']}\n Student Level:\t\t {student['level']}"
                    messagebox.showinfo("Update", message)
                else:
                    messagebox.showerror("Update", "Update Student has been Canceled.")
            else:
                messagebox.showerror("Notify", "Update Student has been Canceled.")
        else:
            messagebox.showerror("Notify","Error! Student Doesn't Exist!")
                

def main() -> None:
    UserLogin()

if __name__ == "__main__":
    main()
