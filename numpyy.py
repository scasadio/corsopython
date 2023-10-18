import numpy as np
arr=np.array([1,2,3,4,5])   #parte da una lista ma crea un array
#moltiplicandolo per 5, moltiplica tutti i numeri per 5
#moltiplicandolo per 5, la lista viene ripetuta per 5 volte
print(arr)

#creare array
arr=np.array(42) #array di 0 dimensioni che contiene sono uno scalare, perche non ha le quadre
arr1D=np.array([1,2,3,4,5])  #array di 1 dimensione
arr2D=np.array([[1,2,3,4,5],
               [1,2,3,4,5]])  #gli array devono avere le stesse dimensioni
array3D=np.array([
                [[1,2,3],[4,5,6]],
                [[1,2,3],[4,5,6]]
                ])

print(array3D.ndim)

arr5D=np.array([1,2,3],ndmin=5)
print(arr5D.ndim) #controllare la dimensione degli array

arrArange=np.arange(5,50,5)
print(arrArange)  #creo un array che arte da 5, arriva a 50 escluso, facendo steps di 5

arrZeros=np.zeros(3) #array di una dimensione con 3 zeri
arrZeros=np.zeros((2,2,4))   #3 dimensioni, la prima dimensione(verticale) contiene 2 dim, la seconda (orizz) ne contiene 2, la 3(numero di elementi nell'array), ne contiene 4

print(arrZeros)


#indicizzazione degli array 
arr1D=np.array([1,2,3,4,5])  
arr3D=np.array([
                [[1,2,3,4,5],[6,7,8,9,10]],
                [[11,12,13,14,15],[16,17,18,19,20]]
                ])
#voglio prendere il numero 14
print(arr3D[1,0,3])  #secondo elemento,1 elemento, 4 elemento


#indicizzazione negativa
arr1D=np.array([1,2,3,4,5])
print(arr1D[-1])  #5
print(arr3D[-1,0,-2])  #14


###SLICING ARRAY
arr1D=np.array([1,2,3,4,5])
print(arr1D[:2]) #prendo i primi due elementi   
#print(arr1D[-1,-3])    il numero a sx deve essere quello di sinistra

#step
print(arr1D[0:-1:2]) #tutti con step di 2

arr2D=np.array([[1,2,3,4,5],
               [1,2,3,4,5]])
print(arr2D[1,1:])

arr3D=np.array([
                [[1,2,3,4,5],[6,7,8,9,10]],
                [[11,12,13,14,15],[16,17,18,19,20]]
                ])
print(arr3D[1,1,::2 ])



###TIPI DI DATI
#boolean                  |b
#unsigned byte            |B
#(signed)integer          |i
#unsigned integer         |u
#floating-point           |f
#complex-floating point   |c
#timedelta                |m
#datetime                 |M
#(python)objects          |O
#string                   |S
#Unicode string           |U
#fixed chunk of memory
            #other type   |V


arr= np.array([1,2,3,4,5])
arr=np.array(["a","b","c"])
print(arr.dtype)

arr=np.array(["1","2","3","4","5"],dtype="i")
print(arr+4)

arr=np.array(["1","2","3","4","5"])
arrInt=arr.astype("i")  #(int)  trasforma l'array se possibile
print(arrInt+4)

###VIEW E COPY
arr=np.array([1,2,3])
arrCopy=arr.copy()
arr[0]=10
print(arr) #cambio array ma ilprimo non viene modificato perche ne abbiamo creato una copia
print(arrCopy)

arrCopy=arr.view()
arrCopy[0]=10  #qui modifico l'array ma con view cambiano entrambi
print(arr)
print(arrCopy)

#vedere se qualcuno è proprietario dei dati
print(arr.base) #none, sappiamo che array è propritario di dati
print(arrCopy.base) #non è proprietario di dati, fa riferimento all'array quindi sappiamo che è generato da una view
#la copy ritorna none perche essendo una copia nuova dell'array diventa proprietaria di dati


###SHAPE E RESHAPE
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)  #2 array da 3 elementi

print(arr.reshape(-1))  #cambio la shape
print(arr.reshape(-1).base)  #ci riporta quale è la sua base, non è proprietario di dati (non ritorna none)

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(4,3)) #4*3=12
    #cambia la forma dell'array, da 1 a 2 dimensioni
print(arr.reshape(2,2,3))
    #da 1 a 3 dimensioni

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.flatten()) #lo ritrasforma ad un array ad una dimensione = (arr.reshape[-1])

###ITERARE ARRAY
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:   #un for per ogni dimensione
    for y in x:
        print(y)

#nditer
#n è il numero indefinito di dimensioni
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):     #l'output deve essere una stringa 
    print(x)  #fa il flattening di base

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
for x in np.nditer(arr[:,::2]): #vogliamo tutti gli array della dimensione
    print(x)    #il :2 fa fare salti di due

