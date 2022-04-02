AVERAGE = 93
REMARKS = None
switcher = None

if AVERAGE >= 95 and AVERAGE <= 100:
    REMARKS = "Excellent"
    index = 0
elif AVERAGE >= 91 and AVERAGE <= 94:
    REMARKS = "Superior"
    index = 1
elif AVERAGE >= 88 and AVERAGE <= 90:
    REMARKS = "Very Good"
    index = 2
elif AVERAGE >= 86 and AVERAGE <= 87:
    REMARKS = "Good"
    switcher = 3
elif AVERAGE >= 84 and AVERAGE <= 85:
    REMARKS = "Very Satisfactory"
    switcher = 4
elif AVERAGE >= 82 and AVERAGE <= 83:
    REMARKS = "High Average"
    switcher = 5
elif AVERAGE >= 79 and AVERAGE <= 81:
    REMARKS = "Average"
    switcher = 6
elif AVERAGE >= 77 and AVERAGE <= 78:
    REMARKS = "Fair"
    switcher = 7
elif AVERAGE >= 75 and AVERAGE <= 76:
    REMARKS = "Pass"
    switcher = 8
elif AVERAGE >= 58 and AVERAGE < 75:
    REMARKS = "Conditional if Pass/Failed"
    switcher = 9
elif AVERAGE < 58:
    REMARKS = "Failing Final Grade"
    switcher = 10

print(REMARKS)


print(index)



def GPE(index):

    switcher={
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

print(GPE(index))

gpe = GPE(index)

print("wassap nara oh: " + gpe)