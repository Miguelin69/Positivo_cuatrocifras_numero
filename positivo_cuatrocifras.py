#Primero, pedimos el numero.
n = int(input("Ingrese numero: "))

if ( n > 999 and n < 10000) or ( n < -999 and n > -10000):
    print(f"El numero {n} es de cuatro digitos")
else: 
    print(f"El numero {n} no es de cuatro digitos")

if ( n > 0):
    print(f"El numero {n} es positivo")
else:
    print(f"El numero {n} no es positivo")