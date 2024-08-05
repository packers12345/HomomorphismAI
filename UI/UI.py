from tkinter import *

master = Tk()
Label(master,text = "Please enter the two engineering systems of interest").grid(row=1)
Label(master, text='Engineering System 1').grid(row=2)
Label(master, text='Engineering System 2').grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
Label(master,text="Please enter the system model").grid(row=4)
Lb = Listbox(master)
Lb.insert(1, 'System Model 1')
Lb.insert(2, 'System Model 2')
Lb.insert(3, 'System Model 3')
Lb.grid(row=5)
# Function for printing the
# selected listbox value(s)
def selected_item():
     
    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
    for i in Lb.curselection():
        Label(master,text=Lb.get(i)).grid(row=6)
 
# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(master, text='Print Selected', command=selected_item)
 
# Placing the button and listbox
btn.grid(row=8)
mainloop()