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
