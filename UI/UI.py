from tkinter import *
from AbstractRunner import getHomomorphismVar
from StateBasedAlgorithm import HomomorphismSystem, determine_homomorphism

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

        self.print_button = Button(master, text='Print Selected', command=self.print_selected)
        self.print_button.grid(row=7, columnspan=2, pady=10)

        self.get_data_button = Button(master, text='Get Data', command=self.display_data)
        self.get_data_button.grid(row=8, columnspan=2, pady=10)

        self.get_homomorphism_button = Button(master, text='Get Homomorphism Var', command=self.get_homomorphism_var_display)
        self.get_homomorphism_button.grid(row=9, columnspan=2, pady=10)

        # New Question Box
        Label(master, text="Select a question or enter your own:").grid(row=10, columnspan=2, pady=10)

        self.question_listbox = Listbox(master, selectmode=SINGLE)
        self.question_listbox.insert(1, 'Solving for the degree of homomorphism')
        self.question_listbox.grid(row=11, columnspan=2, pady=10)

        self.custom_question_label = Label(master, text="Please enter your question:")
        self.custom_question_label.grid(row=12, column=0, padx=10, pady=5, sticky=W)

        self.custom_question_entry = Entry(master, width=50)
        self.custom_question_entry.grid(row=12, column=1, padx=10, pady=5)

        self.submit_question_button = Button(master, text='Submit Question', command=self.submit_question)
        self.submit_question_button.grid(row=13, columnspan=2, pady=10)

    def print_selected(self):
        # Clear previous output
        self.clear_output()

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

    def display_data(self):
        data = self.get_data()
        # Clear previous output
        self.clear_output()
        # Display the retrieved data
        Label(self.master, text=f'Engineering System 1: {data[0]}').grid(row=6, columnspan=2, pady=5)
        Label(self.master, text=f'Engineering System 2: {data[1]}').grid(row=7, columnspan=2, pady=5)
        for i, model in enumerate(data[2]):
            Label(self.master, text=f'Selected Model {i+1}: {model}').grid(row=8 + i, columnspan=2, pady=5)

    def clear_output(self):
        """Clear any previously displayed output."""
        for widget in self.master.winfo_children():
            if isinstance(widget, Label) and widget.grid_info()["row"] >= 6:
                widget.destroy()

    def get_data(self):
        """Retrieve the engineering systems and selected system models as a list."""
        if not self.master.winfo_exists():
            raise RuntimeError("The Tkinter window is closed.")
        
        eng_system1 = self.e1.get()
        eng_system2 = self.e2.get()
        selected_models = [self.Lb.get(i) for i in self.Lb.curselection()]
        
        # Return data as a list
        return [eng_system1, eng_system2, selected_models]

    def get_homomorphism_var(self, degree_of_homomorphism):
        """Return the degree_of_homomorphism."""
        return degree_of_homomorphism

    def get_homomorphism_var_display(self):
        """Retrieve and display the degree of homomorphism."""
        # Define the mass-spring system
        states_mass_spring = {'rest', 'compressed', 'extended'}
        inputs_mass_spring = {0, 1}  # 0: no force, 1: force applied
        outputs_mass_spring = {0, 1, 2}  # 0: rest, 1: compressed, 2: extended
        transitions_mass_spring = {('rest', 1): 'compressed', ('compressed', 0): 'rest', ('compressed', 1): 'extended', ('extended', 0): 'compressed'}
        behaviors_mass_spring = {'rest': 0, 'compressed': 1, 'extended': 2}

        # Define the electrical circuit system
        states_circuit = {'off', 'on'}
        inputs_circuit = {0, 1}  # 0: switch off, 1: switch on
        outputs_circuit = {0, 1}  # 0: off, 1: on
        transitions_circuit = {('off', 1): 'on', ('on', 0): 'off'}
        behaviors_circuit = {'off': 0, 'on': 1}

        mass_spring_system = HomomorphismSystem(states_mass_spring, inputs_mass_spring, outputs_mass_spring, transitions_mass_spring, behaviors_mass_spring)
        circuit_system = HomomorphismSystem(states_circuit, inputs_circuit, outputs_circuit, transitions_circuit, behaviors_circuit)
        degree_of_homomorphism, homomorphism_type = determine_homomorphism(mass_spring_system, circuit_system)
        value = degree_of_homomorphism
        # Clear previous output
        self.clear_output()
        # Display the degree of homomorphism
        Label(self.master, text=f'Degree of Homomorphism: {value}').grid(row=10, columnspan=2, pady=5)

    def submit_question(self):
        """Handle the submitted question."""
        selected_question_index = self.question_listbox.curselection()
        if selected_question_index:
            selected_question = self.question_listbox.get(selected_question_index)
            Label(self.master, text=f'Selected Question: {selected_question}').grid(row=14, columnspan=2, pady=5)

        custom_question = self.custom_question_entry.get()
        if custom_question:
            Label(self.master, text=f'Custom Question: {custom_question}').grid(row=15, columnspan=2, pady=5)

def create_app():
    root = Tk()
    app = EngineeringSystemsApp(root)
    return app, root

if __name__ == "__main__":
    app, root = create_app()
    root.mainloop()

