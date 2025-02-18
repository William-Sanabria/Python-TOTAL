#Trabajadores reciben comisiones del 13% sobre
#Jefe quiere saber nombre y cuanto gana con las comiciones cada trabajador
#1 nombre y apellido
#2 ingreso
#3 calcular el 13%
#4 imprimir la informacion en pantalla
print("Solucion dada por William Sanabria 😎")
nombre = input("Dime tu primer nombre: ")
apellido = input("Dime tu apellido: ")
dinero_ventas = input("Cual fue el valor de tus ventas: ")
porcentaje_correspondiente = int(dinero_ventas)*13/100
redondeo = round(porcentaje_correspondiente,2)

print(f"El trabajador {nombre} {apellido} vendio un total de ${dinero_ventas} la comision que le corresponde es ${redondeo}")


#buscar con indice
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("e",1, 6)
print(resultado)