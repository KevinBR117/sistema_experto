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

reglas = []
with open('./dominio.txt') as archivo:
    # crear regla
    regla = []
    for linea in archivo:
        # print(linea)
        # identificar si es regla
        if any(map(str.isdigit, linea)):
            numero_regla = linea.replace('\n', '').replace(':', '').split(' ')
            if(numero_regla[0].isdigit()):
                regla.append(numero_regla[0])
        # condicion o diagnostico
        elif(linea.startswith('-')):
            # si no existe la casilla de premisas
            if(len(regla) < 2):
                regla.append([{linea.replace(
                    '\n', '').replace('-', ''): None}])
                # print('regla actual', regla)
            else:
                regla[1].append({linea.replace(
                    '\n', '').replace('-', ''): None})
        elif(linea == 'entonces:\n'):
            continue
        elif(linea.startswith('*')):
            regla.append(linea.replace('\n', '').replace('*', ''))
            regla.append("sin valor")
            regla.append(0)
            reglas.append(regla)
            regla = []





for regla in reglas:
    print(f'Regla: {regla}')
