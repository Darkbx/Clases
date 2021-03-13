print("Definir clase que almacene un codigo de clinte, cedula, nombre, direccion y fecha de nacimiento")
class persona:        #clase
    def __init__(self):
        self.edad = 25
        self.cedula = 128-1726348-7
        self.direccion = "capotillo 3"
        self.tarjeta = 4312310271286179
        self.codigo_cliente = 1955
        self.fecha_nacimiento = "11/7/1996"
        self.suspendidos = ["Mamerto", "Pirulo", "Eugenio"]
Aurelio = persona()
print("Su nombre es Aurelio")
print("Codigo",Aurelio.codigo_cliente)
print("Edad",Aurelio.edad)
print("Su tarjeta es ",Aurelio.tarjeta)
print("Direccion",Aurelio.direccion)
print("Su fecha de nacimiento es",Aurelio.fecha_nacimiento)
print("Los clientes suspendidos son")
print(Aurelio.suspendidos)