from tkinter import *
import tkinter.ttk as ttk
import sqlite3
import information


def compute():

    if entry_employee_no.get() == "" or entry_employee_name.get() == "" or entry_rate.get() == "" or entry_days.get() == "" or entry_SSS.get() == "" or entry_philhealth.get() == "" or entry_ca.get() == "":
        txt_result.config(text="Please complete the Input!", fg='red')

    else:
        EMPLOYEE_NO.set(entry_employee_no.get())
        EMPLOYEE_NAME.set(entry_employee_name.get())
        Rate.set(entry_rate.get())
        Days.set(entry_days.get())
        SSS.set(entry_SSS.get())
        PHIL_HEALTH.set(entry_philhealth.get())
        CA.set(entry_ca.get())

        gross = (float(entry_rate.get()) * float(entry_days.get()))

        GROSS.set(round(gross, 2))

        total_deductions = (float(entry_SSS.get()) + float(entry_philhealth.get()) + float(entry_ca.get()))
        DEDUCTIONS.set(round(total_deductions, 2))

        net_pay = gross - total_deductions

        NET_PAY.set(round(net_pay, 2))

        insertData()


def insertData():

    information.Database()
    information.cursor.execute("""INSERT INTO 'employee'(
        employee_no, employee_name, rate, days, gross, SSS, phil_health, CA, deduction, net_pay) 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (str(EMPLOYEE_NO.get()), str(EMPLOYEE_NAME.get()), str(Rate.get()),
                                                  str(Days.get()), str(GROSS.get()), str(SSS.get()),
                                                  str(PHIL_HEALTH.get()), str(CA.get()), str(DEDUCTIONS.get()),
                                                  str(NET_PAY.get())))
    information.conn.commit()
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

    information.cursor.close()
    information.conn.close()
    txt_result.config(text="Data Added Successfully!", fg='blue')

    displayData()


def displayData():

    tree.delete(*tree.get_children())
    information.Database()
    information.cursor.execute("SELECT * FROM `employee` ORDER BY `employee_name` ASC")
    fetch = information.cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end',
                    values=(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
    information.cursor.close()
    information.conn.close()


def selected(event):
    update_button.config(state=NORMAL)
    delete_button.config(state=NORMAL)
    global mem_id






def delete():

    selItem = tree.focus()
    contents = (tree.item(selItem))
    selected_item = contents['values']
    tree.delete(selItem)
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("DELETE from employee WHERE mem_id = %d" % selected_item[0])
    conn.commit()
    conn.close()
    cursor.close()



def update():
    pass


def add_record():
    global add

    add = Tk()
    add.title("Add Record")

    height = 400
    width = 550

    screen_height = add.winfo_screenheight()
    screen_width = add.winfo_screenwidth()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    add.geometry('%dx%d+%d+%d' % (width, height, x, y))
    add.resizable(0, 0)

    # =====================VARIABLES=========================
    global EMPLOYEE_NO, EMPLOYEE_NAME, Rate, Days, SSS, PHIL_HEALTH, CA, txt_result
    global entry_employee_no,entry_employee_name,entry_rate,entry_days,entry_SSS,entry_ca,entry_philhealth
    # GIVEN
    EMPLOYEE_NO = StringVar()
    EMPLOYEE_NAME = StringVar()
    Rate = StringVar()
    Days = StringVar()
    # DEDUCTIONS
    SSS = StringVar()
    PHIL_HEALTH = StringVar()
    CA = StringVar()

    # =====================LABEL ENTRY=======================

    label_employee_no = Label(add, text="Employee No. :", font=('arial', 12, 'bold'), bd=10)
    label_employee_no.grid(row=1, sticky=W)

    entry_employee_no = Entry(add, width=40, textvariable=EMPLOYEE_NO)
    entry_employee_no.grid(column=1, row=1, sticky=E)

    label_employee_name = Label(add, text="Employee Name:", font=('arial', 12, 'bold'), bd=10)
    label_employee_name.grid(row=2, sticky=W)

    entry_employee_name = Entry(add, width=40, textvariable=EMPLOYEE_NAME)
    entry_employee_name.grid(column=1, row=2, sticky=E)

    label_rate = Label(add, text="Rate/Day:", font=('arial', 12, 'bold'), bd=10)
    label_rate.grid(row=3, sticky=W)

    entry_rate = Entry(add, width=40, textvariable=Rate)
    entry_rate.grid(column=1, row=3, sticky=E)

    label_days = Label(add, text="No. of Days Worked:", font=('arial', 12, 'bold'), bd=10)
    label_days.grid(row=4, sticky=W)

    entry_days = Entry(add, width=40, textvariable=Days)
    entry_days.grid(column=1, row=4, sticky=E)

    label_deductions = Label(add, text="Deductions:", font=('arial', 14, 'bold'), bd=10)
    label_deductions.grid(row=5, sticky=W)

    label_SSS = Label(add, text="SSS:", font=('arial', 12, 'bold'), bd=10)
    label_SSS.grid(row=6, sticky=W)

    entry_SSS = Entry(add, width=40, textvariable=SSS)
    entry_SSS.grid(column=1, row=6, sticky=E)

    label_philhealth = Label(add, text="Phil Health:", font=('arial', 12, 'bold'), bd=10)
    label_philhealth.grid(row=7, sticky=W)

    entry_philhealth = Entry(add, width=40, textvariable=PHIL_HEALTH)
    entry_philhealth.grid(column=1, row=7, sticky=E)

    label_ca = Label(add, text="Cash Advance:", font=('arial', 12, 'bold'), bd=10)
    label_ca.grid(row=8, sticky=W)

    entry_ca = Entry(add, width=40, textvariable=CA)
    entry_ca.grid(column=1, row=8, sticky=E)

    txt_result = Label(add)
    txt_result.grid(column=1, row=10, sticky=E)

    # ========================BUTTONS=========================

    add_button = Button(add, width=12, height=2, text="Add Record", font=('arial', 10, 'bold'), bd=5, command=compute)
    add_button.grid(column=2, row=10, sticky=W)


def record():
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

    global GROSS, DEDUCTIONS, NET_PAY, tree, update_button, delete_button

    GROSS = StringVar()

    DEDUCTIONS = StringVar()

    NET_PAY = StringVar()

    # ======================FRAMES============================
    Title_top = Frame(records, height=50, width=1100, bd=5, relief="raised")
    Title_top.pack(side=TOP)

    Buttons = Frame(records, height=50, width=1100, bd=5, relief=RAISED)
    Buttons.pack(side=TOP)

    Display = Frame(records, height=400, width=1100, bd=5, relief="raised")
    Display.pack(side=BOTTOM)

    # ======================TITLE============================
    label_title = Label(Title_top, text="Dynalink Solutions INC.", font=("arial", 30, 'bold'), width=1000)
    label_title.pack()

    label_title2 = Label(Title_top, text="Payroll Summary Report", font=("arial", 12, 'bold'))
    label_title2.pack()

    # ======================BUTTONS==========================

    add_button = Button(Buttons, width=12, height=1, text="Add Record", bd=5, command=add_record)
    add_button.place(x=50)

    update_button = Button(Buttons, width=12, height=1, text="Update Record", bd=5, command=update, state=DISABLED)
    update_button.place(x=180)

    delete_button = Button(Buttons, width=12, height=1, text="Delete Record", bd=5, command=delete, state=DISABLED)
    delete_button.place(x=310)

    # ======================TREE==============================

    scroll_vertical = Scrollbar(Display, orient=VERTICAL)
    scroll_horizontal = Scrollbar(Display, orient=HORIZONTAL)

    tree = ttk.Treeview(Display, columns=("Employee\'s No.", "Employee\'s Name", "Rate/Day", "No. of days Worked",
                                          "Gross Pay", "SSS", "Phil Health", "C/A", "Total Deductions", "Net Pay"),
                        selectmode="extended", height=600, yscrollcommand=scroll_vertical.set,
                        xscrollcommand=scroll_horizontal.set)
    scroll_vertical.config(command=tree.yview)
    scroll_vertical.pack(side=RIGHT, fill=Y)
    scroll_horizontal.config(command=tree.xview)
    scroll_horizontal.pack(side=BOTTOM, fill=X)

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
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=180)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=70)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=90)
    tree.column('#8', stretch=NO, minwidth=0, width=80)
    tree.column('#9', stretch=NO, minwidth=0, width=140)
    tree.column('#10', stretch=NO, minwidth=0, width=150)

    tree.pack()
    tree.bind("<Button-1>", selected)

    mainloop()


record()
