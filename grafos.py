import random

class EcosistemaGrafo:
    def __init__(self):
        # Define las regiones como nodos y sus conexiones (aristas)
        self.regiones = {
            'region_1': {'alces': 50, 'lobos': 10, 'pasto': 300},
            'region_2': {'alces': 30, 'lobos': 5, 'pasto': 200},
            'region_3': {'alces': 40, 'lobos': 8, 'pasto': 250},
            'region_4': {'alces': 20, 'lobos': 7, 'pasto': 100}
        }
        
        # Define el grafo (conexiones entre las regiones)
        self.grafo = {
            'region_1': ['region_2', 'region_3'],
            'region_2': ['region_1', 'region_4'],
            'region_3': ['region_1', 'region_4'],
            'region_4': ['region_2', 'region_3']
        }

    def crecer_pasto(self, region):
        # Cada región tiene un crecimiento de pasto aleatorio
        self.regiones[region]['pasto'] += random.randint(10, 30)

    def alimentar_alces(self, region):
        alces = self.regiones[region]['alces']
        pasto = self.regiones[region]['pasto']
        
        # Los alces comen pasto y se reproducen si hay suficiente comida
        if pasto >= alces:
            self.regiones[region]['pasto'] -= alces
            if random.random() < 0.3:  # Probabilidad de reproducción
                self.regiones[region]['alces'] += random.randint(1, 10)
        else:
            # Si no hay suficiente pasto, los alces disminuyen
            self.regiones[region]['alces'] -= random.randint(1, 2)

        # Muerte natural de algunos alces
        if random.random() < 0.1:
            self.regiones[region]['alces'] -= random.randint(1, 3)

        # Evitar valores negativos
        self.regiones[region]['alces'] = max(self.regiones[region]['alces'], 0)

    def alimentar_lobos(self, region):
        lobos = self.regiones[region]['lobos']
        alces = self.regiones[region]['alces']
        
        # Los lobos cazan alces si hay suficientes y se reproducen
        if alces >= lobos:
            self.regiones[region]['alces'] -= lobos // 2
            if random.random() < 0.2:  # Probabilidad de reproducción
                self.regiones[region]['lobos'] += random.randint(1, 8)
        else:
            # Si no hay suficientes alces, los lobos disminuyen
            self.regiones[region]['lobos'] -= random.randint(1, 2)

        # Muerte natural de algunos lobos
        if random.random() < 0.15:
            self.regiones[region]['lobos'] -= random.randint(1, 5)

        # Evitar valores negativos
        self.regiones[region]['lobos'] = max(self.regiones[region]['lobos'], 0)

    def mover_alces(self, region_origen, region_destino):
        # Mover algunos alces de una región a otra si están conectadas
        alces_a_mover = min(5, self.regiones[region_origen]['alces'])
        self.regiones[region_origen]['alces'] -= alces_a_mover
        self.regiones[region_destino]['alces'] += alces_a_mover

    def mover_lobos(self, region_origen, region_destino):
        # Mover algunos lobos de una región a otra si están conectadas
        lobos_a_mover = min(3, self.regiones[region_origen]['lobos'])
        self.regiones[region_origen]['lobos'] -= lobos_a_mover
        self.regiones[region_destino]['lobos'] += lobos_a_mover

    def simular_paso(self):
        # Simulación de un paso de tiempo para cada región
        for region in self.regiones:
            self.crecer_pasto(region)
            self.alimentar_alces(region)
            self.alimentar_lobos(region)

        # Movimiento entre regiones conectadas
        for region_origen in self.grafo:
            for region_destino in self.grafo[region_origen]:
                # Probabilidad de mover alces y lobos entre regiones
                if random.random() < 0.2:
                    self.mover_alces(region_origen, region_destino)
                if random.random() < 0.1:
                    self.mover_lobos(region_origen, region_destino)

    def simular(self, duracion):
        # Simulación del ecosistema en varios pasos de tiempo
        for t in range(1, duracion + 1):
            print(f"Tiempo: {t}")
            self.simular_paso()
            for region, datos in self.regiones.items():
                print(f"{region}: Alces: {datos['alces']}, Lobos: {datos['lobos']}, Pasto: {datos['pasto']}")
            print("-" * 30)

# Crear instancia del ecosistema con grafo y simular por 10 pasos de tiempo
ecosistema = EcosistemaGrafo()
ecosistema.simular(50)
