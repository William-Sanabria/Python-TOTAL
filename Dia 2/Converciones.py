num1 = 20.5
num2 = 30.5
print(num1)
#num1 = num1 + num2

print(type(num1))
print(type(num2))

print("Ejemplo 2")

num2 = int(num1)
print(num2)
print(type(num2))


print("Ejemplo practico transformar datos")
edad = input("Dime tu edad: ")

print("Antes de int")
print(type(edad))

edad = int(edad)
print("Despues de int")
print(type(edad))

nueva_edad = 1 + edad
print(nueva_edad)