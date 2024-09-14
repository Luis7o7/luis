class Zoo:
    def __init__(self, aves:str,reptiles:str,felinos:str,edad:int,tipo:str):
        self.aves = aves
        self.reptiles = reptiles
        self.felinos = felinos
        self.edad = edad
        self.tipo = tipo
    
    def __str__(self):
        return f'el zoologico tien en  {self.tipo} como {self.aves} , {self.tipo} como {self.reptiles}  y {self.tipo} como {self.felinos} , con una edad de con {self.edad} años'
    
class Animal(Zoo) :
    def __init__(self, aves:str,reptiles:str,felinos:str,edad:int,tipo:str):
        super().__init__(aves,reptiles,felinos,edad,tipo)

especie=Animal('aguila','pantera','vaca','19')

print(especie)
print(type(especie))




    