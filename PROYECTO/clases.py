
class Vehiculo:
    def __init__( self, marca:str,conbustible:str,tipo:str, nivel_combustible:float):## este es el constructor __init__
        self.marca=marca 
        self.conbustible=conbustible
        self.tipo=tipo
        self.nivel_combustible=nivel_combustible
        self.en_marcha=False

    def encender(self):
        if self.nivel_combustible<0.1:
            print('Advertencia: nivel de conbustible muy bajo. necesita ir a la gasolineria')
        else:
         print(f'El vehiculo {self.tipo}{self.marca} se ha encendido correctamente.')
         self.en_marcha=True
    def marcha(self):
        if self.en_marcha:
            consumo_combustible=0.1
            self.nivel_combustible = max(0,self.nivel_combustible - consumo_combustible)
            print(f'El vehiculo {self.tipo}{self.marca} ya esta en marcha. Nivel de combustible {self.nivel_combustible:.2f}')
            if self.nivel_combustible<= 0:
               print('el vehiculo se ha detenido. Nivel de conbustible 0')
               self.en_marcha=False
            elif self.nivel_combustible <0.1:
                print('Advertencia: nivel de conbustible muy bajo. necesita ir a la gasolineria')
        else:
            ('el vehiculo no esta encendido')        
    def apagar(self):
        if self.en_marcha:
            print(f'El vehiculo {self.tipo}{self.marca} se ha apagado correctamente')
            self.en_marcha=False
    def arrancar(self):
        pass
    def __str__(self):
        return f"el vehiculo es una {self.tipo} {self.marca} que utiliza {self.conbustible}"

carro=Vehiculo('toyota','corriente','carro', 0.5 )    
print(carro)
print(type(carro))
 
 
class Moto (Vehiculo):
     def __init__(self,marca:str,combustible:str, nivel_combustible:float):
         super().__init__(marca,combustible,'Moto',nivel_combustible)
class Carro (Vehiculo):
     def __init__ (self,marca:str,combustible:str,nivel_combustible:float):
         super().__init__(marca,combustible,'Carro', nivel_combustible )
 
motocicleta=Moto('honda','corriente',0.3)
mi_carro=Carro('masda','extra',0.6)

print(motocicleta)
print(type(motocicleta))

print(mi_carro)

carro.encender()
carro.marcha()
carro.marcha()
carro.marcha()

motocicleta.encender()  # se puede llamar a los metodos de la clase
motocicleta.marcha() 
motocicleta.marcha() 
motocicleta.marcha() 
mi_carro.encender()
mi_carro.marcha()
mi_carro.marcha()
mi_carro.marcha()
