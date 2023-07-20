from tkinter import *
from random import *
import pyperclip
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import string


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    mail_entry.delete(0, END)
    username_entry.delete(0, END)


# -------------------------------Password Saver ---------------------------
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    Email_id = mail_entry.get()

    if website == "" or username == "" or password == "" or Email_id == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty. ")

    else:
        is_ok = messagebox.askyesno(title="Website", message=f"Do you confirm to add the details entered")

        if is_ok:
            try:
                db = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd='45968060',
                    database="datm")
                cur = db.cursor()
                cur.execute("INSERT INTO UserData (Website, Username, Password, Email_id) VALUES(%s, %s, %s, %s )",
                            (website, username, password, Email_id))
                db.commit()
                db.close()
                fetch_data()
                clear()

            except Exception as e:
                messagebox.showerror("Error", f"Error Due to {e}")


def update():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    Email_id = mail_entry.get()

    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='45968060',
            database="datm")
        cur = db.cursor()
        cur.execute("UPDATE UserData SET Username=%s, Password=%s, Email_id=%s WHERE Website=%s",
                    (username, password, Email_id, website))
        db.commit()
        db.close()
        fetch_data()
        clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error Due to {e}")


def delete():
    website = website_entry.get()
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='45968060',
            database="datm")
        cur = db.cursor()
        cur.execute("DELETE FROM UserData WHERE Website= %s",
                (website,))
        db.commit()
        db.close()
        fetch_data()
        clear()

    except Exception as e:
        messagebox.showerror("Error", f"Error Due to {e}")

window = Tk()
window.geometry("1590x800+0+0")
window.title("PASSWORD MANAGER")
window.config(bg="#ea5455")

frame1 = Frame(width=1482, height=740, bg="white")
frame1.place(x=20, y=30)

frame2 = Frame(frame1, width=600, height=570, bg="white", borderwidth=1, relief="solid")
frame2.place(x=30, y=150)

frame3 = LabelFrame(frame1, text='Password Generator', font=("helvetica", 18), width=800, height=260,
                    bg="white", borderwidth=1, relief="solid")
frame3.place(x=650, y=140)


def check():
    upper = upper_var.get()
    lower = lower_var.get()
    number = number_var.get()
    symbol = symbol_var.get()
    ps = " "

    if upper == 'on':
        ps += string.ascii_uppercase
    if lower == 'on':
        ps += string.ascii_lowercase
    if number == 'on':
        ps += string.digits
    if symbol == 'on':
        ps += string.punctuation

    else:
        generate_entry.delete(0, END)
        generate_entry.insert(0, "Please check any one option")
    return ps


def generate(ev):
    pswrd = check()
    password = ''
    for i in range(0, slider.get()):
        password = password + choice(pswrd)
    generate_entry.delete(0, END)
    password_entry.delete(0, END)
    generate_entry.insert(0, password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


upper_var = StringVar()
lower_var = StringVar()
number_var = StringVar()
symbol_var = StringVar()
label = Label(frame3, text='Customize Your Password', font=("helvetica", 18, 'underline'), bg='white')
label.place(x=100, y=80)

slider = Scale(frame3, label='Password Length', font=("helvetica", 12), from_=0, to=50, length=250, resolution=1,
               orient=HORIZONTAL, troughcolor='white', relief='groove', activebackground="#ea5455", bg='#ffcccb',
               bd=0, command=generate)
slider.place(x=100, y=140)

upper_check = Checkbutton(frame3, text='Uppercase', variable=upper_var, font=("helvetica", 13), bg='white',
                          onvalue='on', offvalue='off')
upper_check.place(x=380, y=130)
upper_check.select()
lower_check = Checkbutton(frame3, text='Lowercase', variable=lower_var, font=("helvetica", 13), bg='white',
                          onvalue='on', offvalue='off')
lower_check.place(x=380, y=180)
lower_check.select()

number_check = Checkbutton(frame3, text='Numbers', variable=number_var, font=("helvetica", 13), bg='white',
                           onvalue='on', offvalue='off')
number_check.place(x=525, y=130)
number_check.deselect()

symbol_check = Checkbutton(frame3, text='Symbols', variable=symbol_var, font=("helvetica", 13), bg='white',
                           onvalue='on', offvalue='off')
symbol_check.place(x=525, y=180)
symbol_check.deselect()

generate_entry = Entry(frame3, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)
generate_entry.place(x=150, y=20, height=35)

title = Label(text="Password Manager", font=("Oswald", 30, "bold"), bg="white")
title.place(x=590, y=60)

web_label = Label(frame2, text="Website or App Name", font=("helvetica", 20), bg="white")
web_label.place(x=40, y=50)

username_label = Label(frame2, text="Username", font=("helvetica", 20), bg="white")
username_label.place(x=40, y=150)

password_label = Label(frame2, text="Password", font=("helvetica", 20,), bg="white")
password_label.place(x=40, y=250)

mail_label = Label(frame2, text="Email Id", font=("helvetica", 20), bg="white")
mail_label.place(x=40, y=350)

website_entry = Entry(frame2, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)

website_entry.focus()
website_entry.place(x=40, y=100, height=25)

username_entry = Entry(frame2, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)
username_entry.place(x=40, y=200, height=25)

password_entry = Entry(frame2, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)
password_entry.place(x=40, y=300, height=25)

mail_entry = Entry(frame2, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)
mail_entry.place(x=40, y=400, height=25)

add_btn = Button(frame2, text='ADD', bd=10, bg="tomato", command=save, font='Bold')
add_btn.place(x=40, y=480)

update_btn = Button(frame2, text='UPDATE', bg='tomato', bd=10, command=update, font='bold')
update_btn.place(x=200, y=480)

delete_btn = Button(frame2, text='DELETE', bg="tomato", bd=10, command=delete, font='bold')
delete_btn.place(x=390, y=480)


# ==================== Treeview================

def get_cursor(event):

    cursor_row = password_tree.focus()
    contents = password_tree.item(cursor_row)
    row = contents['values']
    clear()
    website_entry.insert(0, row[0])
    username_entry.insert(1, row[1])
    password_entry.insert(2, row[2])
    mail_entry.insert(3, row[3])



frame4 = Frame(frame1, width=800, height=300, bg="white", borderwidth=1, relief="solid")
frame4.place(x=650, y=420)

style = ttk.Style()
style.configure("Treeview", rowheight=28)
style.map("Treeview", background=[('selected', '#ea5455')])
password_tree = ttk.Treeview(frame4, columns=("website", "username", "password", "mail_id"))
password_tree.tag_configure('oddrow', background='white')
password_tree.tag_configure('evenrow', background='#ffcccb')
password_tree.column("website", width=140)
password_tree.heading("username", text="Username", anchor="w")
password_tree.heading("website", text="Website", anchor="w")
password_tree.heading("password", text="Password", anchor="w")
password_tree.heading("mail_id", text="Email", anchor="w")
password_tree['show'] = 'headings'
password_tree.pack(expand=True, fill=BOTH)
password_tree.bind("<ButtonRelease-1>", get_cursor)


def fetch_data():
    count = 0
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='45968060',
            database="datm")
        cur = db.cursor()
        cur.execute("SELECT * FROM UserData ")
        rows = cur.fetchall()
        if len(rows) != 0:
            password_tree.delete(*password_tree.get_children())
            for row in rows:
                if count % 2 == 0:
                    password_tree.insert(parent='', index=END, values=row, tags='evenrow')
                    db.commit()
                else:
                    password_tree.insert(parent='', index=END, values=row, tags='oddrow')
                    db.commit()
                count+=1
        db.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error Due to {e}")

window.mainloop()
