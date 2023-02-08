import sys
import os
# se asume que todas las funciones propias de python tienen un orden de crecimiento O(1) 
# O(1)
def recibirArchivo():
    archivo = input("Ingrese la direccion del archivo: ")
    procesarEntrada(archivo)

# O(1)
def procesarEntrada(archivo):
    # se abre el archivo para leerlo, una vez que lo lee lo cierra
    archivo_entrada = open(archivo, "r") # se abre el archivo y se guarda la informacion que contiene en una variable
    NK = archivo_entrada.readline().split() # separa la primera linea del archivo en una lista de strings
    NK = list(map(int, NK)) # se convierte la lista de strings en una lista de ints
    
    trabajadores = archivo_entrada.read().splitlines() # separa el resto de lineas del archivo en una lista de strings
    trabajadores = list(map(int, trabajadores)) # se convierte la lista de string en una lista de ints
    
    archivo_entrada.close() # se cierra el archivo
    
    verificarEntrada(NK, trabajadores)

# O(1)
def verificarEntrada(NK,trabajadores):
    if (NK[0] == len(trabajadores)) and (NK[1] > 0) and (len(trabajadores) > 0):
        creacionGrupos(NK,trabajadores)
    else:
        sys.exit("EL NUMERO DE TRABAJADORES NO COINCIDEN O NO HAY TRABAJADORES PARA FORMAR GRUPOS, POR FAVOR VERIFIQUE LA INFORMACION SUMINISTRADA")

# O(1)
def mejorTrabajador(grupo): # Devuelve el índice del mejor trabajador
    mejor = max(grupo)
    index = grupo.index(mejor)
    return index

# O(techo(N/K))
def creacionGrupos(NK,trabajadores):
    grupos = []
    solucion = []
    # O(techo(N/K)-> maximo de grupos que se pueden formar )
    for i in range(0, NK[0], NK[1]): # separa el arreglo "trabajadores" en suplistas de maximo "K" elementos
        grupos.append(trabajadores[i:i+NK[1]])
    
    for i in range(len(grupos) -2, -1,-1): #O(techo(N/K))
        if grupos[i][mejorTrabajador(grupos[i])] < grupos[i+1][mejorTrabajador(grupos[i+1])]: # se compara que el elemento mayor de un grupo sea menor a el elemento mayor del siguiente grupo
            if len(grupos[i+1]) < NK[1]: # se verifica que el siguiente grupo puede tener mas elementos en su grupo
                j = NK[1] - len(grupos[i+1]) # maximo de elementos que se pueden añadir
                # en el peor caso se ejecuta K-1 veces, es decir, se deja solo un elemento en el grupo
                while j > 0: # añade los elementos posibles al siguiente grupo y a la vez los borra del grupo en el que estaba
                    grupos[i+1].insert(0, grupos[i].pop()) # añade los elemento que puedan entrar al grupo
                    j -= 1
    
    i = 0
    inicio = 0
    # O(techo(N/K))
    while i < len(grupos): # llena el arreglo solucion con las tuplas que indica el trabajador con el que inicia y termina cada grupo
        solucion.append([inicio + 1 , inicio + len(grupos[i])])
        inicio += len(grupos[i])
        i +=1
    procesarSalida(solucion)

# O(techo(N/K))
def procesarSalida(grupos):
    #se crea un archivo el cual se puede escribir
    with open("salida-fada.txt", "w") as archivo_salida:
        # O(techo(N/K))
        for e in grupos: #Recorre cada elemento del arreglo
            archivo_salida.write(str(e[0]) + " " + str(e[1]) + "\n")  #ingresa en el archivo salida cada parte del arreglo con un salto de linea con su respectivo formato
    
    os.system("salida-fada.txt")
            
while True:
    recibirArchivo()
