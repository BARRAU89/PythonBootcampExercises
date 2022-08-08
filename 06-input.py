#Sirve para capturar datos ingresados por el usuario, a traves de la plataforma de Python. 
nombre = input('Como te llamas?: ')
print ('Hola ' + nombre)

edad = input('Cual es tu edad?: ')
print (type(edad))
print (f'{nombre} tiene {edad} años de edad')


#Programa que pide dos numeros al usuario y los suma
numero1 = int(input('Introduce el primer numero: '))
numero2 = int(input('Introduce el segundo numero: '))
numero3 = numero1 + numero2

print (f'El resultado de la suma es: {numero3}')
