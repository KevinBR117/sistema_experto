class Regla():
    def __init__(self, lista_regla):
        self.regla = lista_regla[0]
        self.condiciones = lista_regla[1]
        self.diagnostico = lista_regla[2]
        self.valor = lista_regla[3]
        self.porcentaje = self.actualiza_porcentaje()

    def get_regla(self):
        return (self.regla, self.condiciones, self.diagnostico, self.valor, self.porcentaje)

    def get_condiciones_verdaderas(self):
        verdaderas = 0
        for value in self.condiciones.values():
            if (value == True):
                verdaderas += 1

        return verdaderas

    def __gt__(self, regla):
        return (self.porcentaje < regla.porcentaje)
        # return (self.porcentaje < regla.porcentaje), (self.get_condiciones_verdaderas() < regla.get_condiciones_verdaderas())

    def actualiza_porcentaje(self):
        verdaderas = 0
        for value in self.condiciones.values():
            # print(value)
            if (value == True):
                verdaderas += 1

            elif(value == False):
                self.descarta_regla()

        if(verdaderas/len(self.condiciones) == 1.0):
            self.acepta_regla()
        self.porcentaje = verdaderas/len(self.condiciones)

    def descarta_regla(self):
        self.valor = 'falso'

    def acepta_regla(self):
        self.valor = 'verdadero'
