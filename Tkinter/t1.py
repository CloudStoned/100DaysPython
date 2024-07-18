from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title('Gui')
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)
my_label.config(padx=20, pady=20)

my_label.config(text="New Text")

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=15)
input.grid(column=3, row=3)












window.mainloop()