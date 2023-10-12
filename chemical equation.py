from chempy import balance_stoichiometry

# Define the unbalanced chemical equation
equation = 'H2 + O2 -> H2O'

# Balance the equation
balanced_eq = balance_stoichiometry(equation)

# Print the balanced equation
print("Balanced Equation:", balanced_eq)

# Get the coefficients as a dictionary
coefficients = balanced_eq[0]

# Print the coefficients
print("Coefficients:", coefficients)
