from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
R1, R2, R3, R4 = symbols('R1, R2, R3, R4')
b = Beam(3, 200*(10**9), 400*(10**-6))
b.apply_load(10, 0, 0, end = 3)
b.apply_load(R1, 0, -1)
b.apply_load(R2, 1, -1)
b.apply_load(R3, 2, -1)
b.apply_load(R4, 3, -1)
# b.bc_deflection = [(0, 0), (8, 0)]
b.bc_deflection = [(0, 0), (1,0), (2,0), (3,0)]
b.solve_for_reaction_loads(R1, R2, R3, R4)
b.plot_shear_force()

