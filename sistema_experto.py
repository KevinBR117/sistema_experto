# crear json para alamcenar relgas
import json

# leer archivo json y cargar base del conocimiento
with open('./sistema_experto/dominio.json') as archivo:
    datos = json.load(archivo)
    
    print(json.dumps(datos['dominio'], indent=4))
    # print(json.dumps(datos, indent=4))
    
    #imprimir primer casilla
    # print(json.dumps(datos['dominio'][0], indent=4))

    # print(json.dumps(datos['dominio'][1]['premisas'], indent=4))
    
    # modificar datos
    # datos['dominio'][1]['premisas'][0]["foo2"] = True
    # print(datos['dominio'][1]['premisas'][0]["foo2"])
    # print(json.dumps(datos['dominio'], indent=4))

    # modificar datos
    # obtener llaves del diccionario premisas
    print(datos['dominio'][0]['premisas'].keys()) 

# escribir en el mismo json
# with open('./sistema_experto/json.json', 'w') as nuevo_archivo:
#     json.dump(datos, nuevo_archivo, indent=4)
    
# buscar premisas iniciales
# print(len(datos['dominio']))
# for i in range(len(datos['dominio'])):
#     print(i)
#     print(datos['dominio'][i]['premisas'])


# print(f'Datos de la regla 1 {datos["dominio"][1]}')

    






