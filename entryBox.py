from tkinter import *

def submit():
    username = entry.get()
    print('Hello' + username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(lenentry.get(), END)

window = Tk()

entry = Entry(window,
              font = ("Arial", 50))
entry.pack(side = LEFT)

submit_button = Button(window, text = "Submit", command = submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text = "Delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "Backspace", command = backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()