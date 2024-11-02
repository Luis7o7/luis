import random

class Ecosistema:
    def __init__(self, cant_alces, cant_lobos, cant_pasto, tiempo_crecer_pasto):
        self.alces = cant_alces
        self.lobos = cant_lobos
        self.pasto = cant_pasto
        self.tiempo_crecer_pasto = tiempo_crecer_pasto
        self.tiempo = 0

    def crecer_pasto(self):
        # El pasto crece un poco cada cierto tiempo
        if self.tiempo % self.tiempo_crecer_pasto == 0:
            self.pasto += random.randint(10, 50)

    def alimentar_alces(self):
        # Los alces comen pasto y se reproducen ligeramente
        if self.pasto >= self.alces:
            self.pasto -= self.alces
            if random.random() < 0.3:  # Probabilidad de reproducción
                self.alces += random.randint(1, 15)
        else:
            # Si hay poco pasto, los alces disminuyen por falta de alimento
            self.alces -= random.randint(1, 2)

        # Probabilidad de muerte natural de los alces
        if random.random() < 0.1:
            self.alces -= random.randint(1, 3)
        self.alces = max(self.alces, 0)  # Evitar números negativos

    def alimentar_lobos(self):
        # Los lobos cazan alces y se reproducen ligeramente
        if self.alces >= self.lobos:
            self.alces -= self.lobos // 2  # Los lobos cazan la mitad de su número en alces
            if random.random() < 0.2:  # Probabilidad de reproducción
                self.lobos += random.randint(1, 5)
        else:
            # Si hay pocos alces, los lobos disminuyen por falta de alimento
            self.lobos -= random.randint(1, 2)

        # Probabilidad de muerte natural de los lobos
        if random.random() < 0.15:
            self.lobos -= random.randint(1, 2)
        self.lobos = max(self.lobos, 0)  # Evitar números negativos

    def actualizar_ecosistema(self):
        self.crecer_pasto()
        self.alimentar_alces()
        self.alimentar_lobos()

    def simular(self, duracion):
        for _ in range(duracion):
            self.tiempo += 1
            self.actualizar_ecosistema()
            print(f"Tiempo: {self.tiempo}")
            print(f"Alces: {self.alces}, Lobos: {self.lobos}, Pasto: {self.pasto}")
            print("-" * 30)

# Parámetros iniciales
ecosistema = Ecosistema(cant_alces=50, cant_lobos=10, cant_pasto=350, tiempo_crecer_pasto=5)

# Ejecuta la simulación por 50 pasos de tiempo
ecosistema.simular(50)
