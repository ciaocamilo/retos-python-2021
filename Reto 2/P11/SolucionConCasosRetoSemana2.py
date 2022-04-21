# Solución del reto en la plataforma
def comprarEntrada(infantil: str, familiar: str, alto_impacto: str, cantidad_personas: int) -> dict:
    combo = {'infantil': infantil, 'familiar': familiar, 'alto impacto': alto_impacto, 'obsequio': '', 'personas': cantidad_personas, 'total': 0}
    costo_total = 0

    if infantil == 'Trencito':
        costo_total += 5000
    elif infantil == 'Mini rueda':
        costo_total += 5500
    if familiar == 'Carrusel':
        costo_total += 6000
    elif familiar == 'Carros chocones':
        costo_total += 8000
    if alto_impacto == 'Barco pirata':
        costo_total += 8500
    elif alto_impacto == 'Montaña rusa':
        costo_total += 9000
    if infantil == 'Trencito' and cantidad_personas > 2:
        combo['obsequio'] = 'Peluche'
    if (familiar == 'Carrusel' and cantidad_personas > 3) or (alto_impacto == 'Barco pirata' and cantidad_personas > 2):
        combo['obsequio'] = 'Carros chocones'

    combo['total'] = costo_total * cantidad_personas
    return combo

#Llamados a la función para generar la salida esperada
print('-----Salidas Esperadas-----')
print(comprarEntrada('Trencito', 'Carrusel', 'Montaña rusa', 3))

print(comprarEntrada('', 'Carros chocones', 'Barco pirata', 4))
print(comprarEntrada('Mini rueda', 'Carrusel', 'Montaña rusa', 2))
print(comprarEntrada('', 'Carros chocones', 'Barco pirata', 6))
print(comprarEntrada('', 'Carrusel', 'Montaña rusa', 5))