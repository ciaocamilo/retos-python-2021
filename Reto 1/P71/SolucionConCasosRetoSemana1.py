# Solución del reto en la plataforma
def calcularCantidadBaldosas(b_ancho: int, b_largo: int, p_ancho: int, p_largo: int) -> str:
    area_baldosa = b_ancho * b_largo
    area_piso = p_ancho * p_largo
    cantidad = round(area_piso / area_baldosa) + 1
    return f"Es necesario adquirir {cantidad} baldosas"

#Llamados a la función para generar la salida esperada
print('-----Salidas Esperadas-----')
print (calcularCantidadBaldosas(40, 60, 346, 495))
print (calcularCantidadBaldosas(30, 30, 346, 495))
print (calcularCantidadBaldosas(40, 40, 346, 495))
print (calcularCantidadBaldosas(40, 60, 235, 322))
print (calcularCantidadBaldosas(30, 30, 150, 200))
