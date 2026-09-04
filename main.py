import json

from funcion_menu import interfaz
from funcion_visualizar import visualizar_horario
from funcion_registro import registrar_materias
from funcion_eliminar import eliminar_registro
from funcion_modificar import modificar_registro
from funcion_reporte import generar_reporte

start = True
while start == True:

    try:
        with open('registro.json', mode='r', encoding='utf-8') as registro:
            registro_materias = json.load(registro)
    except (FileNotFoundError, json.JSONDecodeError):
        registro_materias = []

    interfaz()

    try: 
        select = int(input('\n Seleccione una opcion: '))
    except ValueError:
        print('Error. El tipo de dato no es valido.')
        continue

    match select:
        case 1:
            registrar_materias(registro_materias)
        case 2:
            visualizar_horario(registro_materias)
        case 3:
            modificar_registro(registro_materias)
        case 4:
            eliminar_registro(registro_materias)
        case 5:
            generar_reporte(registro_materias)
        case 6:
            print('Saliendo del programa...')
            start = False
        case _:
            print('La opcion no existe.')
