from StateBasedAlgorithm import HomomorphismSystem, determine_homomorphism

# Flashlight A: 3 states
states_a = {'off', 'dim', 'bright'}
inputs_a = {'toggle'}
outputs_a = {'dark', 'dim light', 'bright light'}
transitions_a = {
    ('off', 'toggle'): 'dim',
    ('dim', 'toggle'): 'bright',
    ('bright', 'toggle'): 'off'
}
behaviors_a = {
    'off': 0,
    'dim': 1,
    'bright': 2
}

flashlight_a = HomomorphismSystem(states_a, inputs_a, outputs_a, transitions_a, behaviors_a)

# Flashlight B: 2 states
states_b = {'off', 'on'}
inputs_b = {'toggle'}
outputs_b = {'dark', 'light'}
transitions_b = {
    ('off', 'toggle'): 'on',
    ('on', 'toggle'): 'off'
}
behaviors_b = {
    'off': 0,
    'on': 2
}

flashlight_b = HomomorphismSystem(states_b, inputs_b, outputs_b, transitions_b, behaviors_b)

degree_of_homomorphism, homomorphism_type = determine_homomorphism(flashlight_a, flashlight_b)
print(f'Degree of Homomorphism: {degree_of_homomorphism}')
print(f'Type of Homomorphism: {homomorphism_type}')