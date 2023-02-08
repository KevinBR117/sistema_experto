# reglas = ['5',
#           [
#               {
#                   "tiene cabello": None
#               }
#           ],
#           "El animal es un mamifero",
#           "sin valor",
#           0
#           ]

# reglas[1].append({"produce leche": None})
# reglas[1].append({"es domestico": None})
# print(reglas)

# print(reglas[1][0])
# print(reglas[1].keys())

reglas = []
with open('./sistema_experto/dominio.txt') as archivo:
    # crear regla
    regla = []
    dicccionario = {}
    for linea in archivo:
        # print(linea)
        # identificar si es regla
        if any(map(str.isdigit, linea)):
            numero_regla = linea.replace('\n', '').replace(':', '').split(' ')
            if(numero_regla[0].isdigit()):
                regla.append(numero_regla[0])
        # condicion
        elif(linea.startswith('-')):
            dicccionario.setdefault(linea.replace(
                '\n', '').replace('-', ''), None)
        elif(linea == 'entonces:\n'):
            regla.append(dicccionario)
            dicccionario = {}
            # continue
        elif(linea.startswith('*')):
            regla.append(linea.replace('\n', '').replace('*', ''))
            regla.append("sin valor")
            regla.append(0)
            reglas.append(regla)
            regla = []


def mostrar_reglas():
    for regla in reglas:
        print(f'Regla: {regla}')
        # print('el animal tiene cabello' in regla[1])


def leer_premisas():
    premisas = input('¿Que caracteristicas tiene el amimal? ')
    return premisas.split(', ')


def buscar_reglasAptas(premisas):
    print(f'premisas iniciales: {premisas}')
    for regla in reglas:
        dict = regla[1].keys()
        llaves_verdaderas = []
        for premisa in premisas:
            for key in dict:
                if (premisa in key):
                    # actualizar diccionario
                    print('key ', key)
                    llaves_verdaderas.append(key)
                    # regla[1].update(key=True)
                    # print(regla[1].keys())
        for llave in llaves_verdaderas:
            regla[1].update({llave: True})


def main():
    mostrar_reglas()
    buscar_reglasAptas(leer_premisas())
    mostrar_reglas()


if __name__ == '__main__':
    main()
