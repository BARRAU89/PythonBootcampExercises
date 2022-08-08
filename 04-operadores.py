#Operadores aritméticos
print (2+2) #suma
print (4-2) #resta
print (3*7) #multiplicacion
print (15/2) #division

# print (11% 4) #modulo
print (11//4) #division de piso
print (2**3) #exponencial

# #Operadore en cadena (strings)
print ('hola' + 'mundo') #concatenacion
print ('hola'*3) #repeticion
print ('hola'+'mundo'*3)

#Operadores de comparacion
print ('Hola' == 'hola') #igual que
print ('Hola' != 'hola') #distinto que
print (3 > 11) 
print (11 >= 10)
print (10 <= 10)

#Operadores de existencia
print ('ola' in 'Hola') #existencia
print ('ola' not in 'Hola') #inexistencia

#Operadores booleanos: Verifican si se cumple una u otra condicion
print (True or False) #Or=True si cualquiera de las dos es Verdadera
print (True and False) #And=True si todas las condiciones es Verdadera. 

#Operadores de asignacion: Asigna un nuevo valor a una variable que ya habia sido previamente definida
x = 1
x += 2 # += suma al valor previamente establecido (1 + 2 = 3)
x *= 3 # *= multiplica al valor establecido (3 * 3 = 9)
x %= 4 # %= coloca como nuevo valor, el resultado del modulo (9 % 4 = 1)
print (x)

#Jerarquia de oepraciones= 1, parentesis; 2, exponentes; 3, multiplicaciones, divisiones, modulos; 4, sumas y restas. 
x = 6 * 5 + 8 / 2 ** 4