a = int (input('Ingrese un valor'))
b = int (input('Ingrese un valor'))
c = int (input('Ingrese un valor'))

suma = a+b+c

promedio = suma/3

print('El promedio es', promedio)

if (promedio <= 3):
    print('Repbrobado ')
if (promedio >= 4 and promedio <= 6):
    print('Debe rendir final')
else:
    print('Eximido')