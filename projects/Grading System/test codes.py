from tkinter import *


main = Tk()
main.title("Python - Student Database")
height = 500
width = 500
screen_height = main.winfo_screenheight()
screen_width = main.winfo_screenwidth()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
main.geometry('%dx%d+%d+%d' % (width, height, x, y))
main.resizable(0, 0)


AVERAGE = DoubleVar()
PRELIM = StringVar()
MIDTERM = StringVar()
FINAL = StringVar()


def save():

    print(average1)
    str(average1)
    string = average1.split()
    print(string)


def solve():
    global prelim, midterm, final, average1

    prelim = int(PRELIM.get())
    midterm = int(MIDTERM.get())
    final = int(FINAL.get())

    average1 = ((prelim+midterm+final) / 3)


    save()

entry1 = Entry(main, textvariable=PRELIM, width=30).pack()
entry2 = Entry(main, textvariable=MIDTERM, width=30).pack()
entry3 = Entry(main, textvariable=FINAL, width=30).pack()
button1 = Button(main, width=20, height=2, text='save', command=solve).pack()



mainloop()