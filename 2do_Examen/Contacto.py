print("<--------------------------->")
print("<---------CONTACTOS--------->")
print("<--------------------------->")

#BUCLE_WHILE-PARA_EL_MENU_DE_CONTACTOS

opcion = 0
while opcion != 5:
    """OPCIONES A ELEGIR"""
    print("1.Crear contacto en la agenda")
    print("2.Listado de contactos")
    print("3.Buscar ingresando el nombre de la persona")
    print("4.Modificacionde su telefono, mail o direccion")
    print("5.Finalizar programa!")
    """SELECCION DE OPCION"""
    opcion = int(input("¿Que desea?\n"))

    if opcion == 1:
        
        print("Escriba sus datos a continuacion")
        a = int(input(""))