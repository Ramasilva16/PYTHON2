a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("Usted ingresa los valores:", a, b, c)
if (a>b):
    print(a, 'es mayor que', b  )
if (a==b):
    print(a,'y', b, 'son iguales')
if (a>b and a>c):
    print(a, 'Es el mayor de todos')
if(b<a and b<c):
    print (b, 'Es el menor de todos')
if (a>b or a>c):
    print (a, 'Es mayor que alguno de los otros dos')
if (a<=b or a<=c):
    print (a, 'Es menor o igual que alguno de los otros dos')
if (a==b and a==c and b==c):
    print ('Los tres numeros son iguales')
if (not a==b and not a==c and not b==c):
    print('Los tres numeros son distintos')
if (a%2 == 0):
    print(a, 'Es par')
if (a%2 == 0 or b%2 == 0 or c%2 == 0):
    print('Alguno es par')
if (a%2 == 1 and b%2 == 1 and c%2 == 1):
    print ('Ninguno es par')
if (a%2 == 0 and b%2 == 0 and c%2 == 0):
    print('Todos son pares')
if (a%3 == 0):
    print(a, 'Es multiplo de 3')
if (a%3 == 0 and a%5 == 0):
    print(a, 'Es multiplo de 3 y 5')
if (a%3== 0 and a%2 == 0):
    print (a, 'Es multiplo de 3 y par')
if ( a-b > 0):
    print(a, 'Es un numero Positivo')
if ((a-b)%2 == 0 and a-b > 0 ):
    print(a-b, 'Es un numero par positivo')
