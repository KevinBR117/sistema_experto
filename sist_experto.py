from dominio import reglas,Regla
import sys

def mostrar_reglas():
    for regla in reglas:
        print(f'{regla.get_regla()}\n')


def leer_premisas():
    premisas = input('¿Que caracteristicas tiene el amimal? ')
    return premisas.split(', ')


def buscar_reglasAptas(premisas):
    print(f'premisas iniciales: {premisas} \n')
    for regla in reglas:
        dict = regla.condiciones.keys()
        llaves_verdaderas = []
        for premisa in premisas:
            for key in dict:
                if (premisa in key):
                    # actualizar diccionario
                    print('key verdadera', key)
                    llaves_verdaderas.append(key)
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
            
                if (r.diagnostico in diagnostico):
                    r.valor = 'verdadero'
                    for key in r.condiciones.keys():
                        r.condiciones.update({key: True})
                    r.actualiza_porcentaje()

    print('Reglas actualizadas: \n')
    mostrar_reglas()


def ordenar_reglas():
    global reglas
    reglas = sorted(reglas)
    print('Reglas ordenadas: \n')
    mostrar_reglas()


def seleccionar_regla():
    regla_seleccionada = reglas[0]
    for regla in reglas:
        if (regla.valor == 'sin valor'):
            regla_seleccionada = regla

    for regla in reglas:
        if(regla.valor == 'sin valor' and regla.porcentaje > regla_seleccionada.porcentaje):
            regla_seleccionada = regla

    print('Regla seleccionada: ', regla_seleccionada.get_regla())
    return regla_seleccionada


def generar_preguntas(regla_seleccionada):
    global encontrado
    print('generar preguntas')
    r_general = object()

    for condicion in regla_seleccionada.condiciones:
        if (regla_seleccionada.condiciones[condicion] == None):
            r_general = regla_general(regla_seleccionada)
            # sys.exit('termina ejecucion de manera forzada')

            if(r_general != False):
                print('regla general: ',r_general.get_regla())
                # print('if')
                break

            else:
                respuesta = (input(f'¿{condicion}? ')).lower()

                if (respuesta == 'si'):
                    regla_seleccionada.condiciones.update({condicion: True})
                    regla_seleccionada.actualiza_porcentaje()

                elif (respuesta == 'no'):
                    regla_seleccionada.condiciones.update({condicion: False})
                    regla_seleccionada.actualiza_porcentaje()
                    regla_seleccionada.descarta_regla()
                    break
    
    # print('salimos del ciclo for')
    if (isinstance(r_general, Regla)):
        # sys.exit('termina la ejecucion de manera forzada')
        generar_preguntas(r_general)

    if (regla_seleccionada.valor == 'verdadero'):
        encontrado = regla_particular(regla_seleccionada)
        if(encontrado == True):
            print('Fin de preguntas\n')
            print(regla_seleccionada.diagnostico, '\n')
            print(regla_seleccionada.get_regla(), '\n')


def regla_general(regla_seleccionada):
    for regla in reglas:
        for key in regla_seleccionada.condiciones.keys():
            if(key in regla.diagnostico):
                if(regla.porcentaje < 1.0):
                    return regla
    return False


def regla_particular(regla_seleccionada):
    for regla in reglas:
        for key in regla.condiciones.keys():
            if (key in regla_seleccionada.diagnostico):
                return False
    return True


encontrado = False


def main():
    mostrar_reglas()
    buscar_reglasAptas(leer_premisas())
    while(encontrado == False):
        buscar_reglasSeriadas()
        ordenar_reglas()
        generar_preguntas(seleccionar_regla())
    print('La ejecución ha terminado')


if __name__ == '__main__':
    main()
