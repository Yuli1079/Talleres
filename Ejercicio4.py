NDatos = int(input('¿Cuántos datos desea evaluar?'))

datos = []  # Crear una lista para almacenar los datos

for _ in range(NDatos):
    valor = input("\nIngrese un dato a evaluar: ")
    datos.append(valor)  # Agregar el dato a la lista


DatosTupla = tuple(datos)

for valor in datos:
    try:
        tipo = type(eval(valor))
        print(f"El valor {valor} es de tipo {tipo}")
    except NameError:
        print(f"El valor {valor} es de tipo {type(valor)}")

    



