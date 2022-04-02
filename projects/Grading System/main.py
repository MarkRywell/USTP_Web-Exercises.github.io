from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
import information

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


def compute():
    global prelim, midterm, final, average

    prelim = PRELIM_GRADE.get()
    midterm = MIDTERM_GRADE.get()
    final = FINAL_GRADE.get()

    average = ((prelim + midterm + final) / 3)


def insertData():
    if STUDENT_ID.get() == "" or STUDENT_NAME.get() == "" or COURSE.get() == "" or SUBJECT.get() == "" or PRELIM_GRADE.get() == "" or MIDTERM_GRADE.get() == "" or FINAL_GRADE.get() == "":
        messagebox.showwarning("Incomplete!", "Please complete the information needed!")

    else:
        information.Database()
        information.cursor.execute(
            "INSERT INTO `member` (student_id, student_name, course, subject, prelim_grade, midterm_grade, final_grade, average_grade, grade_point, remarks) VALUES(?, ?, ?, ?, ?, ?)",
            (str(STUDENT_ID.get()), str(STUDENT_NAME.get()), str(COURSE.get()), str(SUBJECT.get()),
             str(PRELIM_GRADE.get()), str(MIDTERM_GRADE.get()), str(FINAL_GRADE.get())))
        information.conn.commit()
        STUDENT_ID.set("")
        STUDENT_NAME.set("")
        COURSE.set("")
        SUBJECT.set("")
        PRELIM_GRADE.set("")
        MIDTERM_GRADE.set("")
        FINAL_GRADE.set("")

        information.cursor.close()
        information.conn.close()

        displayData()


def displayData():
    tree.delete(*tree.get_children())
    information.Database()
    information.cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
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


# ==================VARIABLES======================

STUDENT_ID = IntVar()
STUDENT_NAME = StringVar()
COURSE = StringVar()
SUBJECT = StringVar()

PRELIM_GRADE = IntVar()
MIDTERM_GRADE = IntVar()
FINAL_GRADE = IntVar()
average = 0

REMARKS = StringVar()
GRADE_POINT = IntVar()

# ==================FRAMES========================

Top = Frame(main, width=1500, height=50, relief='raised', bd=5)
Top.pack(side=TOP)

Display = Frame(main, width=1100, height=550, relief='raised', bd=5)
Display.pack(side=RIGHT)

Enter = Frame(main, width=400, height=500)
Enter.pack(side=TOP)

Buttons = Frame(main, width=400, height=50, bd=5)
Buttons.pack(side=BOTTOM)

# ===================WIDGETS=======================

label_title = Label(Top, text="Student Information Database", font=('arial', 24, 'bold'), width=1100)
label_title.pack()

label_id = Label(Enter, text="Student ID: ", font=('arial', 12, 'bold'), bd=10)
label_id.grid(row=1, sticky=W)

entry_id = Entry(Enter, width=30, textvariable=STUDENT_ID)
entry_id.grid(row=1, column=1, sticky=E)

label_name = Label(Enter, text="Student Name: ", font=('arial', 12, 'bold'), bd=10)
label_name.grid(row=2, sticky=W)

entry_name = Entry(Enter, width=30, textvariable=STUDENT_NAME)
entry_name.grid(row=2, column=1, sticky=E)

label_course = Label(Enter, text="Course: ", font=('arial', 12, 'bold'), bd=10)
label_course.grid(row=3, sticky=W)

course = Combobox(Enter, width=27, textvariable=COURSE)
course['values'] = ('BS - Computer Engineering', 'BS - Information Technology', 'BS - TCM', 'BS - Data Science')
course.grid(row=3, column=1, sticky=E)

label_subject = Label(Enter, text="Subject: ", font=('arial', 12, 'bold'), bd=10)
label_subject.grid(row=4, sticky=W)

entry_subject = Entry(Enter, width=30, textvariable=SUBJECT)
entry_subject.grid(row=4, column=1, sticky=E)

prelim_label = Label(Enter, text="Prelim Grade: ", font=('arial', 12, 'bold'), bd=10)
prelim_label.grid(row=5, sticky=W)

prelim_entry = Entry(Enter, width=30, textvariable=PRELIM_GRADE)
prelim_entry.grid(row=5, column=1, sticky=E)

midterm_label = Label(Enter, text="Midterm Grade: ", font=('arial', 12, 'bold'), bd=10)
midterm_label.grid(row=6, sticky=W)

midterm_entry = Entry(Enter, width=30, textvariable=MIDTERM_GRADE)
midterm_entry.grid(row=6, column=1, sticky=E)

final_label = Label(Enter, text="Final Grade: ", font=('arial', 12, 'bold'), bd=10)
final_label.grid(row=7, sticky=W)

final_entry = Entry(Enter, width=30, textvariable=FINAL_GRADE)
final_entry.grid(row=7, column=1, sticky=E)

# ==================BUTTONS====================

compute_button = Button(Buttons, width=15, height=2, bd=5, text='Compute & Save', font=('arial', 10, 'bold'))
compute_button.grid(row=0, column=0, sticky=W)

exit_button = Button(Buttons, width=15, height=2, bd=5, text='Exit', font=('arial', 10, 'bold'), command=Exit)
exit_button.grid(row=0, column=1, sticky=E)

# ====================DATABASE=====================

tree = ttk.Treeview()

mainloop()