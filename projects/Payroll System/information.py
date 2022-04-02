import sqlite3
def Database():
    global conn, cursor
    conn = sqlite3.connect("payroll.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'employee' 
            (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            employee_no TEXT, employee_name TEXT, rate TEXT, days TEXT, gross TEXT, 
            SSS TEXT, phil_health TEXT, CA TEXT, deduction TEXT, net_pay TEXT)""")

# ===========================================================================================================