#librerias necesarias para el ejercicio
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Lineplot:
    
    def __init__(self):
        #importacion del dataset para graficar los resultados
        data = pd.read_csv('archivo.csv')
        self.datos = pd.DataFrame(data)
        
        #figura
        sns.set(rc = {'figure.figsize':(8,4)})
        
        
        
    def confi_figura(ax):
      
        ax.set_title('Recuento de company por año')
        ax.set_ylabel('Recuento de company',labelpad = 25)
        ax.set_xlabel("Año",labelpad = 25)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
       
        
class Figura1(Lineplot):
    
    def figura1(self):
        
        self.datos.Date_Joined = pd.DatetimeIndex(self.datos['Date_Joined']).year
        
        data_final = self.datos.Date_Joined.value_counts()

        di = dict(sorted(data_final.items()))

        y = list(di.values())
        x = list(di.keys())
        
        ax = sns.lineplot(x,y,marker = "o")
        
        for x, y in zip(x, y):
            ax.text(x = x, 
            y = y-1, 
            s = '{:.0f}'.format(y)) 
            
        return Lineplot.confi_figura(ax)
        
fig1 = Figura1()
fig1.figura1()

plt.show()