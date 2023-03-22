# OPERACIONES LÓGICAS
#2 valores de veradad o true(1) o false(0)#
#3 operaciones basicas conjunsion o (and) o Y
# OPERACIONES RELACIONALES O DE COMPARACIÓN
#primero operaciones se realizan por jerarquia : Primero en parentisis() luego potencia, ** luego operaciones de asterisco division , */ y por ultimo suma o resta 2+3
number = int(input("digite un numero: "))
print(number > 3)
print(number <= 3)
print(number < 3)
print(number <= 3)
print(number != 3)
# OPERACIONES LÓGICAS
#conjucion And & o Y
print(True & False)
print(number > 3 and False and True)
#Disyuncion (or,I)
print("Disyuncion:")
print(False or True)
print(number <= 3 or number >= 10)
print(not (number <= 3 | number > 10))

#negacion (not)
print('negacion:')
print(not (True))

#or exclusiva (^)
print('Or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
#**operacion de contenido o de pertenencia**#  in# pregunta si un valor esta de una variable o no.
number ="Yenny Salcedo"
print('K' in number)
print('Y' in number)
