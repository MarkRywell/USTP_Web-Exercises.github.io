from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3

# AUTHOR = MARK RYWELL G. GAJE
# COURSE = BS - IT1R5

records = Tk()
records.title("Employee Records")

height = 600
width = 1100

screen_height = records.winfo_screenheight()
screen_width = records.winfo_screenwidth()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

records.geometry('%dx%d+%d+%d' % (width, height, x, y))
records.resizable(0, 0)

# ======================VARIABLES=========================
# GIVEN
EMPLOYEE_NO = IntVar()
EMPLOYEE_NAME = StringVar()
Rate = DoubleVar()
Days = IntVar()
# DEDUCTIONS
SSS = DoubleVar()
PHIL_HEALTH = DoubleVar()
CA = DoubleVar()
GROSS = DoubleVar()
DEDUCTIONS = DoubleVar()
NET_PAY = DoubleVar()


def Database():
    global conn, cursor
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    # CREATE A TABLE IN DATABASE
    cursor.execute("""CREATE TABLE IF NOT EXISTS `employee` 
                    (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    employee_no INTEGER, employee_name TEXT, rate REAL, days INTEGER, gross REAL, 
                    SSS REAL, phil_health REAL, CA REAL, deduction REAL, net_pay REAL)""")
    # DISPLAY RECORD IN TREE
    cursor.execute("SELECT * FROM `employee` ORDER BY `employee_no` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def yeah():
    global hey
    don = Toplevel()
    don.title("OKEH")
    height = 500
    width = 400

    screen_height = don.winfo_screenheight()
    screen_width = don.winfo_screenwidth()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    don.geometry('%dx%d+%d+%d' % (width, height, x, y))
    don.resizable(0, 0)

    hey = PhotoImage(file="lol.png")

    image_label = Label(don, image=hey)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)


def success():
    global bg
    kr = Toplevel()
    kr.title("OKEH")
    height = 600
    width = 700

    screen_height = kr.winfo_screenheight()
    screen_width = kr.winfo_screenwidth()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    kr.geometry('%dx%d+%d+%d' % (width, height, x, y))
    kr.resizable(0, 0)

    bg = PhotoImage(file="okeh.png")

    image_label = Label(kr, image=bg)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)


def succ_del():
    global dell
    panda = Toplevel()
    panda.title("OKEH")
    height = 280
    width = 480

    screen_height = panda.winfo_screenheight()
    screen_width = panda.winfo_screenwidth()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    panda.geometry('%dx%d+%d+%d' % (width, height, x, y))
    panda.resizable(0, 0)

    dell = PhotoImage(file="deleteee.png")

    image_label = Label(panda, image=dell)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)


def compute():
    if EMPLOYEE_NO.get() == "" or EMPLOYEE_NAME.get() == "" or Rate.get() == "" or Days.get() == "" or SSS.get() == "" or PHIL_HEALTH.get() == "" or CA.get() == "":
        txt_result.config(text="Please complete the Input!", fg='red')

    else:

        gross = (float(Rate.get()) * float(Days.get()))

        GROSS.set(round(gross, 2))

        total_deductions = (float(SSS.get()) + float(PHIL_HEALTH.get()) + float(CA.get()))
        DEDUCTIONS.set(round(total_deductions, 2))

        net_pay = gross - total_deductions

        NET_PAY.set(round(net_pay, 2))

        insertData()


def compute2():
    if EMPLOYEE_NO.get() == "" or EMPLOYEE_NAME.get() == "" or Rate.get() == "" or Days.get() == "" or SSS.get() == "" or PHIL_HEALTH.get() == "" or CA.get() == "":
        messagebox.showwarning('', 'Please make changes on the field!', icon="warning")

    else:

        gross = (float(Rate.get()) * float(Days.get()))

        GROSS.set(round(gross, 2))

        total_deductions = (float(SSS.get()) + float(PHIL_HEALTH.get()) + float(CA.get()))
        DEDUCTIONS.set(round(total_deductions, 2))

        net_pay = gross - total_deductions

        NET_PAY.set(round(net_pay, 2))

        updateData()


