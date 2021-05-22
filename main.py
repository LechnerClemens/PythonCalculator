import tkinter as tk
from tkinter import Canvas, filedialog, Text

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=500, bg = "#263D42")
canvas.grid(columnspan=3, rowspan=3)

button7 = tk.Button(root, text="7", width=10, height=5)
button7.grid(column=0, row=0)
button8 = tk.Button(root, text="8", width=10, height=5)
button8.grid(column=1, row=0)
button9 = tk.Button(root, text="9", width=10, height=5)
button9.grid(column=2, row=0)
button4 = tk.Button(root, text="4", width=10, height=5)
button4.grid(column=0, row=1)
button5 = tk.Button(root, text="5", width=10, height=5)
button5.grid(column=1, row=1)
button6 = tk.Button(root, text="6", width=10, height=5)
button6.grid(column=2, row=1)
button1 = tk.Button(root, text="1", width=10, height=5)
button1.grid(column=0, row=2)
button2 = tk.Button(root, text="2", width=10, height=5)
button2.grid(column=1, row=2)
button3 = tk.Button(root, text="3", width=10, height=5)
button3.grid(column=2, row=2)

root.mainloop()
