Personas = set()

while True:
    Nombre = str(input("Ingrese su nombre: "))
    
    Personas.add(Nombre)
    print("Su nombre es:", Nombre)

    Agregar_nombre = input("Digite 'si' si desea agregar un nuevo nombre, de lo contrario, escriba 'no': ")
    if Agregar_nombre.lower() != "si":
        break



