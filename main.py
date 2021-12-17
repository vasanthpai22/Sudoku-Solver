# Python program to create a table
from tkinter import *
import Solver
a=10

class Table:
    def __init__(self,root, total_rows, total_columns):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width = 8, justify = CENTER, fg='black', font=('Arial',10,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = Solver.fun1()

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window S

root = Tk()

##root.attributes("-fullscreen",True)
root.configure(bg='black')

t = Table(root, total_rows, total_columns)
root.mainloop()