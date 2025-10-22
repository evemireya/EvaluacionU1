import random

numero_secreto = random.randint(1,50)
print(numero_secreto)
intento = 0
adivinado = 0

#Ciclo repetitivo
while adivinado != numero_secreto:
    #Intentos (incrementos y decrementos)
    intento += 1
    print(f"Este es tu intento {intento}, adivina el numero entre 1 y 50")
    adivinado = int(input("Ingrese el numero"))
    if intento == 5:
        print(f"""Kaboooom. numero de intentos excedidos
               Ha perdido""")
        break 
    
    print("Lo he logrado")