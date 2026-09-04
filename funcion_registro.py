import json

def cruce(a1,b1,a2,b2): # Verificar si existe cruce entre horarios
    if a1 < b2 and a2 < b1:
        return True
    else:
        return False

def registrar_materias(materias):

    print('Para el registro de materias recuerde que el limite esta entre las 06:00 y las 18:00')

    semana = ['lunes','martes','miercoles','jueves','viernes','sabado']
    clase = input('Ingrese el nombre de la clase o actividad: ').upper()

    dia = input('Ingrese el dia de la semana: ').lower()
    while dia not in semana:
        print('Error. El dia ingresado no es valido')
        dia = input('Ingrese el dia de la semana: ').lower()

    hora_inicio = int(input('Ingrese la hora de inicio (Formato 24h - ejemplo: 14): '))
    while not(5 < hora_inicio < 18):
        print('Error. La hora ingresada no es valida')
        hora_inicio = int(input('Ingrese la hora de inicio (Formato 24h - ejemplo: 14): '))

    hora_fin = int(input('Ingrese la hora de fin (Formato 24h - ejemplo: 16): '))
    while not(hora_inicio < hora_fin < 19):
        print('Error. La duracion de la clase no es valida.')
        hora_fin = int(input('Ingrese la hora de fin (Formato 24h - ejemplo: 16): '))

    ubicacion = input('Ingrese la ubicación (opcional, presione ENTER para omitir): ')
    aux = True

    
    for materia in materias:
        if (materia['dia'] == dia) and cruce(materia['hora_inicio'],materia['hora_fin'],hora_inicio,hora_fin):
            print('\nError. La materia se cruza con otra.\n')
            aux = False
            break

    if aux == True:
        materia_registro = {
            'clase': clase,
            'dia': dia,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
            'ubicacion': ubicacion
        }
        with open('registro.json', mode='w', encoding='utf-8') as registro:
            materias.append(materia_registro)
            json.dump(materias, registro, indent=4, ensure_ascii=False)

        if ubicacion == '' : 
            print(f'\nMateria {clase} registrada exitosamente el {dia} de {hora_inicio}:00 a {hora_fin}:00.\n')
        else:
            print(f'\nMateria {clase} registrada exitosamente el {dia} de {hora_inicio}:00 a {hora_fin}:00 en {ubicacion}.\n')