class ViajeroFrecuente:
    __num_viajero=""
    __dni=""
    __nombre=""
    __apellido=""
    __millas_acumuladas=""
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acumuladas):
        self.num_viajero = num_viajero
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acumuladas = millas_acumuladas
    
    def cantidadTotaldeMillas(self):
        return self.millas_acumuladas
    
    def acumularMillas(self, millas_recorridas):
        self.millas_acumuladas += millas_recorridas
        return self.millas_acumuladas
    
    def canjearMillas(self, millas_a_canjear):
        if millas_a_canjear <= self.millas_acumuladas:
            self.millas_acumuladas -= millas_a_canjear
            return self.millas_acumuladas
        else:
            print("No tiene suficientes millas para realizar el canje.")
            return self.millas_acumuladas