class Cliente:
    
    def __init__(self):
        #interes 1 de acuerdo con estudio, interes 0 no desea estudio
        #historia 1 cuenta con calificación, historia 0 no cuenta con calificación
        self.Edad = int(input('Ingrese su edad '))
        self.Interesestudio = int(input('Ingrese 1 si desea el estudio, de lo contrario ingrese 0:  ')) # conocer o aplicar credito
        self.Histocredito = int(input('Ingrese 1 si cuenta con calificación, de lo contrario ingrese 0:  '))
        

    def ingreso (self):
        if self.Interesestudio == 0:
            Cliente.egresos # aplicar cliente.estudio de paso 2
        else:
            print("puedes recorrer la plataforma")  # Conocer

    
    def calificacioninicial (self):
        if self.Histocredito == 1:
            self.Calestudio = int(input("Por favor ingrese su calificación numérica: "))
            #Cliente.analisis interpretación de resultados paso 4
            if self.Calestudio>= 700:
                print("Manejo correcto\n")
            elif (self.Calestudio>=400 and self.Calestudio <=699):
                print("Manejo Aceptable\n")
            elif self.Calestudio<400:
                print("Manejo Crítico\n")       
        elif Cliente.egresos: 
             pass # aplicar cliente.estudio de paso 2
        else: 
            print("Ingrese una calificación válida")  

class Egresos():
    def __init__(self):
      
        self.consolidadogasto = []
        self.nomgasto = input("Por favor ingrese el nombre del gasto: ")
        self.nomfrecuencia = input("Por favor ingrese frecuencia\n 1 mensual\n 2 quincenal\n 4 semanal\n y 30 diario\n ")
        self.nomvalor = input("Por favor ingrese el valor del gasto: ")
        nuevogasto = (self.nomgasto, self.nomfrecuencia, self.nomvalor)
        self.consolidadogasto.append(nuevogasto) 
        print("Nuevo gasto incluido")
   
        
        


# cliente1= Cliente()
# cliente1.calificacioninicial()
egreso1= Egresos()
egreso1.consolidadogasto()
