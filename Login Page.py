from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("1590x800+0+0")
root.title("PASSWORD MANAGER")
root.config(bg="#ea5455")


def login():
    if email_txt.get() == "" or paswd_txt == "":
        messagebox.showerror("Error", "All fields are Required")

    else:
        try:
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd="root",
                database="Password_manager")
            cur = db.cursor()
            cur.execute("SELECT * FROM Accounts WHERE Username=%s and Password=%s",
                        (email_txt.get(), paswd_txt.get()))
# cur.execute("ALTER TABLE UserAccounts userID int PRIMARY KEY AUTO_INCREMENT ")
            row = cur.fetchone()  # fetches that user credentials in a single tuple
            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password")

            else:
                root.destroy()
            db.commit()
            db.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to {e}")

frame1 = Frame(bg="white", bd=0)
frame1.place(x=550, y=30, width=500, height=740)


title = Label(text="Log In", bg="white", font=("Californian FB", 35, "bold"))
title.place(x=710, y=80)

label = Label(text="Username", compound=LEFT, font=("helvetica", 18), bg="white")
label.place(x=600, y=200)

email_txt = Entry(text="hell", font=("helvetica", 15), bg="white", relief="sunken", bd=1)
email_txt.place(x=600, y=260, width=300)
email_txt.focus()

pass_lbl = Label(text="Password", font=("helvetica", 18), bg="white")
pass_lbl.place(x=600, y=320)
paswd_txt = Entry(font=("helvetica", 15), show="*", relief="sunken", bd=1)
paswd_txt.place(x=600, y=380, width=300)

sign_in = Button(text='LOGIN', bd=15, bg="TOMATO",font='bold', command=login)
sign_in.place(x=720, y=500)

root.mainloop()
