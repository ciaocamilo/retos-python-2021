# Solución del reto en la plataforma
def asignarCita(pacientes: list) -> str:
    citas = 'Identificación\tPaciente\tHora\tMédico asignado\n'
    for paciente in pacientes:
        datos_paciente = ''
        if paciente[2] >= 8 and paciente[2] <= 12:
            paciente.append('Juan Perez')
        elif paciente[2] >= 14 and paciente[2] < 18:
            paciente.append('Maria Lopez')
        elif paciente[2] >= 18 and paciente[2] < 20:
            paciente.append('Pedro Rodriguez')
        for dato in paciente:
            datos_paciente += f'{dato}\t'
        citas += f'\n{datos_paciente[:-1]}'
    return citas

print(asignarCita([['1110569478', 'Alexander Pinto', 14], ['1110934100','Nicolas Machado', 10], ['1110312456', 'Rebeca Vega', 8]]))
print(asignarCita([['1110397410', 'Ofelia Duarte', 19], ['1110398416', 'Marcela Cervera', 16], ['1110973354', 'Sebastian Gomez', 9]]))
print(asignarCita([['1110133221', 'Claudia Perez', 18], ['1110953217', 'Manuel Gonzalez', 11], ['1110462238', 'Andres Villanueva', 15]]))
print(asignarCita([['1110033495', 'Violeta Murcia', 8], ['1110783206', 'Claudia Gallego', 19], ['1110759130', 'Julio Paredes', 17]]))
print(asignarCita([['1110987631', 'Natalia Saldaña', 10], ['1110014965', 'Helena Vargas', 8], ['1110743310', 'Estefania Vallejo', 14]]))
