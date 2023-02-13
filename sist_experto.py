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
    for regla in reglas:
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


def buscar_reglasSeriadas():
    for regla in reglas:
        if(regla.valor == 'verdadero'):
            diagnostico = regla.diagnostico
            # buscar reglas seriadas con otras reglas
            for r in reglas:
                for key in r.condiciones.keys():
                    if (key in diagnostico):
                        r.condiciones.update({key: True})
                r.actualiza_porcentaje()

    print('Reglas actualizadas: \n')
    mostrar_reglas()
    # print(reglas[0].get_regla())


def ordenar_reglas():
    global reglas
    reglas = sorted(reglas)
    print('Reglas ordenadas: \n')
    mostrar_reglas()


def seleccionar_regla():
    # print('seleccionar regla')
    regla_seleccionada = reglas[0]
    for regla in reglas:
        if (regla.valor == 'sin valor'):
            regla_seleccionada = regla
    
    for regla in reglas:
        if(regla.valor == 'sin valor' and regla.porcentaje > regla_seleccionada.porcentaje):
            regla_seleccionada = regla
    
    print('regla seleccionada: ', regla_seleccionada.get_regla())
    return regla_seleccionada

def generar_preguntas(regla_seleccionada):
    # print(regla_seleccionada.condiciones)
    print(regla_seleccionada.condiciones)
    for condicion in regla_seleccionada.condiciones:
        if (regla_seleccionada.condiciones[condicion] == None):
            respuesta = (input(f'¿{condicion}? ')).lower()
            # print('respuesta', respuesta)
            if (respuesta == 'si'):
                # print(type(respuesta))
                regla_seleccionada.condiciones.update({condicion: True})
                regla_seleccionada.actualiza_porcentaje()

            elif (respuesta == 'no'):
                regla_seleccionada.condiciones.update({condicion: False})
                regla_seleccionada.actualiza_porcentaje()
                regla_seleccionada.descarta_regla()
                break
                
    if (regla_seleccionada.valor == 'verdadero'):
        print('Fin de preguntas')
        print(regla_seleccionada.diagnostico)
        print(regla_seleccionada.get_regla())
        
        # if(regla_seleccionada.valor != 'falso'):
        #     if(regla_seleccionada == False):
        #         pass
            
        


        
    #     if (condicion == True):
    #         print('none')
    #     # print('condicion: ', condicion)
        


def main():
    
    mostrar_reglas()
    
    
    buscar_reglasAptas(leer_premisas())
    buscar_reglasSeriadas()
    ordenar_reglas()
    generar_preguntas(seleccionar_regla())

    # print(seleccionar_regla())



if __name__ == '__main__':
    main()