def insertData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO `employee`(
        employee_no, employee_name, rate, days, gross, SSS, phil_health, CA, deduction, net_pay) 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (int(EMPLOYEE_NO.get()), str(EMPLOYEE_NAME.get()), float(Rate.get()),
                                                  int(Days.get()), float(GROSS.get()), float(SSS.get()),
                                                  float(PHIL_HEALTH.get()), float(CA.get()), float(DEDUCTIONS.get()),
                                                  float(NET_PAY.get())))
    conn.commit()
    cursor.execute("SELECT * FROM `employee` ORDER BY `employee_no` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()
    EMPLOYEE_NO.set("")
    EMPLOYEE_NAME.set("")
    Rate.set("")
    Days.set("")
    GROSS.set("")
    SSS.set("")
    PHIL_HEALTH.set("")
    CA.set("")
    DEDUCTIONS.set("")
    NET_PAY.set("")
    success()


def updateData():
    if EMPLOYEE_NO.get() == "" or EMPLOYEE_NAME.get() == "" or Rate.get() == "" or Days.get() == "" or SSS.get() == "" or PHIL_HEALTH.get() == "" or CA.get() == "":
        messagebox.showwarning('', 'Please make changes on the field!', icon="warning")
    else:
        tree.delete(*tree.get_children())
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE `employee` SET `employee_no` = ?, `employee_name` = ?, `rate` = ?, `days` = ?, `gross` = "
                   "?, `SSS` = ?, `phil_health` = ?, `CA` = ?, `deduction` = ?,`net_pay` = ? WHERE `mem_id` = ?",
                   (int(EMPLOYEE_NO.get()), str(EMPLOYEE_NAME.get()), float(Rate.get()),
                    int(Days.get()), float(GROSS.get()), float(SSS.get()),
                    float(PHIL_HEALTH.get()), float(CA.get()), float(DEDUCTIONS.get()),
                    float(NET_PAY.get()), int(mem_id)))
    conn.commit()
    cursor.execute("SELECT * FROM `employee` ORDER BY `employee_no` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()
    EMPLOYEE_NO.set("")
    EMPLOYEE_NAME.set("")
    Rate.set("")
    Days.set("")
    GROSS.set("")
    SSS.set("")
    PHIL_HEALTH.set("")
    CA.set("")
    DEDUCTIONS.set("")
    NET_PAY.set("")
    upwindow.destroy()
    yeah()


def selected(event):
    update_button.config(state=NORMAL)
    delete_button.config(state=NORMAL)
    global mem_id


def delete():
    if not tree.selection():
        messagebox.showwarning('No Record Selected', 'Please Select a Record First!')
    else:
        selItem = tree.focus()
        contents = (tree.item(selItem))
        selected_item = contents['values']
        tree.delete(selItem)
        conn = sqlite3.connect("payroll.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM `employee` WHERE `mem_id` = %d" % selected_item[0])
        conn.commit()
        conn.close()
        succ_del()


def update():
    if not tree.selection():
        messagebox.showwarning('No Record Selected', 'Please Select a Record First!')
    else:

        global upwindow, mem_id, txt_result

        selItem = tree.focus()
        contents = (tree.item(selItem))
        selected_item = contents['values']
        mem_id = selected_item[0]

        EMPLOYEE_NO.set("")
        EMPLOYEE_NAME.set("")
        Rate.set("")
        Days.set("")
        SSS.set("")
        PHIL_HEALTH.set("")
        CA.set("")

        EMPLOYEE_NO.set(selected_item[1])
        EMPLOYEE_NAME.set(selected_item[2])
        Rate.set(selected_item[3])
        Days.set(selected_item[4])
        SSS.set(selected_item[6])
        PHIL_HEALTH.set(selected_item[7])
        CA.set(selected_item[8])

        upwindow = Toplevel()
        upwindow.title("Update a Record")

        height = 450
        width = 550

        screen_height = upwindow.winfo_screenheight()
        screen_width = upwindow.winfo_screenwidth()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        upwindow.geometry('%dx%d+%d+%d' % (width, height, x, y))
        upwindow.resizable(0, 0)
        upwindow.config(bg='#EABDAE')

        # ====================== LABEL ENTRY =========================

        Label(upwindow, text="UPDATE RECORD", font=('arial', 18, 'bold'), bd=10, bg='#EABDAE').grid(row=0, columnspan=1)

        label_employee_no = Label(upwindow, text="Employee No. :", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_employee_no.grid(row=1, sticky=W)

        entry_employee_no = Entry(upwindow, width=40, textvariable=EMPLOYEE_NO)
        entry_employee_no.grid(column=1, row=1, sticky=E)

        label_employee_name = Label(upwindow, text="Employee Name:", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_employee_name.grid(row=2, sticky=W)

        entry_employee_name = Entry(upwindow, width=40, textvariable=EMPLOYEE_NAME)
        entry_employee_name.grid(column=1, row=2, sticky=E)

        label_rate = Label(upwindow, text="Rate/Day:", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_rate.grid(row=3, sticky=W)

        entry_rate = Entry(upwindow, width=40, textvariable=Rate)
        entry_rate.grid(column=1, row=3, sticky=E)

        label_days = Label(upwindow, text="No. of Days Worked:", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_days.grid(row=4, sticky=W)

        entry_days = Entry(upwindow, width=40, textvariable=Days)
        entry_days.grid(column=1, row=4, sticky=E)

        label_deductions = Label(upwindow, text="Deductions:", font=('arial', 14, 'bold'), bd=10, bg='#EABDAE')
        label_deductions.grid(row=5, sticky=W)

        label_SSS = Label(upwindow, text="SSS:", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_SSS.grid(row=6, sticky=W)

        entry_SSS = Entry(upwindow, width=40, textvariable=SSS)
        entry_SSS.grid(column=1, row=6, sticky=E)

        label_philhealth = Label(upwindow, text="Phil Health:", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_philhealth.grid(row=7, sticky=W)

        entry_philhealth = Entry(upwindow, width=40, textvariable=PHIL_HEALTH)
        entry_philhealth.grid(column=1, row=7, sticky=E)

        label_ca = Label(upwindow, text="Cash Advance:", font=('arial', 12, 'bold'), bd=10, bg='#EABDAE')
        label_ca.grid(row=8, sticky=W)

        entry_ca = Entry(upwindow, width=40, textvariable=CA)
        entry_ca.grid(column=1, row=8, sticky=E)

        # ========================BUTTONS=========================

        update_button = Button(upwindow, width=12, height=2, text="Update Record", font=('arial', 10, 'bold'), bd=5,
                               command=compute2,
                               cursor='hand2')
        update_button.grid(column=1, row=10, sticky=E)


def add_record():
    global add, txt_result

    add = Toplevel()
    add.title("Add Record")

    height = 450
    width = 550

    screen_height = add.winfo_screenheight()
    screen_width = add.winfo_screenwidth()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    add.geometry('%dx%d+%d+%d' % (width, height, x, y))
    add.resizable(0, 0)
    add.config(bg='powder blue')

    # =====================LABEL ENTRY=======================
    Label(add, text="Adding Record", font=('times new roman', 15, 'bold'), bd=10, bg='powder blue').grid(row=0,
                                                                                                         columnspan=1)

    label_employee_no = Label(add, text="Employee No. :", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_employee_no.grid(row=1, sticky=W)

    entry_employee_no = Entry(add, width=40, textvariable=EMPLOYEE_NO)
    entry_employee_no.grid(column=1, row=1, sticky=E)

    label_employee_name = Label(add, text="Employee Name:", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_employee_name.grid(row=2, sticky=W)

    entry_employee_name = Entry(add, width=40, textvariable=EMPLOYEE_NAME)
    entry_employee_name.grid(column=1, row=2, sticky=E)

    label_rate = Label(add, text="Rate/Day:", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_rate.grid(row=3, sticky=W)

    entry_rate = Entry(add, width=40, textvariable=Rate)
    entry_rate.grid(column=1, row=3, sticky=E)

    label_days = Label(add, text="No. of Days Worked:", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_days.grid(row=4, sticky=W)

    entry_days = Entry(add, width=40, textvariable=Days)
    entry_days.grid(column=1, row=4, sticky=E)

    label_deductions = Label(add, text="Deductions:", font=('arial', 14, 'bold'), bd=10, bg='powder blue')
    label_deductions.grid(row=5, sticky=W)

    label_SSS = Label(add, text="SSS:", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_SSS.grid(row=6, sticky=W)

    entry_SSS = Entry(add, width=40, textvariable=SSS)
    entry_SSS.grid(column=1, row=6, sticky=E)

    label_philhealth = Label(add, text="Phil Health:", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_philhealth.grid(row=7, sticky=W)

    entry_philhealth = Entry(add, width=40, textvariable=PHIL_HEALTH)
    entry_philhealth.grid(column=1, row=7, sticky=E)

    label_ca = Label(add, text="Cash Advance:", font=('arial', 12, 'bold'), bd=10, bg='powder blue')
    label_ca.grid(row=8, sticky=W)

    entry_ca = Entry(add, width=40, textvariable=CA)
    entry_ca.grid(column=1, row=8, sticky=E)

    txt_result = Label(add, bg='powder blue')
    txt_result.grid(column=1, row=10, sticky=E)

    # ========================BUTTONS=========================

    add_button = Button(add, width=12, height=2, text="Add Record", font=('arial', 10, 'bold'), bd=5, command=compute,
                        cursor='hand2')
    add_button.grid(column=2, row=10, sticky=W)


# ======================FRAMES============================
Title_top = Frame(records, height=50, width=1100, bd=5, relief="raised", bg="#FFD8AE")
Title_top.pack(side=TOP)

Buttons = Frame(records, height=50, width=1100, bd=5, relief=RAISED, bg="#5BD0F0")
Buttons.pack(side=TOP)

Display = Frame(records, height=400, width=1100, bd=5, relief="raised")
Display.pack(side=BOTTOM)

# ======================TITLE============================
label_title = Label(Title_top, text="Dynalink Solutions INC.", font=("arial", 30, 'bold'), width=1000, bg="#FFD8AE")
label_title.pack()

label_title2 = Label(Title_top, text="Payroll Summary Report", font=("arial", 12, 'bold'), bg="#FFD8AE")
label_title2.pack()

# ======================BUTTONS==========================

add_button = Button(Buttons, width=12, height=1, text="Add Record", bd=5, command=add_record, bg="#5BD0F0",
                    cursor='hand2')
add_button.place(x=50)

update_button = Button(Buttons, width=12, height=1, text="Update Record", bd=5, command=update, state=DISABLED,
                       bg="#5BD0F0", cursor='hand2')
update_button.place(x=180)

delete_button = Button(Buttons, width=12, height=1, text="Delete Record", bd=5, command=delete, state=DISABLED,
                       bg="#5BD0F0", cursor='hand2')
delete_button.place(x=310)

# ======================TREE==============================

scroll_vertical = Scrollbar(Display, orient=VERTICAL)
scroll_horizontal = Scrollbar(Display, orient=HORIZONTAL)

tree = ttk.Treeview(Display,
                    columns=("mem_id", "Employee\'s No.", "Employee\'s Name", "Rate/Day", "No. of days Worked",
                             "Gross Pay", "SSS", "Phil Health", "C/A", "Total Deductions", "Net Pay"),
                    selectmode="extended", height=600, yscrollcommand=scroll_vertical.set,
                    xscrollcommand=scroll_horizontal.set)
scroll_vertical.config(command=tree.yview)
scroll_vertical.pack(side=RIGHT, fill=Y)
scroll_horizontal.config(command=tree.xview)
scroll_horizontal.pack(side=BOTTOM, fill=X)

tree.heading('mem_id', text="mem_id", anchor=W)
tree.heading('Employee\'s No.', text="Employee\'s No.", anchor=W)
tree.heading('Employee\'s Name', text="Employee\'s Name", anchor=W)
tree.heading('Rate/Day', text="Rate/Day", anchor=W)
tree.heading('No. of days Worked', text="No. of days Worked", anchor=W)
tree.heading('Gross Pay', text="Gross Pay", anchor=W)
tree.heading('SSS', text="SSS", anchor=W)
tree.heading('Phil Health', text="Phil Health", anchor=W)
tree.heading('C/A', text="C/A", anchor=W)
tree.heading('Total Deductions', text="Total Deductions", anchor=W)
tree.heading('Net Pay', text="Net Pay", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=50)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=180)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=70)
tree.column('#6', stretch=NO, minwidth=0, width=100)
tree.column('#7', stretch=NO, minwidth=0, width=90)
tree.column('#8', stretch=NO, minwidth=0, width=90)
tree.column('#9', stretch=NO, minwidth=0, width=80)
tree.column('#10', stretch=NO, minwidth=0, width=100)
tree.column('#11', stretch=NO, minwidth=0, width=100)

tree.pack()
tree.bind("<Double-Button-1>", selected)

Database()

records.mainloop()
