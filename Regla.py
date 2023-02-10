class Regla():
    def __init__(self, lista_regla):
        self.regla = lista_regla[0]
        self.condiciones = lista_regla[1]
        self.diagnostico = lista_regla[2]
        self.valor = lista_regla[3]
        self.porcentaje = self.actualiza_porcentaje(self.condiciones)

    def get_regla(self):
        return (self.regla, self.condiciones, self.diagnostico, self.valor, self.actualiza_porcentaje(self.condiciones))

    def actualiza_porcentaje(self, condiciones):
        verdaderas = 0
        for key in self.condiciones.values():
            # print(key)
            if (key == True):
                verdaderas += 1

            elif(key == False):
                self.descarta_regla()

        if(verdaderas/len(self.condiciones) == 1.0):
            self.acepta_regla()
        return verdaderas/len(self.condiciones)

    def descarta_regla(self):
        self.valor = 'falso'

    def acepta_regla(self):
        self.valor = 'verdadero'
