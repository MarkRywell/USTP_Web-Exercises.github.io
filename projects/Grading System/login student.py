from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from tkinter.ttk import Combobox
from tkinter import messagebox
import information


def compute():
    if STUDENT_ID.get() == "" or STUDENT_NAME.get() == "" or COURSE.get() == "" or SUBJECT.get() == "" or PRELIM_GRADE.get() == "" or MIDTERM_GRADE.get() == "" or FINAL_GRADE.get() == "":
        messagebox.showwarning("Incomplete!", "Please complete the information needed!")
    else:

        global average_num, AVERAGE

        average_num = ((int(PRELIM_GRADE.get()) + int(MIDTERM_GRADE.get()) + int(FINAL_GRADE.get())) / 3)
        AVERAGE.set(round(average_num, 2))

        remarks()


def remarks():

    global index, counter


    if 95 <= average_num <= 100:
        REMARKS.set('Excellent')
        index = 0
    elif 91 <= average_num <= 94.99:
        REMARKS.set("Superior")
        index = 1
    elif 88 <= average_num <= 90.99:
        REMARKS.set("Very Good")
        index = 2
    elif 86 <= average_num <= 87.99:
        REMARKS.set("Good")
        index = 3
    elif 84 <= average_num <= 85.99:
        REMARKS.set("Very Satisfactory")
        index = 4
    elif 82 <= average_num <= 83.99:
        REMARKS.set("High Average")
        index = 5
    elif 79 <= average_num <= 81.99:
        REMARKS.set("Average")
        index = 6
    elif 77 <= average_num <= 78.99:
        REMARKS.set("Fair")
        index = 7
    elif 75 <= average_num <= 76.99:
        REMARKS.set("Pass")
        index = 8
    elif 58 <= average_num < 75.99:
        REMARKS.set("Conditional if Pass/Failed")
        index = 9
    elif average_num < 58.99:
        REMARKS.set("Failing Final Grade")
        index = 10


    tunnel()


def tunnel():
    global gpe

    def GPE(index):
        switcher = {
            0: "1.00",
            1: "1.25",
            2: "1.50",
            3: "1.75",
            4: "2.00",
            5: "2.25",
            6: "2.50",
            7: "2.75",
            8: "3.00",
            9: "4.00",
            10: "5.00",
        }
        return switcher.get(index, "default")

    gpe = GPE(index)

    GRADE_POINT.set(gpe)

    insertData()

def insertData():

        information.Database()
        information.cursor.execute(
            "INSERT INTO `student` (student_id, student_name, course, subject, prelim_grade, midterm_grade, final_grade, average_grade, grade_point, remarks) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (str(STUDENT_ID.get()), str(STUDENT_NAME.get()), str(COURSE.get()), str(SUBJECT.get()),
             str(PRELIM_GRADE.get()), str(MIDTERM_GRADE.get()), str(FINAL_GRADE.get()), str(AVERAGE.get()), str(GRADE_POINT.get()), str(REMARKS.get())))
        information.conn.commit()
        STUDENT_ID.set("")
        STUDENT_NAME.set("")
        COURSE.set("")
        SUBJECT.set("")
        PRELIM_GRADE.set("")
        MIDTERM_GRADE.set("")
        FINAL_GRADE.set("")
        AVERAGE.set("")
        GRADE_POINT.set("")
        REMARKS.set("")

        information.cursor.close()
        information.conn.close()
        txt_result.config(text="Data saved & computed!", fg='blue', font=('arial', 11, 'bold'))

        displayData()


