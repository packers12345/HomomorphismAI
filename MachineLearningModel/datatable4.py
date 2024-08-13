import pandas as pd

# Define the sets and relations
S_AD = ["S_AD1", "S_AD2"]
X_AD = ["IoX_A1", "IoX_A2"]
Y_AD = ["IoX_A5", "IoX_A6"]

N_AD = [
    (("S_AD1", "IoX_A1"), "S_AD1"),
    (("S_AD1", "IoX_A2"), "S_AD2"),
    (("S_AD2", "IoX_A1"), "S_AD1"),
    (("S_AD2", "IoX_A2"), "S_AD2")
]

R_AD = [
    ("S_AD1", "IoX_A5"),
    ("S_AD2", "IoX_A6")
]

F_AD = ["IF-A1", "IF-A3"]

P_AD = [
    ("IoX_A1", "IF-A1"),
    ("IoX_A2", "IF-A1"),
    ("IoX_A5", "IF-A3"),
    ("IoX_A6", "IF-A3")
]

# Create DataFrames for each set and relation

# N_AD (Transitions)
df_N_AD = pd.DataFrame(N_AD, columns=['N_AD_Transition', 'N_AD_Next_State'])

# R_AD (Relations)
df_R_AD = pd.DataFrame(R_AD, columns=['R_AD_State', 'R_AD_Output'])

# F_AD (Functions)
df_F_AD = pd.DataFrame(F_AD, columns=['F_AD'])

# P_AD (Pairs)
df_P_AD = pd.DataFrame(P_AD, columns=['P_AD_Input', 'P_AD_Function'])

# Determine the maximum length for padding
max_length = max(len(S_AD), len(X_AD), len(Y_AD), len(df_N_AD), len(df_R_AD), len(df_F_AD), len(df_P_AD))

# Ensure all lists are of the same length by padding with empty strings
def pad_list(lst, length):
    return lst + [''] * (length - len(lst))

# Creating padded lists
padded_S_AD = pad_list(S_AD, max_length)
padded_X_AD = pad_list(X_AD, max_length)
padded_Y_AD = pad_list(Y_AD, max_length)
padded_N_AD = pad_list(df_N_AD['N_AD_Transition'].tolist(), max_length)
padded_N_AD_next = pad_list(df_N_AD['N_AD_Next_State'].tolist(), max_length)
padded_R_AD_state = pad_list(df_R_AD['R_AD_State'].tolist(), max_length)
padded_R_AD_output = pad_list(df_R_AD['R_AD_Output'].tolist(), max_length)
padded_F_AD = pad_list(df_F_AD['F_AD'].tolist(), max_length)
padded_P_AD_input = pad_list(df_P_AD['P_AD_Input'].tolist(), max_length)
padded_P_AD_function = pad_list(df_P_AD['P_AD_Function'].tolist(), max_length)

# Create the final DataFrame
df_combined_AD = pd.DataFrame({
    'S_AD': padded_S_AD,
    'X_AD': padded_X_AD,
    'Y_AD': padded_Y_AD,
    'N_AD_Transition': padded_N_AD,
    'N_AD_Next_State': padded_N_AD_next,
    'R_AD_State': padded_R_AD_state,
    'R_AD_Output': padded_R_AD_output,
    'F_AD': padded_F_AD,
    'P_AD_Input': padded_P_AD_input,
    'P_AD_Function': padded_P_AD_function
})

# Print the combined DataFrame
print("Combined Table for AD:")
print(df_combined_AD)
