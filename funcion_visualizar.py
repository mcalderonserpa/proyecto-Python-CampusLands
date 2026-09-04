import tabulate as tab

def visualizar_horario(materias):
    horario = [

        ['']* 15,
        ['']* 15,
        ['']* 15,
        ['']* 15,
        ['']* 15,
        ['']* 15,
    ]

    semana = ['lunes','martes','miercoles','jueves','viernes','sabado']

    for i in range(6):
        horario[i][0] = semana[i]

    for materia in materias:
        for dia in range(len(semana)):
            if materia['dia'] == semana[dia]:
                for i in range(materia['hora_fin'] - materia['hora_inicio']):
                    horario[dia][materia['hora_inicio']-5 + i] = materia['clase']

    horas = ['Form. 24H']
    for i in range(13):
            horas.append(f'{i+6}:00')
    horario.insert(0, horas)

    horario = list(map(list, zip(*horario))) # Trasponer la matriz

    print(tab.tabulate(horario, tablefmt='grid'))