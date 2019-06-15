import math

l=float(input("l:"))
theta1=float(input("theta1:"))
theta2=float(input("theta2:"))
sp=float(input("sp:"))
np=float(input("np:"))
H = 0.38*10**(-4)
mu = 4*math.pi*10**(-2)
m = 8*((math.pi)*H*l/mu)*(1/((math.cos(theta2)/sp**2)-(math.cos(theta1)/np**2)))
print(math.cos(theta1))
print(math.cos(theta2))
print(m)