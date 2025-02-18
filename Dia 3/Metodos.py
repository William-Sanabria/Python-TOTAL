#Minuscula a mayuscula
texto = "Este es el texto de william"
resultado = texto.upper()
print(resultado)
#mayuscula a Minuscula
texto = "Este es el texto de william"
resultado = texto.lower()
print(resultado)
#Separar y guardar en una lista
texto = "Este es el texto de william"
resultado = texto.split()
print(resultado)
texto = "Este es el texto de william"
resultado = texto.split("t")
print(resultado)
#unir texto .join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

#buscar caracter find
texto = "Este es el texto de william"
resultado = texto.find("x")
print(resultado)
texto = "Este es el texto de william"
resultado = texto.find("g")
print(resultado)

#reemplazar replace
texto = "Este es el texto de william"
resultado = texto.replace("william","todos")
print(resultado)
texto = "Este es el texto de william"
resultado = texto.replace("s","y")
print(resultado)
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil","fácil") + frase.replace("mala","buena"))