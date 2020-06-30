import numpy as np
import scipy.integrate 
import matplotlib.pyplot as plt


def SIRD_model(y, t, beta, gamma, delta):            #adding death separately from recovery
    S, I, R, D = y
    
    dS = -beta*S*I
    dI = beta*S*I - gamma*I - delta*I
    dR = gamma*I
    dD = delta*I
    
    return ([dS, dI, dR, dD])


t = np.linspace(0, 100,1000)

S0 = 0.9
I0 = 0.1
R0 = 0.0
D0 = 0.0
beta = 0.45
gamma = 0.1
delta = 0.15
Ro = beta/(delta+gamma)
print('R0 =',Ro)
solution = scipy.integrate.odeint(SIRD_model, [S0, I0, R0, D0], t, args=(beta, gamma, delta))



plt.figure(figsize=[6,4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.plot(t, solution[:, 3], label="D(t)")
plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("SIRD model")
plt.show()