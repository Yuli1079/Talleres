""" """ """
 Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas
. Luego muestre la lista por consola mediante un ciclo
"""
Materias = {}

while True:
    asignatura = input("Ingresa la asignatura: ")
    calificacion = float(input("Ingresa la calificacion: "))
    
    Materias[asignatura] = calificacion
    
    Agregar_materia= input("\n si desea agregar otra materia digite:si, de lo contrario: no ")
    if Agregar_materia.lower() != "si":
        break

for asignatura, calificacion in Materias.items():
    print("\nMateria:", asignatura, "\nNota:", calificacion)













    
