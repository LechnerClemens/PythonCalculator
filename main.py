import tkinter as tk
from tkinter import Canvas, filedialog, Text

numbers = []

def combinatenumber(num):
    #numbers.append(num)
    #T.delete(0.0, tk.END)
    #T.insert(tk.END, num)
    T['text'] += num



root = tk.Tk()




canvas = tk.Canvas(root, height=500, width=500, bg = "#263D42")
canvas.grid(columnspan=3, rowspan=4)

button7 = tk.Button(canvas, text="7", width=10, height=5, command=lambda:combinatenumber("7"))
button7.grid(column=0, row=0)
button8 = tk.Button(canvas, text="8", width=10, height=5, command=lambda:combinatenumber("8"))
button8.grid(column=1, row=0)
button9 = tk.Button(canvas, text="9", width=10, height=5, command=lambda:combinatenumber("9"))
button9.grid(column=2, row=0)
button4 = tk.Button(canvas, text="4", width=10, height=5, command=lambda:combinatenumber("4"))
button4.grid(column=0, row=1)
button5 = tk.Button(canvas, text="5", width=10, height=5, command=lambda:combinatenumber("5"))
button5.grid(column=1, row=1)
button6 = tk.Button(canvas, text="6", width=10, height=5, command=lambda:combinatenumber("6"))
button6.grid(column=2, row=1)
button1 = tk.Button(canvas, text="1", width=10, height=5, command=lambda:combinatenumber("1"))
button1.grid(column=0, row=2)
button2 = tk.Button(canvas, text="2", width=10, height=5, command=lambda:combinatenumber("2"))
button2.grid(column=1, row=2)
button3 = tk.Button(canvas, text="3", width=10, height=5, command=lambda:combinatenumber("3"))
button3.grid(column=2, row=2)

div = tk.Button(canvas, text="/", width=10, height=5)
div.grid(column=3, row=0)
mul = tk.Button(canvas, text="*", width=10, height=5)
mul.grid(column=3, row=1)
min = tk.Button(canvas, text="-", width=10, height=5)
min.grid(column=3, row=2)
plu = tk.Button(canvas, text="+", width=10, height=5)
plu.grid(column=3, row=3)

T = tk.Label(root, text="")
T.grid(column=0, row=4)

root.mainloop()

