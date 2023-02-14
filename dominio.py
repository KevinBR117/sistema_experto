from Regla import Regla

reglas = []
with open('./dominio.txt') as archivo:
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
        # identificar si es condicion
        elif(linea.startswith('-')):
            dicccionario.setdefault(linea.replace(
                '\n', '').replace('-', ''), None)
        elif(linea == 'entonces:\n'):
            regla.append(dicccionario)
            dicccionario = {}
            # continue
        # identificar si es diagnostico
        elif(linea.startswith('*')):
            regla.append(linea.replace('\n', '').replace('*', ''))
            regla.append("sin valor")
            # objeto
            reglas.append(Regla(regla))
            regla = []
