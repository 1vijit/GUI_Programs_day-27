from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=100, pady=50)
km=0
#Entries
entry = Entry(width=5)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
entry.grid(column=1,row=0)


#Labels
label1 = Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

label3 = Label(text=km)
label3.grid(column=1,row=1)

label4 = Label(text="Km")
label4.grid(column=2,row=1)


#Buttons
def action():
    km = 1.609*float(entry.get())
    print(km)
    label3.config(text=km)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1,row=3)

window.mainloop()