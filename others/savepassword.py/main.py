from tkinter import *
import mysql.connector

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="tkinter"
)
    
window = Tk()
window.title("Login Panel")
window.geometry('400x400')

window.configure(background = "grey")

a = Label(window ,text = "Username").grid(row = 1,column = 0)
b = Label(window ,text = "Pass").grid(row = 2,column = 0)

a1 = Entry(window)
a1.grid(row = 1,column = 1)

b1 = Entry(window)
b1.grid(row = 2,column = 1)

def clicked():
    print(a1.get())
    print(b1.get())

    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO pass (name, pass) VALUES (%s, %s)", (a1.get(), b1.get()))
    db_connection.commit()

mainloop()

fetch_query = "select * from pass"
cursor = db_connection.cursor()
cursor.execute(fetch_query)
records = cursor.fetchall()

height = len(records) 
width = 3
cells = {}
for i in range(height): 
    for j in range(width): 
        b = Label(window, text=str(records[i][j]))
        d = i + 10
        b.grid(row=d, column=j)


btn = tk.Button(window ,text="Submit", command=clicked).grid(row=4,column=0)
window.mainloop()