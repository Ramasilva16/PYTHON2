n1 = int ( input("Ingrese un número"))
n2 = int ( input("Ingrese un número"))
n3 = int ( input("Ingrese un número"))

if (n1 > n2 and n1 > n3):
    print ("El mayor es",n1)
if (n2 > n1 and n2 > n3):
    print ("El mayor es",n2)
if (n3 > n2 and n3 > n1):
    print ("El mayor es",n3)