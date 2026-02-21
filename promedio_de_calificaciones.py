notas = []
cantidad = int(input("¿cuantas calificaciones desea ingresar? "))
for i in range(cantidad):
    nota = float(input(f"ingrese la calificación #{i + 1}: "))
    notas.append(nota)
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print("\ncalificaciones ingresadas:", notas)
print("el promedio de las calificaciones es:", promedio)