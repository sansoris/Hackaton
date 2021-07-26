from ClasePersona import Egresos


class Ingresos:
    def __init__(self):
      
        self.consolidadoingreso = []

        self.nomingreso = input("Por favor ingrese el nombre del ingreso: ")
        self.nomfrecuenciaingreso = input("Por favor ingrese frecuencia\n 1 mensual\n 2 quincenal\n 4 semanal\n y 30 diario\n ")
        self.nomvaloringreso = input("Por favor ingrese el valor del ingreso: ")
        nuevoingreso = (self.nomingreso, self.nomfrecuenciaingreso, self.nomvaloringreso)
        self.consolidadoingreso.append(nuevoingreso) 
        print("Nuevo ingreso incluido")


class Endeudamiento:
    def __init__(self):
      
        self.totaldeudas = []
        # self.nomdeuda = map de lista de egresos Egresos.consolidadogasto con la suma de todos los gastos multiplicados por frecuencia
        self.nomdeuda = map(lambda x: x[2]*x[3], (Egresos.consolidadogasto[i][1:])) for i in range(len(Egresos.consolidadogasto))
        self.totaldeudas.append(self.nomdeuda)


class Estudio: 
    def __init__(self):
        endeuda = 0
        endeuda = (Ingresos.consolidadoingreso / Endeudamiento.totaldeudas)*100
        if endeuda< 40:
            print( endeuda + "Tiene capacidad de endeudamiento\n")
            
        elif endeuda> 40:
            print("NO Tiene capacidad de endeudamiento\n")
        else: print("Por favor revisar los valores\n")

class Fechas:
    def __init__(self):
        endeuda1 = Estudio.endeuda/40
        self.cumplido = input("Si cancela sus deudas en la fecha oportuna ingrese 1, de lo contrario coloque 0: ")

        return (self.cumplido + self.valor + endeuda1)