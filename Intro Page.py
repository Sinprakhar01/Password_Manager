from tkinter import *

root = Tk()
root.geometry("1590x800+0+0")
root.title("INTRO")
root.config(bg="#ea5455")


def lg_in():
    root.destroy()


title = Label(text="Welcome to Password Manager", font=("Verdana 15 underline", 50,"bold"),
              relief="groove",
              bg="#ea5455",
              fg="white")
title.place(x=0, y=150, relwidth=1)
des = Label(text="It Gives you a easy access to store,generate, and manage\n"
                 "your passwords for local applications and online services.",
            font=("helvetica", 25, "italic"),
            bg="#ea5455",
            fg='white')
des.place(x=330, y=350)
sign_up_btn = Button(text='Sign UP', bd=15, command=lg_in,
                     bg="slateblue1",font=
                    'bold')
sign_up_btn.place(x=700, y=550)

root.mainloop()
