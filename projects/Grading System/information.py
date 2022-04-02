import sqlite3
def Database():
 global conn, cursor
 conn = sqlite3.connect('student_info.db')
 cursor = conn.cursor()
 cursor.execute("CREATE TABLE IF NOT EXISTS `student` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, student_id TEXT, student_name TEXT, course TEXT, subject TEXT, prelim_grade TEXT, midterm_grade TEXT, final_grade TEXT, average_grade TEXT, grade_point TEXT, remarks TEXT)")


#==================================================
