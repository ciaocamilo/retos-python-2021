# Solución del reto en la plataforma
def calcularDistancia(c1: str, x1: int, y1: int, c2: str, x2: int, y2: int) -> str:
    distancia = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 2)
    return f"La distancia entre las ciudades {c1} y {c2} es de {distancia} kilómetros"

#Llamados a la función para generar la salida esperada
print('-----Salidas Esperadas-----')
print (calcularDistancia("Ciudad del Este", 9, 3, "Ciudad del Oeste", 3, 4))
print (calcularDistancia("Pereira", 5, 50, "Ibague", 55, 10))
print (calcularDistancia("Bogota", 12, 3, "Tunja", 16, 5))
print (calcularDistancia("Roma", 45, 50, "Venecia", 46, 60))
print (calcularDistancia("Berlin", 50, 70, "Munich", 50, 60))
