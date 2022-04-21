def ingresarPersona(personas: list) -> str:
    personas_presentes = 'Identificación\tNombre\tDestino\tOficina\n'
    for persona in personas:
        datos_persona = ''
        if persona[2] == 'Gerencia':
            persona.append('302')
        elif persona[2] == 'Ventas':
            persona.append('105')
        elif persona[2] == 'Producción':
            persona.append('201')
        for dato in persona:
            datos_persona += f'{dato}\t'
        personas_presentes += f'\n{datos_persona[:-1]}'
    return personas_presentes

print(ingresarPersona([['1110934100', 'Nicolas Machado', 'Producción'],['1110312456', 'Rebeca Vega', 'Ventas'],['1110462238', 'Andres Villanueva', 'Gerencia']]))
print(ingresarPersona([['1110398416', 'Marcela Cervera', 'Ventas'],['1110133221', 'Claudia Perez', 'Producción'],['1110934100', 'Nicolas Machado', 'Gerencia']]))
print(ingresarPersona([['1110973354', 'Sebastian Gomez', 'Producción'],['1110743310', 'Estefania Vallejo', 'Gerencia'],['1110014965', 'Helena Vargas', 'Producción']]))
print(ingresarPersona([['1110133221', 'Claudia Perez', 'Ventas'],['1110312456', 'Rebeca Vega', 'Gerencia'],['1110033495', 'Violeta Murcia', 'Producción']]))
print(ingresarPersona([['1110759130', 'Julio Paredes', 'Gerencia'],['1110987631', 'Natalia Saldaña', 'Producción'],['1110397410', 'Ofelia Duarte', 'Ventas']]))