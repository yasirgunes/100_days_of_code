import tkinter


def convert_mile_to_km():
    miles = float(mile_entry.get())
    km = miles * 1.609
    label_3["text"] = round(km, 2)


# initialize the window
window = tkinter.Tk()
window.minsize(width=350, height=150)
window.resizable(False, False)
window.title("Mile to Kilometer")
window.config(pady=40, padx=60)

# entry
mile_entry = tkinter.Entry()
mile_entry.config(width=10)
mile_entry.grid(row=0, column=1)

# label 1
label_1 = tkinter.Label()
label_1["text"] = "miles"
label_1.grid(row=0, column=2)

# label 2
label_2 = tkinter.Label()
label_2["text"] = "is equal to"
label_2.grid(row=1, column=0)

# label 3
label_3 = tkinter.Label()
label_3["text"] = "0"
label_3.grid(row=1, column=1)

# label 4
label_4 = tkinter.Label()
label_4["text"] = "km"
label_4.grid(row=1, column=2)

# calculate button
convert = tkinter.Button(text="Convert", command=convert_mile_to_km)
convert.grid(row=2, column=1)

window.mainloop()
