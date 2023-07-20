from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("1590x800+0+0")
root.title("Sign up")
root.config(bg="#ea5455")
frame1 = Frame(bg="white", bd=0)
frame1.place(x=550, y=30, width=500, height=740)

lbl_sign_up = Label(text="SIGN UP", font=("times new roman", 30, "bold"),
                    bg="white", fg="black")
lbl_sign_up.place(x=690, y=70)
username = Label(text="Enter your Email", font=("helvetica", 15,), bg="white")
username.place(x=600, y=200)
user_mail = Entry(font=("helvetica", 15), bg="white", relief="ridge", borderwidth=1)
user_mail.place(x=600, y=260, width=300)
user_mail.focus()
paswd = Label(text="New Password", font=("helvetica", 15,), bg="white")
paswd.place(x=600, y=330)
new_pswd = Entry(font=("helvetica", 15), show="*", relief="ridge", borderwidth=1)
new_pswd.place(x=600, y=380, width=300)
cfrm_paswd = Label(text="Confirm Password", font=("helvetica", 15,), bg="white")
cfrm_paswd.place(x=600, y=440, height=35)
cnfrm_pswd = Entry(font=("helvetica", 15), show="*", relief="ridge", borderwidth=1)
cnfrm_pswd.place(x=600, y=490, width=300)


def regs():
    if new_pswd.get() == "" or cnfrm_pswd.get() == "" or user_mail.get() == "":
        messagebox.showerror("Error", "All fields are Required")
    elif new_pswd.get() != cnfrm_pswd.get():
        messagebox.showerror("Error", "Password and Confirm Password doesn't  match")

    else:
        try:
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='45968060',
                database="datm")
            cur = db.cursor()
            cur.execute("INSERT INTO useraccounts (Email_id,password) VALUES(%s,%s)",(user_mail.get(), new_pswd.get()))
            db.commit()
            db.close()
            root.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error Due to {e}")
reg_btn = Button(text='Sign UP', bg="tomato", bd=15, command=regs,font='bold')
reg_btn.place(x=700, y=560)

root.mainloop()
