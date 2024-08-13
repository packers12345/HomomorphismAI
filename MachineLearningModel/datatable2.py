import pandas as pd

# Define the sets and relations
S_B = ["S_B1", "S_B2", "S_B3"]
X_B = ["IoX_B1", "IoX_B2", "IoX_B3", "IoX_B4"]
Y_B = ["IoX_B5", "IoX_B6", "IoX_B7"]

N_B = [
    (("S_B1", "IoX_B1"), "S_B1"),
    (("S_B1", "IoX_B2"), "S_B2"),
    (("S_B1", "IoX_B3"), "S_B1"),
    (("S_B1", "IoX_B4"), "S_B1"),
    (("S_B2", "IoX_B1"), "S_B1"),
    (("S_B2", "IoX_B2"), "S_B2"),
    (("S_B2", "IoX_B3"), "S_B3"),
    (("S_B2", "IoX_B4"), "S_B2"),
    (("S_B3", "IoX_B1"), "S_B3"),
    (("S_B3", "IoX_B2"), "S_B3"),
    (("S_B3", "IoX_B3"), "S_B3"),
    (("S_B3", "IoX_B4"), "S_B2")
]

R_B = [
    ("S_B1", "IoX_B5"),
    ("S_B2", "IoX_B6"),
    ("S_B3", "IoX_B7")
]

F_B = ["IF-B1", "IF-B2"]

P_B = [
    ("IoX_B1", "IF-B1"),
    ("IoX_B2", "IF-B1"),
    ("IoX_B3", "IF-B1"),
    ("IoX_B4", "IF-B1"),
    ("IoX_B5", "IF-B2"),
    ("IoX_B6", "IF-B2"),
    ("IoX_B7", "IF-B2")
]

# Create DataFrames for each set and relation

# N_B (Transitions)
df_N_B = pd.DataFrame(N_B, columns=['N_B_Transition', 'N_B_Next_State'])

# R_B (Relations)
df_R_B = pd.DataFrame(R_B, columns=['R_B_State', 'R_B_Output'])

# F_B (Functions)
df_F_B = pd.DataFrame(F_B, columns=['F_B'])

# P_B (Pairs)
df_P_B = pd.DataFrame(P_B, columns=['P_B_Input', 'P_B_Function'])

# Determine the maximum length for padding
max_length = max(len(S_B), len(X_B), len(Y_B), len(df_N_B), len(df_R_B), len(df_F_B), len(df_P_B))

# Ensure all lists are of the same length by padding with empty strings
def pad_list(lst, length):
    return lst + [''] * (length - len(lst))

# Creating padded lists
padded_S_B = pad_list(S_B, max_length)
padded_X_B = pad_list(X_B, max_length)
padded_Y_B = pad_list(Y_B, max_length)
padded_N_B = pad_list(df_N_B['N_B_Transition'].tolist(), max_length)
padded_N_B_next = pad_list(df_N_B['N_B_Next_State'].tolist(), max_length)
padded_R_B_state = pad_list(df_R_B['R_B_State'].tolist(), max_length)
padded_R_B_output = pad_list(df_R_B['R_B_Output'].tolist(), max_length)
padded_F_B = pad_list(df_F_B['F_B'].tolist(), max_length)
padded_P_B_input = pad_list(df_P_B['P_B_Input'].tolist(), max_length)
padded_P_B_function = pad_list(df_P_B['P_B_Function'].tolist(), max_length)

# Create the final DataFrame
df_combined_B = pd.DataFrame({
    'S_B': padded_S_B,
    'X_B': padded_X_B,
    'Y_B': padded_Y_B,
    'N_B_Transition': padded_N_B,
    'N_B_Next_State': padded_N_B_next,
    'R_B_State': padded_R_B_state,
    'R_B_Output': padded_R_B_output,
    'F_B': padded_F_B,
    'P_B_Input': padded_P_B_input,
    'P_B_Function': padded_P_B_function
})

# Print the combined DataFrame
print("Combined Table for B:")
print(df_combined_B)
