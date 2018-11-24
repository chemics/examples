"""
Calculate gas density from molecular weight, pressure, and temperature. Updated
by G.W. on 11/14/2018.
"""

import chemics as cm

# Calculate gas density
# ----------------------------------------------------------------------------

mw = 28.0134    # molecular weight of N2 gas [g/mol]
p = 101325      # pressure [Pa]
tk = 773        # temperature of gas [K]

rhog = cm.rhog(mw, p, tk)   # density of nitrogen gas [kg/m^3]

print(f'density of N2 gas = {rhog:.4f} kg/m^3')