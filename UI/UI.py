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

        # Move the Get Homomorphism Var button here
        self.get_homomorphism_button = Button(master, text='Get Homomorphism Var', command=self.get_homomorphism_var_display)
        self.get_homomorphism_button.grid(row=7, columnspan=2, pady=10)

        # Move the Store Data button here
        self.store_data_button = Button(master, text='Store Data', command=self.store_data)
        self.store_data_button.grid(row=8, columnspan=2, pady=10)

        # New Question Options
        Label(master, text="Select a question:").grid(row=9, columnspan=2, pady=10)

        self.selected_question = StringVar(value='None')
        
        self.question1 = Radiobutton(master, text='Solving for the degree of homomorphism', variable=self.selected_question, value='Solving for the degree of homomorphism')
        self.question2 = Radiobutton(master, text='Another question', variable=self.selected_question, value='Another question')
        self.question3 = Radiobutton(master, text='Yet another question', variable=self.selected_question, value='Yet another question')

        self.question1.grid(row=10, column=0, padx=10, pady=5, sticky=W)
        self.question2.grid(row=10, column=1, padx=10, pady=5, sticky=W)
        self.question3.grid(row=11, column=0, padx=10, pady=5, sticky=W)

        self.stored_data = {}  # Initialize the dictionary to store data

        # Protocol to handle window closing event
        master.protocol("WM_DELETE_WINDOW", self.close_window)

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
        Label(self.master, text=f'Degree of Homomorphism: {value}').grid(row=12, columnspan=2, pady=5)

    def store_data(self):
        """Store the current data and display it."""
        eng_system1 = self.e1.get()
        eng_system2 = self.e2.get()
        selected_models = [self.Lb.get(i) for i in self.Lb.curselection()]
        question = self.selected_question.get()

        self.stored_data = {
            'engineering_system_1': eng_system1,
            'engineering_system_2': eng_system2,
            'system_models': selected_models,
            'question': question
        }

        # Print the stored data to the command line
        print(f"Data Stored: {self.stored_data}")

        # Clear previous output
        self.clear_output()

        # Display the stored data
        Label(self.master, text=f'Data Stored: {self.stored_data}').grid(row=13, columnspan=2, pady=5)

    def clear_output(self):
        """Clear any previously displayed output."""
        for widget in self.master.winfo_children():
            if isinstance(widget, Label) and widget.grid_info()["row"] >= 6:
                widget.destroy()

    def close_window(self):
        """Handle the window closing event."""
        self.master.quit()  # Stop the GUI event loop
        self.master.destroy()  # Destroy the Tkinter window

    def get_stored_data(self):
        """Retrieve the stored data."""
        return self.stored_data

def create_app():
    root = Tk()
    app = EngineeringSystemsApp(root)
    return app, root
