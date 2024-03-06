from iapws import IAPWS97

kelvin = 273.15 

#Inputs
temp_bottom_hole = 225 + kelvin     #float(input("Down Hole Temperature in C: "))  + kelvin
pressure_bottom_hole = 8 #float(input("Bottom Hole Pressure in MPa: "))   
pressure_seperator =  .04  #float(input("Pressure at Seperator in MPa: "))
pressure_condensor =  .01  #float(input("Pressure at Condensor in MPa: "))
turbine_efficiency =   .83 #float(input("Turbine Efficiency in percent: ")) / 100
turbine_exit_pressure = .01#float(input("Turbine Exit Pressure in MPa: "))
required_output =  10     #float(input("Required Power Output in MW: "))

#Calculations
h1 = steam=IAPWS97(P=pressure_bottom_hole, T=temp_bottom_hole)
h2 = h1
h3 = h1
quality = steam=IAPWS97(P=pressure_seperator, h=h1.h) 
steam_quality = quality.x * 100
enthalpy_steam = steam=IAPWS97(P=pressure_seperator, x=1)
enthalpy_water = steam=IAPWS97(P=pressure_seperator, x=0)
turbine_exit_enthalpy= steam=IAPWS97(P=turbine_exit_pressure, s=enthalpy_steam.s)
isentropic_work_turbine = enthalpy_steam.h - turbine_exit_enthalpy.h
actual_work_turbine = isentropic_work_turbine * turbine_efficiency
mass_flow_rate_of_steam_required = required_output / actual_work_turbine * 1000 # Converting to kg/s
mass_flow_rate_of_water_required = mass_flow_rate_of_steam_required / quality.x

#Outputs
print(f'Two Phase Enthalpy = {h1.h} kJ/kg')
print(f'Steam Quality = {steam_quality} %')
print(f'Steam Enthalpy = {enthalpy_steam.h} kJ/jg')
# print(f'Water Enthalpy {enthalpy_water.h} kJ/jg') # Water Enthalpy if needed
print(f'Steam Entropy = {enthalpy_steam.s} kJ/kg')
print(f'Turbine Exit Enthalpy = {turbine_exit_enthalpy.h} kJ/kg')
print(f'Isentropic Work of Turbine = {isentropic_work_turbine} kJ/kg')
print(f'Actual Work of Turbine = {actual_work_turbine} kJ/kg')
print(f'Mass Flow Rate of Steam Required = {mass_flow_rate_of_steam_required} kg/s')
print(f'Mass Flow Rate of Water Required = {mass_flow_rate_of_water_required} kg/s')


def add(a,b):
    return a+b





"""
Notes

sat_steam=IAPWS97(P=1,x=1)                #saturated steam with known P
sat_liquid=IAPWS97(T=370, x=0)            #saturated liquid with known T
steam=IAPWS97(P=2.5, T=500)               #steam with known P and T
# print(sat_steam.h, sat_liquid.h, steam.h) #calculated enthalpies

Definitions options:

T, P: Not valid for two-phases region
P, h
P, s
h, s
T, x: Only for two-phases region
P, x: Only for two-phases region
Returns:	prop –
The calculated instance has the following properties:

P: Pressure, [MPa]
T: Temperature, [K]
g: Specific Gibbs free energy, [kJ/kg]
a: Specific Helmholtz free energy, [kJ/kg]
v: Specific volume, [m³/kg]
rho: Density, [kg/m³]
h: Specific enthalpy, [kJ/kg]
u: Specific internal energy, [kJ/kg]
s: Specific entropy, [kJ/kg·K]
cp: Specific isobaric heat capacity, [kJ/kg·K]
cv: Specific isochoric heat capacity, [kJ/kg·K]
Z: Compression factor, [-]
fi: Fugacity coefficient, [-]
f: Fugacity, [MPa]
gamma: Isoentropic exponent, [-]
alfav: Isobaric cubic expansion coefficient, [1/K]
xkappa: Isothermal compressibility, [1/MPa]
kappas: Adiabatic compresibility, [1/MPa]
alfap: Relative pressure coefficient, [1/K]
betap: Isothermal stress coefficient, [kg/m³]
joule: Joule-Thomson coefficient, [K/MPa]
deltat: Isothermal throttling coefficient, [kJ/kg·MPa]
region: Region
v0: Ideal specific volume, [m³/kg]
u0: Ideal specific internal energy, [kJ/kg]
h0: Ideal specific enthalpy, [kJ/kg]
s0: Ideal specific entropy, [kJ/kg·K]
a0: Ideal specific Helmholtz free energy, [kJ/kg]
g0: Ideal specific Gibbs free energy, [kJ/kg]
cp0: Ideal specific isobaric heat capacity, [kJ/kg·K]
cv0: Ideal specific isochoric heat capacity [kJ/kg·K]
w0: Ideal speed of sound, [m/s]
gamma0: Ideal isoentropic exponent, [-]
w: Speed of sound, [m/s]
mu: Dynamic viscosity, [Pa·s]
nu: Kinematic viscosity, [m²/s]
k: Thermal conductivity, [W/m·K]
alfa: Thermal diffusivity, [m²/s]
sigma: Surface tension, [N/m]
epsilon: Dielectric constant, [-]
n: Refractive index, [-]
Prandt: Prandtl number, [-]
Pr: Reduced Pressure, [-]
Tr: Reduced Temperature, [-]
Hvap: Vaporization heat, [kJ/kg]
Svap: Vaporization entropy, [kJ/kg·K]"""