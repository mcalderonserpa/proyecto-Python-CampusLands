import json

def eliminar_registro(materias):
    for materia in materias:
        print(f'\nClase: {materia['clase']}')
        print(f'{materia['dia']} de {materia['hora_inicio']} a {materia['hora_fin']}\n')
    materia_borrar = input('Ingrese la materia que desea borrar: ').upper()
    dias = []
    horas = []

    for materia in materias:
        if materia['clase'] == materia_borrar:
            dias.append(materia['dia'])
    dias = list(set(dias))

    if len(dias) > 0: 
        print('En que dia desea hacer la eliminacion?:\n')

        for dia in dias:
            print(dia)
        dia_borrar = input('\n').lower()

        while dia_borrar not in dias:
            dia_borrar = input('\nEl dia ingresado no es valido. Vuelva a intentar:').lower()

        for materia in materias:
            if (materia['clase'] == materia_borrar) and (materia['dia'] == dia_borrar):
                horas.append(materia['hora_inicio'])

        print('Que horario desea eliminar? (ingrese la hora de inicio): ')

        for hora in horas:
            print(f'{hora}:00')
        hora_borrar = int(input('\n'))

        while hora_borrar not in horas:
            hora_borrar = int(input('\nEl horario ingresado no es valido. Vuelva a intentar:'))

        for materia in materias:
            if (materia['clase'] == materia_borrar) and (materia['dia'] == dia_borrar) and (materia['hora_inicio'] == hora_borrar):
                materias.remove(materia)

        with open('registro.json', mode='w', encoding='utf-8') as registro:
            json.dump(materias, registro, indent=4, ensure_ascii=False)

        print(f'La materia {materia_borrar} ha sido eliminada exitosamente.')
    else:
        print('\nLa materia no existe.')  
    
    