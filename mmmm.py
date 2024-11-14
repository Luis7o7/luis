import random

class EcosistemaGrafo:
    def __init__(self):
        self.regiones = {
            'region_1': {'alces': 50, 'lobos': 10, 'pasto': 300},
            'region_2': {'alces': 30, 'lobos': 5, 'pasto': 200},
            'region_3': {'alces': 40, 'lobos': 8, 'pasto': 250},
            'region_4': {'alces': 20, 'lobos': 7, 'pasto': 100}
        }
        
        self.grafo = {
            'region_1': ['region_2', 'region_3'],
            'region_2': ['region_1', 'region_4'],
            'region_3': ['region_1', 'region_4'],
            'region_4': ['region_2', 'region_3']
        }

        # Tabla Q para aprender qué regiones son mejores para los lobos
        self.q_table = {region: {vesino: 0 for vesino in vesinos} for region, vesinos in self.grafo.items()}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 0.2  # Tasa de exploración

    def crecer_pasto(self, region):
        self.regiones[region]['pasto'] += random.randint(10, 30)

    def alimentar_alces(self, region):
        alces = self.regiones[region]['alces']
        pasto = self.regiones[region]['pasto']
        
        if pasto >= alces:
            self.regiones[region]['pasto'] -= alces
            if random.random() < 0.3:
                self.regiones[region]['alces'] += random.randint(1, 10)
        else:
            self.regiones[region]['alces'] -= random.randint(1, 2)

        if random.random() < 0.1:
            self.regiones[region]['alces'] -= random.randint(1, 3)
        self.regiones[region]['alces'] = max(self.regiones[region]['alces'], 0)

    def alimentar_lobos(self, region):
        lobos = self.regiones[region]['lobos']
        alces = self.regiones[region]['alces']
        
        if alces >= lobos:
            self.regiones[region]['alces'] -= lobos // 2
            if random.random() < 0.2:
                self.regiones[region]['lobos'] += random.randint(1, 8)
        else:
            self.regiones[region]['lobos'] -= random.randint(1, 2)

        if random.random() < 0.15:
            self.regiones[region]['lobos'] -= random.randint(1, 5)
        self.regiones[region]['lobos'] = max(self.regiones[region]['lobos'], 0)

    def mover_lobos_adaptativo(self, region):
        if random.random() < self.exploration_rate:
            # Exploración: elegir una acción al azar
            destino = random.choice(self.grafo[region])
        else:
            # Explotación: elegir la mejor acción según la tabla Q
            destino = max(self.q_table[region], key=self.q_table[region].get)
        
        lobos_a_mover = min(3, self.regiones[region]['lobos'])
        self.regiones[region]['lobos'] -= lobos_a_mover
        self.regiones[destino]['lobos'] += lobos_a_mover

        # Calcular recompensa en función de los alces en la región de destino
        recompensa = self.regiones[destino]['alces']

        # Actualizar tabla Q
        mejor_valor_futuro = max(self.q_table[destino].values())
        self.q_table[region][destino] = (1 - self.learning_rate) * self.q_table[region][destino] + \
                                        self.learning_rate * (recompensa + self.discount_factor * mejor_valor_futuro)

    def simular_paso(self):
        for region in self.regiones:
            self.crecer_pasto(region)
            self.alimentar_alces(region)
            self.alimentar_lobos(region)

        # Movimientos inteligentes de los lobos entre regiones
        for region in self.grafo:
            self.mover_lobos_adaptativo(region)

    def simular(self, duracion):
        for t in range(1, duracion + 1):
            print(f"Tiempo: {t}")
            self.simular_paso()
            for region, datos in self.regiones.items():
                print(f"{region}: Alces: {datos['alces']}, Lobos: {datos['lobos']}, Pasto: {datos['pasto']}")
            print("-" * 30)

# Crear instancia del ecosistema con grafo y simular por 50 pasos de tiempo
ecosistema = EcosistemaGrafo()
ecosistema.simular(50)
