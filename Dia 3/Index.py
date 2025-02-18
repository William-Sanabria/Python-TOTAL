#Saber letra por numero de ubicacion
mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
print(resultado)
#buscar letra
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")
print(resultado)
#buscar con indice
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("e",1, 6)
print(resultado)

#buscar con indice derecha a izquierda
mi_texto = "Esta es una prueba"
resultado = mi_texto.rindex("a")
print(resultado)

#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))