import tkinter as tk
from tkinter import *
from tkinter import tkk
from tkinker.tkk import *

root = Tk()

# width and height
w = 100
h = 100

mainframe = tk.Frame(root)

# ----------------Login Page --------------------------#
loginframe = tk.Frame(mainframe)
contentFrame = tk.Frame(loginframe)

username_label = tk.Label(contentFrame, text='Username:')
password_label = tk.Label(contentFrame, text='Password')

username_entry = tk.Entry(contentFrame)
password_entry = tk.Entry(contentFrame)

mainframe.pack()
loginframe.pack()

username_label.grid(row=0, column=0)
username_label.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_label.grid(row=1, column=1)


root.mainloop()