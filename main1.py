#GUI using Tkinter, *Args, **kwargs
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text= "New Text", font=("Arial",24,"bold"))
my_label.pack()

input = tkinter.Entry(width=10)
input.pack()

def button_clicked():
    my_label.config(text= input.get(), width=30)


button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()




window.mainloop()