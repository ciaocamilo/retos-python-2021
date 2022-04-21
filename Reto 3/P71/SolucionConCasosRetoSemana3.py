# Solución del reto en la plataforma
def matricularCurso(estudiantes: list) -> str:
    matriculados = 'Identificación\tNombre\tPuntaje\tGrupo\n'
    for estudiante in estudiantes:
        datos_estudiante = ''
        if estudiante[2] >= 0 and estudiante[2] <= 30:
            estudiante.append('A-Principiante')
        elif estudiante[2] >= 31 and estudiante[2] <= 70:
            estudiante.append('B-Intermedio')
        elif estudiante[2] >= 71 and estudiante[2] <= 100:
            estudiante.append('C-Avanzado')
        for dato in estudiante:
            datos_estudiante += f'{dato}\t'
        matriculados += f'\n{datos_estudiante[:-1]}'
    return matriculados

print(matricularCurso([['1110033495', 'Violeta Murcia', 63], ['1110783206', 'Claudia Gallego', 77], ['1110953217', 'Manuel Gonzalez', 45]]))
print(matricularCurso([['1110398416', 'Marcela Cervera', 19], ['1110569478', 'Alexander Pinto', 34], ['1110987631', 'Natalia Saldaña', 29]]))
print(matricularCurso([['1110397410', 'Ofelia Duarte', 39], ['1110743310', 'Estefania Vallejo', 67], ['1110312456', 'Rebeca Vega', 48]]))
print(matricularCurso([['1110014965', 'Helena Vargas', 74], ['1110973354', 'Sebastian Gomez', 80], ['1110462238', 'Andres Villanueva', 29]]))
print(matricularCurso([['1110759130', 'Julio Paredes', 93], ['1110133221', 'Claudia Perez', 17], ['1110934100', 'Nicolas Machado', 32]]))