def displayData():
    tree.delete(*tree.get_children())
    information.Database()
    information.cursor.execute("SELECT * FROM `student` ORDER BY `student_name` ASC")
    fetch = information.cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end',
                    values=(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
    information.cursor.close()
    information.conn.close()




def Exit():
    confirm = messagebox.askquestion("Program Confirmation", "Do you wish to exit?")

    if confirm == 'yes':
        main.destroy()
        exit()


def student():
    logg.destroy()
    global main

    main = Tk()
    main.title("Python - Student Database")
    height = 600
    width = 1500
    screen_height = main.winfo_screenheight()
    screen_width = main.winfo_screenwidth()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main.geometry('%dx%d+%d+%d' % (width, height, x, y))
    main.resizable(0, 0)
    main.configure(bg='#E5E9FF')

    global STUDENT_ID, STUDENT_NAME, COURSE, SUBJECT, PRELIM_GRADE, MIDTERM_GRADE, FINAL_GRADE, AVERAGE, REMARKS, GRADE_POINT, tree, txt_result

    STUDENT_ID = StringVar()
    STUDENT_NAME = StringVar()
    COURSE = StringVar()
    SUBJECT = StringVar()

    PRELIM_GRADE = StringVar()
    MIDTERM_GRADE = StringVar()
    FINAL_GRADE = StringVar()
    AVERAGE = StringVar()

    REMARKS = StringVar()
    GRADE_POINT = StringVar()

    # ================== FRAMES ========================

    Top = Frame(main, width=1500, height=50, relief='raised', bd=5, bg='#00007B')
    Top.pack(side=TOP)

    Display = Frame(main, width=1100, height=550, relief='raised', bd=5)
    Display.pack(side=RIGHT)

    Enter = Frame(main, width=400, height=500, bg='#E5E9FF')
    Enter.pack(side=TOP)

    Buttons = Frame(main, width=400, height=50, bd=5, bg='#E5E9FF')
    Buttons.pack(side=BOTTOM)

    # ===================WIDGETS=======================

    label_title = Label(Top, text="USTP Student Information Database", font=('times new roman', 24, 'bold'), bg='#00007B', fg='#FFC500', width=1100)
    label_title.pack()

    label_id = Label(Enter, text="Student ID: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    label_id.grid(row=1, sticky=W)

    entry_id = Entry(Enter, width=30, textvariable=STUDENT_ID)
    entry_id.grid(row=1, column=1, sticky=E)

    label_name = Label(Enter, text="Student Name: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    label_name.grid(row=2, sticky=W)

    entry_name = Entry(Enter, width=30, textvariable=STUDENT_NAME)
    entry_name.grid(row=2, column=1, sticky=E)

    label_course = Label(Enter, text="Course: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    label_course.grid(row=3, sticky=W)

    course = Combobox(Enter, width=27, textvariable=COURSE, state='readonly')
    course['values'] = ('BS - Computer Engineering', 'BS - Information Technology', 'BS - TCM', 'BS - Data Science')
    course.grid(row=3, column=1, sticky=E)

    label_subject = Label(Enter, text="Subject: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    label_subject.grid(row=4, sticky=W)

    entry_subject = Entry(Enter, width=30, textvariable=SUBJECT)
    entry_subject.grid(row=4, column=1, sticky=E)

    prelim_label = Label(Enter, text="Prelim Grade: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    prelim_label.grid(row=5, sticky=W)

    prelim_entry = Entry(Enter, width=30, textvariable=PRELIM_GRADE)
    prelim_entry.grid(row=5, column=1, sticky=E)

    midterm_label = Label(Enter, text="Midterm Grade: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    midterm_label.grid(row=6, sticky=W)

    midterm_entry = Entry(Enter, width=30, textvariable=MIDTERM_GRADE)
    midterm_entry.grid(row=6, column=1, sticky=E)

    final_label = Label(Enter, text="Final Grade: ", font=('arial', 12, 'bold'), bd=10, bg='#E5E9FF')
    final_label.grid(row=7, sticky=W)

    final_entry = Entry(Enter, width=30, textvariable=FINAL_GRADE)
    final_entry.grid(row=7, column=1, sticky=E)

    txt_result = Label(Buttons, bg='#E5E9FF')
    txt_result.pack(side=TOP)


    # ==================BUTTONS========================

    compute_button = Button(Buttons, width=12, height=2, bd=5, text='Compute & Save', font=('arial', 10, 'bold'),
                            command=compute)
    compute_button.pack(side=LEFT)


    exit_button = Button(Buttons, width=12, height=2, bd=5, text='Exit', font=('arial', 10, 'bold'), command=Exit)
    exit_button.pack(side=RIGHT)

    # ====================DATABASE=====================

    scroll_vertical = Scrollbar(Display, orient=VERTICAL)
    scroll_horizontal = Scrollbar(Display, orient=HORIZONTAL)

    tree = ttk.Treeview(Display,
                        columns=("Student ID", "Student Name", "Course", "Subject", "Prelim Grade", "Midterm Grade",
                                 "Final Grade", "Average Grade", "Grade Point Equivalence", "Remarks"),
                        selectmode="extended",
                        height=550, yscrollcommand=scroll_vertical.set, xscrollcommand=scroll_horizontal.set)
    scroll_vertical.config(command=tree.yview)
    scroll_vertical.pack(side=RIGHT, fill=Y)
    scroll_horizontal.config(command=tree.xview)
    scroll_horizontal.pack(side=BOTTOM, fill=X)

    tree.heading('Student ID', text="Student ID", anchor=W)
    tree.heading('Student Name', text="Student Name", anchor=W)
    tree.heading('Course', text="Course", anchor=W)
    tree.heading('Subject', text="Subject", anchor=W)
    tree.heading('Prelim Grade', text="Prelim Grade", anchor=W)
    tree.heading('Midterm Grade', text="Midterm Grade", anchor=W)
    tree.heading('Final Grade', text="Final Grade", anchor=W)
    tree.heading('Average Grade', text="Average Grade", anchor=W)
    tree.heading('Grade Point Equivalence', text="Grade Point Equivalence", anchor=W)
    tree.heading('Remarks', text="Remarks", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=170)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=80)
    tree.column('#8', stretch=NO, minwidth=0, width=90)
    tree.column('#9', stretch=NO, minwidth=0, width=80)
    tree.column('#10', stretch=NO, minwidth=0, width=100)

    tree.pack()


def Database():
    global conn, cursor
    conn = sqlite3.connect("mark.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'Mark' AND `password` = 'markrywell'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('Mark', 'markrywell')")
    conn.commit()


def Login(event=None):
    Database()

    if USERNAME1.get() == "" or PASSWORD1.get() == "":
        warning1 = Tk()
        warning1.title("Unsuccessful Login!")
        height = 175
        width = 250
        sh = warning1.winfo_screenheight()
        sw = warning1.winfo_screenwidth()
        x = (sw / 2) - (width / 2)
        y = (sh / 2) - (height / 2)
        warning1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        warning1.resizable(0, 0)
        warning1.configure(bg="#FFAA9F")
        warning_label1 = Label(warning1, text="Please complete the login!", font=('times new roman', 15, 'bold'),
                               bg='#FFAA9F', fg='blue')
        warning_label1.place(x=125, y=60, anchor=N)


    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                       (USERNAME1.get(), PASSWORD1.get()))

        if cursor.fetchone() is not None:
            student()
            USERNAME1.set("")
            PASSWORD1.set("")


        else:
            warning2 = Tk()
            warning2.title("Unsuccessful Login!")
            warning2.configure(bg='#00076C')
            height = 175
            width = 350
            sh = warning2.winfo_screenheight()
            sw = warning2.winfo_screenwidth()
            x = (sw / 2) - (width / 2)
            y = (sh / 2) - (height / 2)
            warning2.geometry('%dx%d+%d+%d' % (width, height, x, y))
            warning2.resizable(0, 0)

            warning2_label = Label(warning2, text="Student's Username and Password\n Does not Match!", font=('times new roman', 15),
                                   fg="#FFFF00", bg='#00076C')
            warning2_label.place(x=175, y=40, anchor=N)
            warning2_label2 = Label(warning2, text="Please try again", font=('times new roman', 15, 'bold'),
                                    fg="#FFFF00", bg='#00076C')
            warning2_label2.place(x=175, y=95, anchor=N)

            USERNAME1.set("")
            PASSWORD1.set("")
    cursor.close()
    conn.close()


def admin_login():
    global logg
    logg = Tk()
    logg.title("Admin Login Application")
    width = 420
    height = 300

    screen_width = logg.winfo_screenwidth()
    screen_height = logg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    logg.geometry("%dx%d+%d+%d" % (width, height, x, y))
    logg.resizable(0, 0)

    global USERNAME1
    global PASSWORD1

    USERNAME1 = StringVar()
    PASSWORD1 = StringVar()
    # ==============================FRAMES=========================================
    Top = Frame(logg, bd=2, bg='#00007B', height=10, relief=GROOVE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(logg, height=200)
    Form.pack(side=TOP, pady=20)
    # ==============================LABELS=========================================
    lbl_title = Label(Top, text=" USTP Student User Login", font=('times new roman', 21, 'bold'), fg='#FFC500', bg='#00007B', bd=15)
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="Username:", font=('times new roman', 15), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('times new roman', 15), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)
    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME1, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD1, show="*", font=(14))
    password.grid(row=1, column=1)
    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", bg='blue', fg='white', width=45, command=Login)
    btn_login.grid(pady=25, row=3, columnspan=3)
    btn_login.bind('<Return>', Login)

    mainloop()


admin_login()
