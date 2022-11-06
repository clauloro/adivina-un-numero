import random 
numero = random.randint(0, 100)
intento = input("introduce un numero entre 0 y 99: ")
intento = int(intento)

while numero!= intento:
    if intento < numero:
        print("El numero es pequeño")
        intento = int(input("Introduce un numero entre 0 y 99: "))
    elif intento > numero:
        print("El numero es muy grande")
        intento = int(input("Introduce otro numero entre 0 y 99: "))
    else:
      break
print("Es correcto")