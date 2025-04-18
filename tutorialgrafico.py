
import matplotlib.pyplot as plt #importiamo la libreria matplotlip per il grafico

array = [1,2,3,4,5,6,7]#creiamo una matrice(quadro di numeri)
plt.figure(1,figsize=(7,4),facecolor="black")#creiamo il grafico e li diamo delle dimensioni e il colore
plt.plot(array,marker="o",color="cyan")#impostiamo la traiettoria,definendo di voler tracciare la variabile array,usiamo marker per i vari punti e li diamo alla traiettoria il colore cyan
plt.xlabel("X",color="white")#creiamo i label per vedere cosa rappresenta il grafico
plt.ylabel("Y",color="white")
plt.grid(True,color="Gray",linestyle="--",alpha=0.5)#impostiamo una griglia di colore grigia e trattegiata
plt.axhline(0,color="Gray")#la traiettoria parte dal punto 0
plt.legend()
a = plt.gca()
a.set_facecolor('black')#impostazioni default
a.tick_params(colors='white')#default
plt.show()#per vedere il grafico