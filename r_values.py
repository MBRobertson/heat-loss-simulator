# R-Values
R = {
    'ROOF': 3.3,
    'WALL': 2.0,
    'FLOOR': 1.3,
    'WINDOW_DOUBLE_ALUMINUM': 0.26,
    'WINDOW_SINGLE_WOOD': 0.27,
    'WINDOW_DOUBLE_HIGH_PERFORMANCE': 0.48
}


def compute_heat_loss(A):
    out = 0
    for key in A:
        if key in R:
            out += A[key]/R[key]
    return out


# https://www.ohio.edu/mechanical/thermo/property_tables/air/air_Cp_Cv.html
AIR_Cp = 1.005  # Specific heat capacity of air
AIR_p = 1.2  # Density of air


def compute_air_energy(temp, volume):
    kg = volume * AIR_p
    kJ_per_C = AIR_Cp * kg
    kJ = kJ_per_C * temp
    return kJ


def compute_air_temp(energy, volume):
    kg = volume * AIR_p
    kJ_per_C = AIR_Cp * kg
    C = energy / kJ_per_C
    return C