'''
El condicional parcial o simple se utiliza cuando es requerido realizar una accion si la condicion es verdadera
y continuar la ejecucion del script si la condicion es falsa
'''

#Ejemplo condicional parcial con expresion lógica simple

importe = float(input('Ingerese el importe de la compra:'))

if importe > 1000:
    print('El cliente tiene un descuento del 10%')
    importe = importe - (importe * 0.10)

print('El importe a pagar es: ', importe)

#Ejemplo condicional parcial con expresion lógica compuesta 


importe = float(input('Ingrese el importe de la compra:'))
provincia = input('Ingrese la provincia de destino')
costo_envio = float(input('Ingrese el costo de envio:'))


if importe > 1000 and provincia == 'cordoba':
    print('Envios gratuitos hacia la provincia de Córdoba')
    costo_envio = 0

print(f'El total a pagar es de ${importe + costo_envio}')

#Ejemplo condicional completo con expresion lógica simple

importe = float(input('Ingrese el importe de la compra:'))
provincia = input('Ingrese la provincia de destino')
costo_envio = float(input('Ingrese el costo de envio:'))

if provincia == 'cordoba':
    print('Envios gratuitos hacia la provincia de Córdoba')
    costo_envio = 0
else:
    print('No hay envios gratis al destino elegido')

print(f'El total a pagar es de ${importe + costo_envio}')

#Ejemplo condicional completo con expresion lógica compuesta

importe = float(input('Ingrese el importe de la compra:'))
provincia = input('Ingrese la provincia de destino')
costo_envio = float(input('Ingrese el costo de envio:'))

if importe > 1000 and provincia == 'cordoba':
    print('Envios gratuitos hacia la provincia de Córdoba a partir de compras mayores a $1000')
    costo_envio = 0
else:
    print('No hay envios gratis al destino elegido')

print(f'El total a pagar es de ${importe + costo_envio}')