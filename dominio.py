from Regla import Regla

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

            # objeto 
            reglas.append(Regla(regla))
            regla = []

for regla in reglas:
    print(regla.get_regla())

            