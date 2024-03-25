n = int (input("Ingrese un número:"))
if n > 0:
    if (n > 0 and n < 9 ):
        print (f" El número {n} es de una cifra")
    if (n > 10):
        print (f" El número {n} es de mas de  una cifra")
else:
    print("Su número es negativo o 0")