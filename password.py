import random
import string

from tkinter import *
from tkinter import ttk

root = Tk()
strength = IntVar()
length = DoubleVar()
root.title('Password Generator')
def pass_gen(event):
    lengthy = int(PassLength.get())

    if strength.get() == 1:
        list = []
        for i in range(0, lengthy):
            list.append(random.choice(string.ascii_letters))
            password = ''.join(list)
            PassField.delete(0, 'end')
            PassField.insert(0, password)

    elif strength.get() == 2:
        list = []
        for i in range(0, lengthy):
            list.append(random.choice(string.digits + string.ascii_letters))
            password = ''.join(list)
            PassField.delete(0, 'end')
            PassField.insert(0, password)

    elif strength.get() == 3:
        list = []
        for i in range(0, lengthy):
            list.append(random.choice(string.punctuation + string.digits + string.ascii_letters))
            password = ''.join(list)
            PassField.delete(0, 'end')
            PassField.insert(0, password)
    

Radiobutton(root, text="Weak", variable=strength, value=1).grid(row=0, column=0, sticky=N)
Radiobutton(root, text="Strong", variable=strength, value=2).grid(row=0, column=1, sticky=N)
Radiobutton(root, text="Extra-strong", variable=strength, value=3).grid(row=0, column=2, sticky=N)

Label(root, text='Length').grid(row=1, column=0, sticky=W, padx=4)
PassLength = Scale(root, variable=length, from_=0, to=20,  orient=HORIZONTAL)
PassLength.grid(row=1, column=1)

Label(root, text='Password').grid(row=2, sticky=W, padx=4)
PassField = Entry(root)
PassField.grid(row=2, column=1, sticky=E, pady=4)

generateButton = Button(root, text='Generate')
generateButton.bind("<Button-1>", pass_gen)
generateButton.grid(row=2, column=2,sticky=E)

root.mainloop()
