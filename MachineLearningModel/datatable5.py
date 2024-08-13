import pandas as pd

# Define the sets and relations
S_AE = ["S_AE1", "S_AE2"]
X_AE = ["IoX_A5", "IoX_A6"]
Y_AE = ["IoX_A3", "IoX_A4"]

N_AE = [
    (("S_AE1", "IoX_A5"), "S_AE1"),
    (("S_AE1", "IoX_A6"), "S_AE2"),
    (("S_AE2", "IoX_A5"), "S_AE1"),
    (("S_AE2", "IoX_A6"), "S_AE2")
]

R_AE = [
    ("S_AE1", "IoX_A3"),
    ("S_AE2", "IoX_A4")
]

F_AE = ["IF-A2", "IF-A3"]

P_AE = [
    ("IoX_A5", "IF-A3"),
    ("IoX_A6", "IF-A3"),
    ("IoX_A3", "IF-A2"),
    ("IoX_A4", "IF-A2")
]

# Create DataFrames for each set and relation

# N_AE (Transitions)
df_N_AE = pd.DataFrame(N_AE, columns=['N_AE_Transition', 'N_AE_Next_State'])

# R_AE (Relations)
df_R_AE = pd.DataFrame(R_AE, columns=['R_AE_State', 'R_AE_Output'])

# F_AE (Functions)
df_F_AE = pd.DataFrame(F_AE, columns=['F_AE'])

# P_AE (Pairs)
df_P_AE = pd.DataFrame(P_AE, columns=['P_AE_Input', 'P_AE_Function'])

# Determine the maximum length for padding
max_length = max(len(S_AE), len(X_AE), len(Y_AE), len(df_N_AE), len(df_R_AE), len(df_F_AE), len(df_P_AE))

# Ensure all lists are of the same length by padding with empty strings
def pad_list(lst, length):
    return lst + [''] * (length - len(lst))

# Creating padded lists
padded_S_AE = pad_list(S_AE, max_length)
padded_X_AE = pad_list(X_AE, max_length)
padded_Y_AE = pad_list(Y_AE, max_length)
padded_N_AE = pad_list(df_N_AE['N_AE_Transition'].tolist(), max_length)
padded_N_AE_next = pad_list(df_N_AE['N_AE_Next_State'].tolist(), max_length)
padded_R_AE_state = pad_list(df_R_AE['R_AE_State'].tolist(), max_length)
padded_R_AE_output = pad_list(df_R_AE['R_AE_Output'].tolist(), max_length)
padded_F_AE = pad_list(df_F_AE['F_AE'].tolist(), max_length)
padded_P_AE_input = pad_list(df_P_AE['P_AE_Input'].tolist(), max_length)
padded_P_AE_function = pad_list(df_P_AE['P_AE_Function'].tolist(), max_length)

# Create the final DataFrame
df_combined_AE = pd.DataFrame({
    'S_AE': padded_S_AE,
    'X_AE': padded_X_AE,
    'Y_AE': padded_Y_AE,
    'N_AE_Transition': padded_N_AE,
    'N_AE_Next_State': padded_N_AE_next,
    'R_AE_State': padded_R_AE_state,
    'R_AE_Output': padded_R_AE_output,
    'F_AE': padded_F_AE,
    'P_AE_Input': padded_P_AE_input,
    'P_AE_Function': padded_P_AE_function
})

# Print the combined DataFrame
print("Combined Table for AE:")
print(df_combined_AE)
