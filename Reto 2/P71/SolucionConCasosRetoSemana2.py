# Solución del reto en la plataforma
def realizarPedido(sopa: str, plato_principal: str, bebida: str, postre: str) -> dict:
    pedido = {'sopa': sopa, 'plato principal': plato_principal, 'bebida': bebida, 'postre': postre, 'total': 0}
    costo_total = 0
    descuento = 0
    if sopa == 'Sopa de pastas':
        costo_total += 3000
    if plato_principal == 'Pollo apanado':
        costo_total += 7000
    elif plato_principal == 'Albóndigas en salsa':
        costo_total += 8000
    if bebida == 'Jugo de uva':
        costo_total += 2000
    elif bebida == 'Limonada':
        costo_total += 1500
    if postre == 'Merengón':
        costo_total += 5000
    elif postre == 'Leche asada':
        costo_total += 4000
    if (postre == 'Merengón' and plato_principal == 'Pollo apanado') or (postre == 'Merengón' and sopa == 'Sopa de pastas'):
        descuento = 0.3
    costo_total = costo_total * (1 - descuento)
    pedido['total'] = int(costo_total)
    return pedido

#Llamados a la función para generar la salida esperada
print('-----Salidas Esperadas-----')
print(realizarPedido("Sopa de pastas", "Pollo apanado", "Jugo de uva", "Merengón"))
print(realizarPedido("", "Albóndigas en salsa", "Limonada", "Leche asada"))
print(realizarPedido("Sopa de pastas", "Albóndigas en salsa", "Jugo de uva", "Merengón"))
print(realizarPedido("", "Pollo apanado", "Limonada", "Leche asada"))
print(realizarPedido("", "Albóndigas en salsa", "Limonada", ""))