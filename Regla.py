class Regla():
    def __init__(self, lista_regla):
        self.regla = lista_regla[0]
        self.condiciones = lista_regla[1]
        self.diagnostico = lista_regla[2]
        self.valor = lista_regla[3]
        self.porcentaje = lista_regla[4]

    def get_regla(self):
        return (self.regla, self.condiciones, self.diagnostico, self.valor, self.porcentaje)
