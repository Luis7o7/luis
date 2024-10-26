class Especie:
    def __init__(self, nombre, poblacion, tasa_crecimiento):
        self.nombre = nombre
        self.poblacion = poblacion
        self.tasa_crecimiento = tasa_crecimiento
        self.depredadores = []
        self.presas = []
    
    def agregar_depredador(self, especie):
        self.depredadores.append(especie)
    
    def agregar_presa(self, especie):
        self.presas.append(especie)
    
    def actualizar_poblacion(self):
        # Calcula la tasa de cambio basada en depredadores y presas
        for depredador in self.depredadores:
            self.poblacion -= int(depredador.poblacion * 0.1)
        for presa in self.presas:
            self.poblacion += int(presa.poblacion * 0.05)
        self.poblacion = max(self.poblacion, 0)  # Evitar poblaciones negativas

class Ecosistema:
    def __init__(self):
        self.especies = []
    
    def agregar_especie(self, especie):
        self.especies.append(especie)
    
    def simular(self, tiempo):
        for _ in range(tiempo):
            print(f"\nEstado del ecosistema en el tiempo {_}:")
            for especie in self.especies:
                especie.actualizar_poblacion()
                print(f"Especie: {especie.nombre}, Población: {especie.poblacion}")

# Ejemplo de uso
especie1 = Especie("Conejo", 100, 1.1)
especie2 = Especie("Lobo", 10, 1.05)

especie1.agregar_depredador(especie2)
especie2.agregar_presa(especie1)

ecosistema = Ecosistema()
ecosistema.agregar_especie(especie1)
ecosistema.agregar_especie(especie2)

ecosistema.simular(10)
