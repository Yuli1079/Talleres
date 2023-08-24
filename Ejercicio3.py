Moneda = {

    "Dolar" : "3400",
    "Euro" : "4500",
    "Yen" : "340"
}

conversiones = {
    'Euro': '€',
    'Dolar': '$',
    'Yen': '¥'}



divisa= input ("Ingrese la divisa: ")
Valor= float(input("Ingrese el valor a convertir: "))

if divisa in Moneda:
    precioaConvetido = Valor/float(Moneda[divisa])
    print(f"El valor en {divisa} es de: {precioaConvetido}{conversiones[divisa]}")
else:
    print("Divisa no encontrada en el diccionario.")


    
 