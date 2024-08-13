import pandas as pd

# Define the sets and relations
S_A = ["S_A1", "S_A2"]
X_A = ["IoX_A1", "IoX_A2"]
Y_A = ["IoX_A3", "IoX_A4"]

N_A = [
    (("S_A1", "IoX_A1"), "S_A1"),
    (("S_A1", "IoX_A2"), "S_A2"),
    (("S_A2", "IoX_A1"), "S_A1"),
    (("S_A2", "IoX_A2"), "S_A2")
]

R_A = [
    ("S_A1", "IoX_A3"),
    ("S_A2", "IoX_A4")
]

F_A = ["IF-A1", "IF-A2"]

P_A = [
    ("IoX_A1", "IF-A1"),
    ("IoX_A2", "IF-A1"),
    ("IoX_A3", "IF-A2"),
    ("IoX_A4", "IF-A2")
]

# Create DataFrames for each set and relation

# N_A (Transitions)
df_N_A = pd.DataFrame(N_A, columns=['N_A_Transition', 'N_A_Next_State'])

# R_A (Relations)
df_R_A = pd.DataFrame(R_A, columns=['R_A_State', 'R_A_Output'])

# F_A (Functions)
df_F_A = pd.DataFrame(F_A, columns=['F_A'])

# P_A (Pairs)
df_P_A = pd.DataFrame(P_A, columns=['P_A_Input', 'P_A_Function'])

# Create a combined DataFrame with appropriate padding
max_length = max(len(S_A), len(X_A), len(Y_A), len(df_N_A), len(df_R_A), len(df_F_A), len(df_P_A))

# Ensure all lists are of the same length by padding with empty strings
def pad_list(lst, length):
    return lst + [''] * (length - len(lst))

# Creating padded lists
padded_S_A = pad_list(S_A, max_length)
padded_X_A = pad_list(X_A, max_length)
padded_Y_A = pad_list(Y_A, max_length)
padded_N_A = pad_list(df_N_A['N_A_Transition'].tolist(), max_length)
padded_N_A_next = pad_list(df_N_A['N_A_Next_State'].tolist(), max_length)
padded_R_A_state = pad_list(df_R_A['R_A_State'].tolist(), max_length)
padded_R_A_output = pad_list(df_R_A['R_A_Output'].tolist(), max_length)
padded_F_A = pad_list(df_F_A['F_A'].tolist(), max_length)
padded_P_A_input = pad_list(df_P_A['P_A_Input'].tolist(), max_length)
padded_P_A_function = pad_list(df_P_A['P_A_Function'].tolist(), max_length)

# Create the final DataFrame
df_combined = pd.DataFrame({
    'S_A': padded_S_A,
    'X_A': padded_X_A,
    'Y_A': padded_Y_A,
    'N_A_Transition': padded_N_A,
    'N_A_Next_State': padded_N_A_next,
    'R_A_State': padded_R_A_state,
    'R_A_Output': padded_R_A_output,
    'F_A': padded_F_A,
    'P_A_Input': padded_P_A_input,
    'P_A_Function': padded_P_A_function
})

# Print the combined DataFrame
print("Combined Table:")
print(df_combined)
