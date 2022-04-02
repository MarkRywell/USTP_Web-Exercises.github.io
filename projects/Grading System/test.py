from tkinter import *

main = Tk()
main.title("Student Information Database")
height = 600
width = 1200
screen_height = main.winfo_screenheight()
screen_width = main.winfo_screenwidth()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
main.geometry('%dx%d+%d+%d' % (width, height, x, y))
main.resizable(0, 0)


number = IntVar

Label(main, text=" ", textvariable=number, font=50).pack()




mainloop()