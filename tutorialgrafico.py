#tutorial Salvatore Naro
import matplotlib.pyplot as plt 
array = [1,2,3,4,5,6,7]
plt.figure(1,figsize=(7,4),facecolor="black")#creiamo il grafico e li diamo delle dimensioni e il colore
plt.plot(array,marker="o",color="cyan")
plt.xlabel("X",color="white")
plt.ylabel("Y",color="white")
plt.grid(True,color="Gray",linestyle="--",alpha=0.5)
plt.axhline(0,color="Gray")
plt.legend()
a = plt.gca()
a.set_facecolor('black')
a.tick_params(colors='white')
plt.show()