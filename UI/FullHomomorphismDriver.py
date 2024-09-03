from StateBasedAlgorithm import HomomorphismSystem, determine_homomorphism

# Define the mass-spring system
states_mass_spring = {'rest', 'moving'}
inputs_mass_spring = {0, 1}  # 0: no force, 1: force applied
outputs_mass_spring = {0, 1}  # 0: compressed, 1: extended
transitions_mass_spring = {('rest', 1): 'moving', ('moving', 0): 'rest'}
behaviors_mass_spring = {'rest': 0, 'moving': 1}

# Define the electrical circuit system
states_circuit = {'off', 'on'}
inputs_circuit = {0, 1}  # 0: switch off, 1: switch on
outputs_circuit = {0, 1}  # 0: off, 1: on
transitions_circuit = {('off', 1): 'on', ('on', 0): 'off'}
behaviors_circuit = {'off': 0, 'on': 1}

# Create system objects
mass_spring_system = HomomorphismSystem(states_mass_spring, inputs_mass_spring, outputs_mass_spring, transitions_mass_spring, behaviors_mass_spring)
circuit_system = HomomorphismSystem(states_circuit, inputs_circuit, outputs_circuit, transitions_circuit, behaviors_circuit)

# Determine homomorphism
degree_of_homomorphism, homomorphism_type = determine_homomorphism(mass_spring_system, circuit_system)
print(f"Degree of Homomorphism: {degree_of_homomorphism}")
print(f"Type of Homomorphism: {homomorphism_type}")