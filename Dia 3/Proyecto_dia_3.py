import time
#Variables
texto_ingresado = input("Ingrese el texto a validar: ")
time.sleep(2)
texto_ingresado_minus = texto_ingresado.lower()#texto a minuscula
letra1 = input("Ingrese una letra: ")
letra1_minus = letra1.lower()#texto a minuscula
letra2 = input("Ingrese una letra diferente a la anterior: ")
letra2_minus = letra2.lower()#texto a minuscula
letra3 = input("Ingrese una letra diferente a las 2 anteriores: ")
letra3_minus = letra3.lower()#texto a minuscula
contador_letra1 = texto_ingresado_minus.count(letra1_minus)
contador_letra2 = texto_ingresado_minus.count(letra2_minus)
contador_letra3 = texto_ingresado_minus.count(letra3_minus)
contador_letras_end = contador_letra1 + contador_letra2 + contador_letra3
#Contador de palabras
separador_de_palabras = texto_ingresado_minus.split()
contador_de_palabras = len(separador_de_palabras)
#primer letra y ultima
primer_letra = texto_ingresado_minus[0]
ultima_letra = texto_ingresado_minus[-1]
#python
validar_python = "python" in texto_ingresado_minus

#Desarrollo
#Solicitud de texto a usuario
#1
time.sleep(5)
print("PUNTO 1")
print("Veremos el texto ingresado: \n" )
print(texto_ingresado)
time.sleep(2)
print(letra1 + " tiene una cantidad de:")
print(contador_letra1)
time.sleep(2)
print(letra2 + " tiene una cantidad de:")
print(contador_letra2)
time.sleep(2)
print(letra3 + " tiene una cantidad de:")
print(contador_letra3)
time.sleep(2)
#2
print("PUNTO 2")
time.sleep(2)
print("La cantidad de palabras es la siguiente:")
print(contador_letras_end)
time.sleep(2)
#3
print("PUNTO 3")
time.sleep(2)
print("La primer letra del texto es:" + primer_letra)
print("La ultima letra del texto es:" + ultima_letra)
#4
print("PUNTO 4")
print("Asi se veria tu texto al invertirlo")
time.sleep(2)
print(texto_ingresado_minus[::-1])
print(''.join(texto_ingresado_minus))

#5
print("PUNTO 5")
print('Acontinuacion validaremos si la palabra "Python" se encuentra en el texto')
print(validar_python)