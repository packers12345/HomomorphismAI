import pandas as pd

# Define the sets and relations
S_C = ["S_C1"]
X_C = ["IoX_C1"]
Y_C = ["IoX_C1"]

N_C = [
    (("S_C1", "IoX_C1"), "S_C1")
]

R_C = [
    ("S_C1", "IoX_C1")
]

F_C = ["IF-C1"]

P_C = [
    ("IoX_C1", "IF-C1")
]

# Create DataFrames for each set and relation

# N_C (Transitions)
df_N_C = pd.DataFrame(N_C, columns=['N_C_Transition', 'N_C_Next_State'])

# R_C (Relations)
df_R_C = pd.DataFrame(R_C, columns=['R_C_State', 'R_C_Output'])

# F_C (Functions)
df_F_C = pd.DataFrame(F_C, columns=['F_C'])

# P_C (Pairs)
df_P_C = pd.DataFrame(P_C, columns=['P_C_Input', 'P_C_Function'])

# Determine the maximum length for padding
max_length = max(len(S_C), len(X_C), len(Y_C), len(df_N_C), len(df_R_C), len(df_F_C), len(df_P_C))

# Ensure all lists are of the same length by padding with empty strings
def pad_list(lst, length):
    return lst + [''] * (length - len(lst))

# Creating padded lists
padded_S_C = pad_list(S_C, max_length)
padded_X_C = pad_list(X_C, max_length)
padded_Y_C = pad_list(Y_C, max_length)
padded_N_C = pad_list(df_N_C['N_C_Transition'].tolist(), max_length)
padded_N_C_next = pad_list(df_N_C['N_C_Next_State'].tolist(), max_length)
padded_R_C_state = pad_list(df_R_C['R_C_State'].tolist(), max_length)
padded_R_C_output = pad_list(df_R_C['R_C_Output'].tolist(), max_length)
padded_F_C = pad_list(df_F_C['F_C'].tolist(), max_length)
padded_P_C_input = pad_list(df_P_C['P_C_Input'].tolist(), max_length)
padded_P_C_function = pad_list(df_P_C['P_C_Function'].tolist(), max_length)

# Create the final DataFrame
df_combined_C = pd.DataFrame({
    'S_C': padded_S_C,
    'X_C': padded_X_C,
    'Y_C': padded_Y_C,
    'N_C_Transition': padded_N_C,
    'N_C_Next_State': padded_N_C_next,
    'R_C_State': padded_R_C_state,
    'R_C_Output': padded_R_C_output,
    'F_C': padded_F_C,
    'P_C_Input': padded_P_C_input,
    'P_C_Function': padded_P_C_function
})

# Print the combined DataFrame
print("Combined Table for C:")
print(df_combined_C)
