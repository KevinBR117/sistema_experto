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

from dominio import reglas


def mostrar_reglas():
    # for regla in reglas:
    #     print(f'Regla: {regla}')
        # print('el animal tiene cabello' in regla[1])
    for regla in reglas[0:1]:
        print(f'{regla.get_regla()}\n')


def leer_premisas():
    premisas = input('¿Que caracteristicas tiene el amimal? ')
    return premisas.split(', ')


def buscar_reglasAptas(premisas):
    print(f'premisas iniciales: {premisas} \n')
    for regla in reglas:
        # dict = regla[1].keys()
        dict = regla.condiciones.keys()
        llaves_verdaderas = []
        for premisa in premisas:
            for key in dict:
                if (premisa in key):
                    # actualizar diccionario
                    print('key verdadera', key)
                    llaves_verdaderas.append(key)
                    # regla[1].update(key=True)
                    # print(regla[1].keys())
        for llave in llaves_verdaderas:
            regla.condiciones.update({llave: True})
        
        regla.actualiza_porcentaje()
            

    print('Reglas actualizadas \n')
    mostrar_reglas()
    # print(reglas[0].get_regla())


def main():
    mostrar_reglas()
    buscar_reglasAptas(leer_premisas())
    mostrar_reglas()


if __name__ == '__main__':
    main()
