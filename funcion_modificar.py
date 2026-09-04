import json

from funcion_registro import cruce

def modificar_registro(materias):
    for materia in materias:
        print(f"\nClase: {materia['clase']}")
        print(f"{materia['dia']} de {materia['hora_inicio']} a {materia['hora_fin']}\n")
    materia_modificar = input('Ingrese la materia que desea modificar: ').upper()
    dias = []
    horas = []

    for materia in materias:
        if materia['clase'] == materia_modificar:
            dias.append(materia['dia'])
    dias = list(set(dias))

    if len(dias) > 0: 
        print('En que dia desea hacer el ajuste?:\n')

        for dia in dias:
            print(dia)
        dia_modificar = input('\n').lower()

        while dia_modificar not in dias:
            dia_modificar = input('\nEl dia ingresado no es valido. Vuelva a intentar:').lower()

        for materia in materias:
            if (materia['clase'] == materia_modificar) and (materia['dia'] == dia_modificar):
                horas.append(materia['hora_inicio'])

        print('En que horario desea hacer el ajuste? (ingrese la hora de inicio): ')

        for hora in horas:
            print(f'{hora}:00')
            
        hora_modificar = int(input('\n'))

        while hora_modificar not in horas:
            hora_modificar = int(input('\nEl horario ingresado no es valido. Vuelva a intentar:'))

        print(f'la clase a modificar es: {materia_modificar} el {dia_modificar} horario {hora_modificar}:00')

        for materia in materias:
            if (materia['clase'] == materia_modificar) and (materia['dia'] == dia_modificar) and (materia['hora_inicio'] == hora_modificar):
                materias.remove(materia)

        semana = ['lunes','martes','miercoles','jueves','viernes','sabado']

        dia = input('Ingrese el nuevo dia de la semana: ').lower()
        while dia not in semana:
            print('Error. El dia ingresado no es valido')
            dia = input('Ingrese el nuevo dia de la semana: ').lower()
        
        hora_inicio = int(input('Ingrese la nueva hora de inicio (Formato 24h - ejemplo: 14): '))
        while not(5 < hora_inicio < 18):
            print('Error. La hora ingresada no es valida')
            hora_inicio = int(input('Ingrese la nueva hora de inicio (Formato 24h - ejemplo: 14): '))

        hora_fin = int(input('Ingrese la nueva hora de fin (Formato 24h - ejemplo: 16): '))
        while not(hora_inicio < hora_fin < 19):
            print('Error. La duracion de la clase no es valida.')
            hora_fin = int(input('Ingrese la nueva hora de fin (Formato 24h - ejemplo: 16): '))
        
        ubicacion = input('Ingrese la nueva ubicación (opcional, presione ENTER para omitir): ')
        aux = True

        for materia in materias:
            if (materia['dia'] == dia) and cruce(materia['hora_inicio'],materia['hora_fin'],hora_inicio,hora_fin):
                print('\nError. La materia se cruza con otra.\n')
                aux = False
                break
        
        if aux == True:
            materia_registro = {
                'clase': materia_modificar,
                'dia': dia,
                'hora_inicio': hora_inicio,
                'hora_fin': hora_fin,
                'ubicacion': ubicacion
            }
            with open('registro.json', mode='w', encoding='utf-8') as registro:
                materias.append(materia_registro)
                json.dump(materias, registro, indent=4, ensure_ascii=False)

            print('\nLa materia fue modificada exitosamente.')
        else:
            print('\nLa materia no pudo ser modificada debido a un cruce de horario.')

    else:
        print('\nEl dia no existe.')  
    
