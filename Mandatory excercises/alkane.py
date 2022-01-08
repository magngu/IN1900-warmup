# alkane.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------

# Declare variables
mass_C = 12.011  # g/mol, Carbon
mass_H = 1.0079  # g/mol, Hydrogen
n = [n for n in range(2, 10)]  # number of carbon atoms

# Print table
for n in n:
    m = 2 * n + 2
    mol_mass = n * mass_C + m * mass_H
    print(f"M(C{n}H{2*n+2}) = {mol_mass:.3f} g/mol")


"""
Test run:
>>>python3 alkane.py
M(C2H6) = 30.069 g/mol
M(C3H8) = 44.096 g/mol
M(C4H10) = 58.123 g/mol
M(C5H12) = 72.150 g/mol
M(C6H14) = 86.177 g/mol
M(C7H16) = 100.203 g/mol
M(C8H18) = 114.230 g/mol
M(C9H20) = 128.257 g/mol
>>>"""
