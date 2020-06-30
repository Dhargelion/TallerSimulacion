import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Ecuaciones diferenciales del modelo SIR para ver la diferencia de las variables
#conforme pasa el tiempo
def derivada(state, t, N, beta):
    #beta tasacontacto  gamma tasa_recuperacion
    S, I, R, E, F = state
    # Cambio de poblacion susceptible conforme pasa el tiempo
    dEdt = S -I
    dSdt = -beta *E* S * I / N
    # Cambio de poblacion infectada conforme pasa el tiempo
    dIdt = 7*E-R-F
    # Cambio poblacion recuperada conforme pasa el tiempo
    dRdt = (1/7)*I*(1-0.03)
    dFdt = (1/14)*I*0.03
    return dSdt, dIdt, dRdt, dEdt, dFdt

tasa_contacto = 0.5
tasa_recuperacion = 0.25


susceptibles = 1000
recuperados = 0
infectados = 10
expuestos = 0
fallecidos=0
# El rango de dias
dias = range(0, 100)
#Mostramos los parametros iniciales
print("********Parametros iniciales********")
print("Poblacion total: ", susceptibles)
print("Tasa de contacto: ", tasa_contacto)
print("Tasa de recuperacion: ",tasa_recuperacion)
print("Numero de dias: ", dias)


# Usamos funcion para ecuaciones
ret = odeint(derivada,
             [susceptibles, infectados, recuperados, expuestos, fallecidos],
             dias,
             args=(susceptibles, tasa_contacto))
S, I, R, E, F = ret.T
# Creamos el dataFrame, el cual nos mostrara los datos de las varibles cada dia
df = pd.DataFrame({
    'suseptibles': S,
    'infectados': I,
    'recuperados': R,
    'expuestos': E,
    'fallecidos': F,
    'dias': dias
})

plt.style.use('ggplot')
df.plot(x='dias',
        y=['infectados', 'suseptibles', 'recuperados', 'expuestos', 'fallecidos' ],
        color=['#bb6424', '#aac6ca', '#cc8ac0','red','blue'],
        #kind='area',
        stacked=False)
print("***********Resultados Simulacion********")
print(df)
plt.show()