#estraiamo gli indici
for idx,x in np.ndenumerate(arr):
    print(idx,x)


###UNIRE ARRAY (min 1h19)
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

#stack,hstack,vstack,dstack
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arrConc=np.concatenate((arr1,arr2),axis=0)  #l'asse zero è l'unico disponibile
arrStack=np.stack((arr1,arr2),axis=0)
arrStack=np.stack((arr1,arr2),axis=1)   #li sacca in base all'asse 1
print(arrConc)
print(arrStack)

arrStack=np.hstack((arr1,arr2)) #=concatenate
arrStack=np.vstack((arr1,arr2)) #=axis 0
arrStack=np.dstack((arr1,arr2)) #=axis 1
print(arrStack)



import numpy as np

###DIVIDERE ARRAY
arr=np.array([1,2,3,4,5,6])
arr2= np.array_split(arr,4)     #np.split funziona solo conun divisiore della lunghezza dell'array
print(arr2)

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
arr2= np.array_split(arr,4)  #np.split funziona solo conun divisiore della lunghezza dell'array
arr2= np.array_split(arr,3,axis=1) 
print(arr2)

arr2= np.hsplit(arr,3)
arr2= np.vsplit(arr,3)
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
arr2= np.dsplit(arr,3)
print(arr2)


###CERCARE, ORDINARE, FILTRARE ARRAY
arr=np.array([1,2,3,4,5,4,4])
arrIndici=np.where(arr==4)

arr=np.array([1,2,3,4,5,6,7,8])
arrIndici=np.where(arr%2==0)    #modulo 0
print(arrIndici)

arr=np.array([[3,7,2],[4,9,1]])
arr=np.array(["marco","anna","lucia","francesco"])
arrOrdinato=np.sort(arr)
print(arrOrdinato)

#esempio statico
arr=np.array([1,2,3,4])
filtroPari=[False,True,False,True]
arrayFiltrato=arr[filtroPari]
print(arrayFiltrato)

arr=np.array([1,2,3,4])
filtroPari=[False,True,False,True]   #filtro statico
arrayFiltrato=arr[filtroPari]
print(arrayFiltrato)

#esempio dinamico
arr=np.array([1,2,3,4])
filtro=[]  #filtro dinamico
for numero in arr:
    if numero%2==0:
        filtro.append(True)
    else:
        filtro.append(False)
    
arrayFiltrato=arr[filtro]
print(arrayFiltrato)

#scorciatoia
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
filtro=arr%2==0
arrayFiltrato=arr[filtro]
print(arrayFiltrato)



###RANDOM
import numpy as np
from numpy import random, size

arr=random.randint(100,size=(3,3,2))  #100 numero intero massimo
print(arr)  #creo array casuali

arr=random.rand(3,5,2) #ritorna numero compesi tra 0 e 1
print(arr)

arr=np.array([1,2,3,4,5,6])
print(random.choice(arr,size=(5,2,3))) #ogni volta ritorna numeri diversi tra quelli proposti
                                    #array di 5 dimensioni, con 2 array per uno, e 3 valori per array

#data distribution con probabilità
values=np.array([10,20,30,40,50])
probability=np.array([0.1,0.2,0.3,0.1,0.3])
arrChoice=random.choice(values,p=probability,size=(20))
print(arrChoice)    #restituisce i values in modo casuale ma in propozione alla probabilità assegnata

arr=np.array([1,2,3,4,5,6])
random.shuffle(arr) #agisce sull'array cambiandone l'ordine, infatti non viene assegnato
arr2=random.permutation(arr)    #va riassegnato 
print(arr)  
print(arr2)


###UNIVERSAL FUNCTION
#funzioni che agiscono sulla funzione np.array in modo da fare operazioni aritmetiche
arr=np.array([5,10,15,20])
def addcinque(x):
    return x+5
addcinque=np.frompyfunc(addcinque,1,1)
print(addcinque(arr))


#add, subtract, multiply, divide, power,mod/reminder, trunc, ceil, floor
arr1=np.array([10,20,30,40,50])
arr2=np.array([5,10,15,20,15])
arr=np.add(arr1,arr2)   #su sue liste, non np.array, le concatena
arr=np.subtract(arr1,arr2) 
arr=np.multiply(arr1,arr2) 
arr=np.divide(arr1,arr2) 
arr=np.power(arr1,arr2) 
arr=np.mod(arr1,arr2)   #il resto

arr=np.trunc([4.976,2.1322]) #arrotonda all'interno in difetto    #=np.fix
arr=np.around([4.976,2.1322]) #arrotonda per eccesso all'interp     #=np.ceil
print(arr)
