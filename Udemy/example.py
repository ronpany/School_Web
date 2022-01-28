# Autor -> Ronny Andres Pantoja 

# Son las variables que se manejaran a lo largo del programa
pilaCar = []
tamaño = 0

# Funcion que busca si una placa se encuentra Retorna True o False
def repeatedPlate(pila,placa):
    band = 0
    for i in range(size()):
        if pila[i]==placa:
            band = 1 
    if band != 0: return True
    else: return False

# Funcion de Adicionar Coche maneja las dos variables globales antes mencionadas
def insertCar(pila, placa):
    global tamaño
    if repeatedPlate(pila,placa)==False: pila.append(placa)
    else: print("---------- LA PLACA ESTA REPETIDA -----------")
    tamaño+=1

# Funcion eliminar coche de ayuda de un arreglo auxiliar para poder eliminar manualmente un coche determiando
def deleteCar(pila,placa):
    global tamaño
    global pilaCar
    pilaAux = []
    band = -1
    for i in range(tamaño):
        if pila[i] == placa:
            band = i
    if band != -1: # Si encontro la placa
        for i in range(size()):
            if i != band:
                print(pila[i])
                pilaAux.append(pila[i])
            """ else:
                pila.pop(i) """

        pilaCar = pilaAux
        tamaño-=1        

# Funcion de vaciar la Pila o arreglo (Se ayuda de otro arreglo auxiliar)
def emptyPila(pila):
    global pilaCar
    pilaA = []
    pilaCar = pilaA

    """ global tamaño
    del pila[:]
    tamaño =0 """

# Esta funcion nos retorna el tamaño que se ha ido midifucando a travez del flujo en el algoritmo
def size():
    global tamaño
    return tamaño

# ------------------------------------- MAIN --------------------------------------------
# Arreglo que guradará los Datos. 
pila = []

# El menu de donde se trabajará
while True:
    print("-------------------------------------------------------------")
    print("             PARQUEADERO CON ARREGLOS ")
    print("-------------------------------------------------------------")
    print(" 1. Agregar Coche")
    print(" 2. Sacar Coche")
    print(" 3. Consultar Coche")
    print(" 4. Vaciar Arreglo")
    print(" 5. Indicar Coches")
    print(" 0. Salir")
    print()
    print(" Digite su Opcion -> ")
    option = int(input())
    if option == 1:
        print("Digite la Placa: ")
        insertCar(pilaCar,input()) 
    if option == 2:
        print("Digite la Placa: ")
        deleteCar(pilaCar,input())
    if option == 3:
        print("Digite la Placa: ")
        plac = input()
        if repeatedPlate(pilaCar,plac):
            print("-------------------------------------------------------------")
            print("El coche si EXISTE. ")
            print("-------------------------------------------------------------")
        else:
            print("-------------------------------------------------------------")
            print("El coche NO EXISTE. ")
            print("-------------------------------------------------------------")
    if option == 4:
        emptyPila(pilaCar)
    if option == 5:
        print()
        print("------------------ LOS COCHES SON ------------------------")
        print(pilaCar)
        print()
    if option==0:
        break
print("Hola")