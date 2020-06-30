import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Poblacion Total
N = 1000000
print(N)
print(1./10)
# Numero inicial de infectados y recuperador
infectados, recuperados = 1, 0
#Numero inicial de suceptibles a contagio
susceptibles = N - infectados - recuperados
#Tasa de contacto => beta, tasa de recuperacion => gamma (1/dias)
beta, gamma = 2.5, 0.5 
# Cantidad de lineas en la tabla
t = np.linspace(0, 20, 20)

# Ecuacion del modelo SIR
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Condiciones inciales del vector
y0 = susceptibles, infectados, recuperados

# Ecuaciones del modelo SIR sobre la cuadricula de tiempo
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Graficamos los datos diferenciando las distintas curvas
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000000, 'b', alpha=0.5, lw=2, label='Susceptibles')
ax.plot(t, I/1000000, 'r', alpha=0.5, lw=2, label='Infectados')
ax.plot(t, R/1000000, 'g', alpha=0.5, lw=2, label='Recuperados con inmunidad')
ax.set_xlabel('Tiempo /dias')
ax.set_ylabel('Numero (1000s)')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

