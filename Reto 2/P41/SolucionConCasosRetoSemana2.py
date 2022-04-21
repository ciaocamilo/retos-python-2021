# Solución del reto en la plataforma
def comprarRopa(nino: str, mujer: str, hombre: str, tarjeta_puntos: bool) -> dict:
    compra = {'niño': nino, 'mujer': mujer, 'hombre': hombre, 'bono': 0, 'total': 0}
    costo_total = 0
    bono = 0

    if nino == 'Camiseta':
        costo_total += 19900
    elif nino == 'Saco':
        costo_total += 45000
    if mujer == 'Vestido':
        costo_total += 60000
    elif mujer == 'Camiseta manga corta':
        costo_total += 35000
    if hombre == 'Chaqueta':
        costo_total += 90000
    elif hombre == 'Camisa':
        costo_total += 59500
    if tarjeta_puntos == True or (mujer == 'Vestido' and hombre == 'Chaqueta'):
        bono = 0.15

    costo_total = costo_total * (1 - bono)
    compra['total'] = int(costo_total)
    compra['bono'] = bono
    return compra

#Llamados a la función para generar la salida esperada
print('-----Salidas Esperadas-----')
print(comprarRopa('Saco', 'Vestido', 'Camisa', True))
print(comprarRopa('Camiseta', 'Vestido', '', False))
print(comprarRopa('Camiseta', '', 'Camisa', False))
print(comprarRopa('Saco', 'Vestido', 'Chaqueta', False))
print(comprarRopa('', 'Camiseta manga corta', '', True))