# miles to km converter
# This has some error, but I haven't figured out yet.
from tkinter import *

def miles_to_kilo():
    miles= float(miles_input.get())
    km=miles*1.61
    kilo_convert_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height =300)
window.config(padx=50, pady=50)

# Miles input
miles_input = Entry(width=20)
miles_input.grid(colum=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(colum=2, row=0)


is_equal_label=Label(text = "is equal to")
is_equal_label.grid(colum=0, row=1)


kilo_convert_label = Label(text = "0")
kilo_convert_label.grid(colum=1, row=1)

km_label = Label(text="Km")
km_label.grid(colum=2, row=1)

calculate_button= Button(text="Calculate", command=miles_to_kilo)  # calculate only when called the miles to kilo conversion function
calculate_button(colum=1, row=2)






#
#


window.mainloop()