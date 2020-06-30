import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Ecuaciones diferenciales del modelo SIR para ver la diferencia de las variables
#conforme pasa el tiempo
def derivada(state, t, N, beta, gamma):
    #beta tasacontacto  gamma tasa_recuperacion
    S, I, R = state
    # Cambio de poblacion susceptible conforme pasa el tiempo
    dSdt = -beta * S * I / N
    # Cambio de poblacion infectada conforme pasa el tiempo
    dIdt = beta * S * I / N - gamma * I
    # Cambio poblacion recuperada conforme pasa el tiempo
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

tasa_contacto = 0.5
tasa_recuperacion = 0.25


poblacion_total = 10000000
recuperados = 0
infectados = 1
susceptibles = poblacion_total - infectados - recuperados
# El rango de dias
dias = range(0, 100)
#Mostramos los parametros iniciales
print("********Parametros iniciales********")
print("Poblacion total: ", poblacion_total)
print("Tasa de contacto: ", tasa_contacto)
print("Tasa de recuperacion: ",tasa_recuperacion)
print("Numero de dias: ", dias)


# Usamos funcion para ecuaciones
ret = odeint(derivada,
             [susceptibles, infectados, recuperados],
             dias,
             args=(poblacion_total, tasa_contacto, tasa_recuperacion))
S, I, R = ret.T

# Creamos el dataFrame, el cual nos mostrara los datos de las varibles cada dia
df = pd.DataFrame({
    'suseptibles': S,
    'infectados': I,
    'recuperados': R,
    'dias': dias
})

plt.style.use('ggplot')
df.plot(x='dias',
        y=['infectados', 'suseptibles', 'recuperados'],
        color=['#bb6424', '#aac6ca', '#cc8ac0'],
        #kind='area',
        stacked=False)
print("***********Resultados Simulacion********")
print(df)
plt.show()