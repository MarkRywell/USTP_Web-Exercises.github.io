from tkinter import *
import os


def redirect():
    reg.destroy()
    login()


def register_user():
    username_info = Username.get()
    password_info = Password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    user_reg.delete(0, END)
    pass_reg.delete(0, END)

    Label(reg, text="Registered Successfully!", fg='blue').place(x=90, y=190)
    Button(reg, text="Login", width=10, command=redirect).place(x=115, y=220)


def login_verify():
    Username1 = User_login.get()
    Password1 = Pass_login.get()
    user_log.delete(0, END)
    pass_log.delete(0, END)

    list_of_files = os.listdir()
    if Username1 in list_of_files:
        file1 = open(Username1, "r")
        verify = file1.read().splitlines()
        if Password1 in verify:

            success = Tk()
            success.title("Successful Login!")
            height = 175
            width = 350
            sh = success.winfo_screenheight()
            sw = success.winfo_screenwidth()
            x = (sw / 2) - (width / 2)
            y = (sh / 2) - (height / 2)
            success.geometry('%dx%d+%d+%d' % (width, height, x, y))
            success.resizable(0, 0)

            Top = Frame(success, bd=2, relief=GROOVE)
            Top.pack(side=TOP, fill=X)

            Label(success, text="Successful Login!", font=("times new roman", 15)).pack(pady=10)
            Button(success, text="Open BIODATA", font=('arial', 13), width=15, height=2).pack(pady=40)

        else:
            warning2 = Tk()
            warning2.title("Unsuccessful Login!")
            warning2.configure(bg='black')
            height = 175
            width = 350
            sh = warning2.winfo_screenheight()
            sw = warning2.winfo_screenwidth()
            x = (sw / 2) - (width / 2)
            y = (sh / 2) - (height / 2)
            warning2.geometry('%dx%d+%d+%d' % (width, height, x, y))
            warning2.resizable(0, 0)

            warning2_label = Label(warning2, text="Username or Password does not match!", font=('times new roman', 15),
                                   fg="red", bg='black')
            warning2_label.place(x=175, y=60, anchor=N)
            warning2_label2 = Label(warning2, text="HACKER DETECTED!", font=('times new roman', 15),
                                    fg="red", bg='black')
            warning2_label2.place(x=175, y=90, anchor=N)

    else:
        warning1 = Tk()
        warning1.title("Unsuccessful Login!")
        height = 175
        width = 400
        sh = warning1.winfo_screenheight()
        sw = warning1.winfo_screenwidth()
        x = (sw / 2) - (width / 2)
        y = (sh / 2) - (height / 2)
        warning1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        warning1.resizable(0, 0)

        warning_label1 = Label(warning1, text="User not found! Please login existing account!",
                               font=('times new roman', 15), fg='blue')
        warning_label1.place(x=200, y=60, anchor=N)


def register():
    global reg

    reg = Toplevel(window)
    reg.title("User Registration")

    width = 300
    height = 250
    sw = reg.winfo_screenwidth()
    sh = reg.winfo_screenheight()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)
    reg.geometry('%dx%d+%d+%d' % (width, height, x, y))
    reg.resizable(0, 0)

    global Username
    global Password
    global user_reg
    global pass_reg

    # ==================== VARIABLES ====================
    Username = StringVar()
    Password = StringVar()

    Label(reg, text="USER REGISTRATION", font=("courier", 15)).place(x=45, y=10)

    Label(reg, text="Please register details below.").place(y=50)

    Label(reg, text="Username:", font=("Calibri", 11)).place(y=78)

    user_reg = Entry(reg, textvariable=Username, width=20)
    user_reg.place(x=90, y=80)

    Label(reg, text="Password:", font=("Calibri", 11)).place(y=108)

    pass_reg = Entry(reg, textvariable=Password, width=20)
    pass_reg.place(x=90, y=110)

    Button(reg, text="Register", width=10, command=register_user).place(x=115, y=150)


def login():
    global log

    log = Toplevel(window)
    log.title("User Registration")

    width = 300
    height = 250
    sw = log.winfo_screenwidth()
    sh = log.winfo_screenheight()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)
    log.geometry('%dx%d+%d+%d' % (width, height, x, y))
    log.resizable(0, 0)

    global User_login
    global Pass_login

    User_login = StringVar()
    Pass_login = StringVar()

    global user_log
    global pass_log

    Label(log, text="USER LOGIN", font=("courier", 15)).place(x=90, y=10)

    Label(log, text="Please login username and password").place(y=50)

    Label(log, text="Username:", font=("Calibri", 11)).place(y=78)

    user_log = Entry(log, textvariable=User_login, width=20)
    user_log.place(x=90, y=80)

    Label(log, text="Password:", font=("Calibri", 11)).place(y=108)

    pass_log = Entry(log, textvariable=Pass_login, width=20, show="*")
    pass_log.place(x=90, y=110)

    Button(log, text="Login", width=10, command=login_verify).place(x=115, y=150)


def main():
    global window

    window = Tk()
    window.title("Basic Login Program")
    width = 400
    height = 300
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.resizable(0, 0)

    Top = Frame(window, bd=2, relief=GROOVE)
    Top.pack(side=TOP, fill=X)

    Label(Top, text="User Login Interface", font=('Comic Sans Ms', 20), height=1, fg='blue').pack(fill=X)

    Button(window, text="Register", width=15, height=1, font=("calibri", 13), command=register).pack(pady=40)

    Button(window, text="Login", width=15, height=1, font=("calibri", 13), command=login).pack(pady=40)

    mainloop()


main()