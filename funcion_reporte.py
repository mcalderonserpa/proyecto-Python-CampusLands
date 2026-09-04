import json

def generar_reporte(materias):
    grupos = {}

    for materia in materias:
        dia = materia['dia']

        if dia not in grupos:
            grupos[dia] = []

        grupos[dia].append({
            'clase': materia['clase'],
            'hora_inicio': materia['hora_inicio'],
            'hora_fin': materia['hora_fin'],
            'ubicacion': materia['ubicacion']
        })

    orden_dias = [
        'lunes',
        'martes',
        'miercoles',
        'jueves',
        'viernes',
        'sabado',
        'domingo'
    ]

    reporte = []

    for dia in orden_dias:
        if dia in grupos:
            eventos = grupos[dia]

            eventos.sort(key=lambda evento: evento['hora_inicio'])

            reporte.append({
                'dia': dia,
                'eventos': eventos
            })

    # Guardar JSON
    with open('reporte.json', 'w', encoding='utf-8') as archivo:
        json.dump(reporte, archivo, ensure_ascii=False, indent=4)

    # Mostrar reporte
    print('====================================================')
    print('REPORTE DEL HORARIO SEMANAL')
    print('====================================================')

    eventos_pagina = 5
    contador = 0
    total_eventos = sum(len(dia['eventos']) for dia in reporte)

    for dia in reporte:
        print(f"{dia['dia']}:")

        for evento in dia['eventos']:
            print(
                f"- {evento['clase']} "
                f"({evento['hora_inicio']} - {evento['hora_fin']}) "
                f"en {evento['ubicacion']}"
            )

            contador += 1

            # Solo pedir ENTER si todavía quedan eventos
            if contador % eventos_pagina == 0 and contador < total_eventos:
                input('\nPresione ENTER para continuar...\n')

        print('----------------------------------------------------')
