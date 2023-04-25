import tkinter as tk
from tkinter import *
#from tkinter import tkk
#from tkinker.tkk import *

root = Tk()

# width and height
w = 450
h = 525

# --------------- CENTER FORM --------------#
root.overrideredirect(1)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ------------- HEADER ---------------------#

headerframe = tk.Frame(root, highlightbackground='yellow', highlightcolor='yellow', highlightthickness=2, bg='black', width=w, height=70)
titleframe = tk.Frame(headerframe, bg='yellow', padx=1, pady=1)
title_label = tk.Label(titleframe, text='Login', padx=20, pady=5, bg='green', fg='#fff', font=('Tahoma', 24))
close_button = tk.Button(headerframe, text='x', borderwidth=1, relief='solid', font=('Verdana', 12))

headerframe.pack()
titleframe.pack()
title_label.pack()
close_button.pack()

titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)
close_button.place(x=410, y=10)


# Close window
def close_win():
    root.destroy()

close_button['command'] = close_win

# ---------------- END HEADER -------------#

mainframe = tk.Frame(root, width=w, height=h)

# ----------------Login Page --------------------------#
loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(registerframe, padx=30, pady=100, highlightbackground='yellow', highlightcolor='yellow', highlightthickness=2, bg='grey')

fullname_label_rg = tk.Label(login_contentframe, text='Fullname:', font=('Verdana', 16), bg='grey')
username_label_rg = tk.Label(login_contentframe, text='Userword:', font=('Verdana', 16), bg='grey')
password_label_rg = tk.Label(login_contentframe, text='Password:', font=('Verdana', 16), bg='grey')
confirmpass_label_rg = tk.Label(login_contentframe, text='Re-Password:', font=('Verdana', 16), bg='grey')
phone_label_rg = tk.Label(login_contentframe, text='Phone:', font=('Verdana', 16), bg='grey')
gender_label_rg = tk.Label(login_contentframe, text='Gender:', font=('Verdana', 16), bg='grey')
image_label_rg = tk.Label(login_contentframe, text='Image:', font=('Verdana', 16), bg='grey')


fullname_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
username_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
password_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
phone_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
gender_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
image_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))


register_button = tk.Button(register_contentframe, text="Register", font=('Verdana', 16), bg='#2980b9', fg='#fff',padx=25, pady=10, width=25)

go_logi_label = tk.Label(register_contentframe, text=">> already have an account? sign in", font=('Verdana', 10))


#mainframe.pack(fill='both', expand=1)
registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)

fullname_label_rg.grid(row=0, column=0, pady=10)
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=1, column=0, pady=10)
username_entry_rg.grid(row=1, column=1)

password_label_rg.grid(row=2, column=0, pady=10)
password_entry_rg.grid(row=2, column=1)

confirmpass_label_rg.grid(row=3, column=0, pady=10)
confirmpass_entry_rg.grid(row=3, column=0)

phone_label_rg.grid(row=4, column=0, pady=10)
phone_entry_rg.grid(row=4, column=1)

gender_label_rg.grid(row=5, column=0, pady=10)

image_label_rg.grid(row=6, column=0, pady=10)
image_entry_rg.grid(row=6, column=1)


register_button.grid(row=7, column=0, columnspan=2, pady=40)

go_logi_label.grid(row=8, column=0, columnspan=2, pady=40)


"""
fullname_label_rg   fullname_entry_rg
username_label_rg   username_entry_rg
password_label_rg   password_entry_rg
confirmpass_label_rg    confirmpass_entry_rg
phone_label_rg  phone_entry_rg
gender_label_rg  gender_entry_rg
image_label_rg  image_entry_rg
"""

# -------------- Register Pager -----------------#
registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, padx=30, pady=100, highlightbackground='yellow', highlightcolor='yellow', highlightthickness=2, bg='grey')

fullname_label_rg = tk.Label(register_contentframe, text='Fullname:', font=('Verdana', 16), bg='grey')
username_label_rg = tk.Label(register_contentframe, text='Userword:', font=('Verdana', 16), bg='grey')
password_label_rg = tk.Label(register_contentframe, text='Password:', font=('Verdana', 16), bg='grey')
confirmpass_label_rg = tk.Label(register_contentframe, text='Re-Password:', font=('Verdana', 16), bg='grey')
phone_label_rg = tk.Label(register_contentframe, text='Phone:', font=('Verdana', 16), bg='grey')
gender_label_rg = tk.Label(register_contentframe, text='Gender:', font=('Verdana', 16), bg='grey')
image_label_rg = tk.Label(register_contentframe, text='Image:', font=('Verdana', 16), bg='grey')


fullname_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
username_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
password_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
phone_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
gender_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))
image_entry_rg = tk.Entry(register_contentframe, font=('Verdana', 16))


register_button = tk.Button(register_contentframe, text="Register", font=('Verdana', 16), bg='#2980b9', fg='#fff',padx=25, pady=10, width=25)

go_logi_label = tk.Label(register_contentframe, text=">> already have an account? sign in", font=('Verdana', 10))


#mainframe.pack(fill='both', expand=1)
registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)

fullname_label_rg.grid(row=0, column=0, pady=10)
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=1, column=0, pady=10)
username_entry_rg.grid(row=1, column=1)

password_label_rg.grid(row=2, column=0, pady=10)
password_entry_rg.grid(row=2, column=1)

confirmpass_label_rg.grid(row=3, column=0, pady=10)
confirmpass_entry_rg.grid(row=3, column=0)

phone_label_rg.grid(row=4, column=0, pady=10)
phone_entry_rg.grid(row=4, column=1)

gender_label_rg.grid(row=5, column=0, pady=10)

image_label_rg.grid(row=6, column=0, pady=10)
image_entry_rg.grid(row=6, column=1)


register_button.grid(row=7, column=0, columnspan=2, pady=40)

go_logi_label.grid(row=8, column=0, columnspan=2, pady=40)





root.mainloop()