from tkinter import *
import tkinter.ttk as ttk


def payroll():

    main = Tk()
    main.title("Payroll Report")

    height = 650
    width = 1200

    screen_height = main.winfo_screenheight()
    screen_width = main.winfo_screenwidth()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    main.geometry('%dx%d+%d+%d' % (width, height, x, y))
    main.resizable(0, 0)

    # ==================== FRAMES =========================

    Title_top = Frame(main, height=50, width=1200, bd=5, relief="raised")
    Title_top.pack(side=TOP)

    Left = Frame(main, height=600, width=400, bd=5, bg="#FFD8CB")
    Left.pack(side=LEFT)

    Display = Frame(main, height=600, width=800, bd=5, relief="raised")
    Display.pack(side=RIGHT)

    # ==================== TITLE ==========================

    label_title = Label(Title_top, text="Dynalink Solutions INC.", font=("arial", 30, 'bold'), width=1200)
    label_title.pack()

    label_title2 = Label(Title_top, text="Payroll Summary Report", font=("arial", 12, 'bold'))
    label_title2.pack()

    # ==================== VARIABLES =======================

    global EMPLOYEE_NO, EMPLOYEE_NAME, RATE, DAYS, SSS, PHIL_HEALTH, CA, GROSS, DEDUCTIONS, NET_PAY, gross_amount, deduction_amount, netpay_amount

    # GIVEN
    EMPLOYEE_NO = StringVar()
    EMPLOYEE_NAME = StringVar()
    RATE = StringVar()
    DAYS= StringVar()
    # DEDUCTIONS
    SSS = StringVar()
    PHIL_HEALTH = StringVar()
    CA = StringVar()
    # SOLVE
    GROSS = StringVar()

    DEDUCTIONS = StringVar()

    NET_PAY = StringVar()

    # ==================== ENTRY LABEL ====================

    label_employee_no = Label(Left, text="Employee No. :", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_employee_no.place(x=5, y=20)

    entry_employee_no = Entry(Left, width=30, textvariable=EMPLOYEE_NO)
    entry_employee_no.place(x=180, y=30)

    label_employee_name = Label(Left, text="Employee Name:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_employee_name.place(x=5, y=60)

    entry_employee_name = Entry(Left, width=30, textvariable=EMPLOYEE_NAME)
    entry_employee_name.place(x=180, y=70)

    label_rate = Label(Left, text="Rate/Day:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_rate.place(x=5, y=100)

    entry_rate = Entry(Left, width=30, textvariable=RATE)
    entry_rate.place(x=180, y=110)

    label_days = Label(Left, text="No. of Days Worked:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_days.place(x=5, y=140)

    entry_days = Entry(Left, width=30, textvariable=DAYS)
    entry_days.place(x=180, y=150)

    label_gross = Label(Left, text="Gross Pay:", font=('arial', 11, 'bold'), bd=10, bg="#FFD8CB")
    label_gross.place(x=100, y=180)

    gross_amount = Label(Left, text="50000", font=('arial', 12, 'underline', 'bold'), bd=7, fg='#00008E', bg="#FFD8CB")
    gross_amount.place(x=200, y=180)

    label_deductions = Label(Left, text="Deductions:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_deductions.place(x=5, y=220)

    label_SSS = Label(Left, text="SSS:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_SSS.place(x=5, y=260)

    entry_SSS = Entry(Left, width=30, textvariable=SSS)
    entry_SSS.place(x=180, y=270)

    label_philhealth = Label(Left, text="Phil Health:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_philhealth.place(x=5, y=300)

    entry_philhealth = Entry(Left, width=30, textvariable=PHIL_HEALTH)
    entry_philhealth.place(x=180, y=310)

    label_ca = Label(Left, text="Cash Advance:", font=('arial', 12, 'bold'), bd=10, bg="#FFD8CB")
    label_ca.place(x=5, y=340)

    entry_ca = Entry(Left, width=30, textvariable=CA)
    entry_ca.place(x=180, y=350)

    label_tdeduction = Label(Left, text="Total Deductions:", font=('arial', 11, 'bold'), bd=10, bg="#FFD8CB")
    label_tdeduction.place(x=50, y=380)

    deduction_amount = Label(Left, text="500000", font=('arial', 12, 'underline', 'bold'), bd=7, fg='#B23F00', bg="#FFD8CB")
    deduction_amount.place(x=200, y=380)

    label_netpay = Label(Left, text="Net Pay: ", font=('arial', 11, 'bold'), bd=10, bg="#FFD8CB")
    label_netpay.place(x=180, y=420)

    netpay_amount = Label(Left, text="50000", font=('arial', 12, 'underline', 'bold'), bd=7, fg='#005400', bg="#FFD8CB")
    netpay_amount.place(x=260, y=420)

    # ========================= BUTTONS ===========================

    button_calculate = Button(Left, width=10, text="Calculate", font=('arial', 10, 'bold'), bd=5)
    button_calculate.place(x=80, y=500)

    button_save = Button(Left, width=10, text="Save", font=('arial', 10, 'bold'), bd=5)
    button_save.place(x=210, y=500)

    mainloop()


payroll()