from tkinter import *


def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

km_result_label = Label(text="Km")
km_result_label.grid(column=2,row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()