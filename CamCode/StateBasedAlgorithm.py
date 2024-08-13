class HomomorphismSystem:
    def __init__(self, states, inputs, outputs, transitions, behaviors):
        #definitions of all parts of the system
        self.states = states # distinct configurations of system
        self.inputs = inputs # external influences on system
        self.outputs = outputs # observable outcomes
        
        # rules or functions that descrive how system moves between states in response to input
        self.transitions = transitions
        self.behaviors = behaviors # mappings of inputs to outputs and transitions

    def get_behavior(self, state):
        return self.behaviors[state]

# finding the best matching state from one system to another based on behavior
def find_best_match(state_a_behavior, system_b, mapped_states):
    
    # state_a behavior: behavior of state from system A
    # system_b: the system in which we are searching for matches
    # mapped_states: a list of already mapped states to avoid duplication
    
    best_match = None
    best_match_diff = float('inf')
    
    for state_b in system_b.states: # loop through states in set of system states
        
        if state_b not in mapped_states: # if it has not been mapped yet
            # get the behavior of the current state and check the difference
            state_b_behavior = system_b.get_behavior(state_b)
            diff = abs(state_a_behavior - state_b_behavior)
            # if the difference is acceptable
            if diff < best_match_diff:
                best_match = state_b # set this as the new best match
                best_match_diff = diff
    
    return best_match

# determines the degree and type of homomorphism between two systems
def determine_homomorphism(system_a, system_b):
    mapped_states = {} # dict to store mapped states from A to B
    valid_transitions = 0 # counter of valid transitions
    
    # map each state in A to the best matching state in B
    for state_a in system_a.states:
        state_a_behavior = system_a.get_behavior(state_a)
        best_match = find_best_match(state_a_behavior, system_b, mapped_states.values())
        if best_match:
            mapped_states[state_a] = best_match
    
    # check transitions in A and validate them in B
    for (state_a, input_a), next_state_a in system_a.transitions.items():
        # make sure the state was actually mapped
        if state_a in mapped_states and next_state_a in mapped_states:
            state_b = mapped_states[state_a]
            next_state_b = mapped_states[next_state_a]
            if (state_b, input_a) in system_b.transitions and system_b.transitions[(state_b, input_a)] == next_state_b:
                valid_transitions += 1 # if the transition was valid, count it
    
    # determine the degree as ratio between valid and total transitions
    degree_of_homomorphism = valid_transitions / len(system_a.transitions)
    
    # check conformity
    sz_conformity = len(system_a.states) <= len(system_b.states)
    iz_conformity = set(system_a.inputs) == set(system_b.inputs)
    oz_conformity = set(system_a.outputs) <= set(system_b.outputs)
    nz_conformity = degree_of_homomorphism == 1
    rz_conformity = all(system_a.get_behavior(s) == system_b.get_behavior(mapped_states[s]) for s in system_a.states if s in mapped_states)

    # determine the type
    if all([sz_conformity, iz_conformity, oz_conformity, nz_conformity, rz_conformity]):
        homomorphism_type = "Isomorphism"
    elif sz_conformity and iz_conformity and rz_conformity:
        homomorphism_type = "Epimorphism"
    elif oz_conformity and nz_conformity:
        homomorphism_type = "Monomorphism"
    else:
        homomorphism_type = "General Homomorphism"

    return degree_of_homomorphism, homomorphism_type