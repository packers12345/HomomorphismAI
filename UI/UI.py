from tkinter import *

class EngineeringSystemsApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Engineering Systems")

        Label(master, text="Please enter the two engineering systems of interest").grid(row=0, columnspan=2, pady=10)
        Label(master, text='Engineering System 1').grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Label(master, text='Engineering System 2').grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e1.grid(row=1, column=1, padx=10, pady=5)
        self.e2.grid(row=2, column=1, padx=10, pady=5)

        Label(master, text="Please enter the system model").grid(row=3, columnspan=2, pady=10)
        self.Lb = Listbox(master, selectmode=MULTIPLE)
        self.Lb.insert(1, 'System Model 1')
        self.Lb.insert(2, 'System Model 2')
        self.Lb.insert(3, 'System Model 3')
        self.Lb.grid(row=4, columnspan=2, pady=10)

        self.btn = Button(master, text='Print Selected', command=self.print_selected)
        self.btn.grid(row=7 + 3, columnspan=2, pady=10)

    def print_selected(self):
        # Clear previous output
        for widget in self.master.winfo_children():
            if isinstance(widget, Label) and widget.grid_info()["row"] >= 6:
                widget.destroy()
        
        # Display the two engineering systems
        eng_system1 = self.e1.get()
        eng_system2 = self.e2.get()
        Label(self.master, text=f'Engineering System 1: {eng_system1}').grid(row=6, columnspan=2, pady=5)
        Label(self.master, text=f'Engineering System 2: {eng_system2}').grid(row=7, columnspan=2, pady=5)

        # Display the selected items from the listbox
        selections = self.Lb.curselection()
        for i, index in enumerate(selections):
            selected_value = self.Lb.get(index)
            Label(self.master, text=f'Selected Model {i+1}: {selected_value}').grid(row=8 + i, columnspan=2, pady=5)

    def get_data(self):
        """Retrieve the engineering systems and selected system models as a list."""
        if not self.master.winfo_exists():
            raise RuntimeError("The Tkinter window is closed.")
        
        eng_system1 = self.e1.get()
        eng_system2 = self.e2.get()
        selected_models = [self.Lb.get(i) for i in self.Lb.curselection()]
        
        # Return data as a list
        return [eng_system1, eng_system2, selected_models]

def create_app():
    root = Tk()
    app = EngineeringSystemsApp(root)
    return app, root

