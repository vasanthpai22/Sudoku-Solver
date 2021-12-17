from tkinter import Tk, Label, StringVar, Button, Entry
from pprint import pprint
window = Tk()
window.title("Sudoku")
window.geometry("380x375")
window.configure(bg='bisque2')
window.resizable(False, False)

# empty arrays for your Entrys and StringVars
text_var = []
entries = []

# callback function to get your StringVars
def get_mat():
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())
    res = [[int(ele) for ele in sub] for sub in matrix]
    return res

Label(window, text="Enter values for the sudoku grid :", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=20)
Label(window, text="(0 for empty boxes)", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=38)

x2 = 0
y2 = 0
rows, cols = (9, 9)
for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your StringVar and Entry
        text_var[i].append(StringVar())
        entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
        entries[i][j].place(x=70 + x2, y=60 + y2)
        x2 += 30
    y2 += 30
    x2 = 0
button= Button(window,text="Submit", bg='bisque3', width=10, command=get_mat)
button.place(x=150,y=340)

window.mainloop()
