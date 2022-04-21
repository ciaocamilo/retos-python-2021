# Solución del reto en la plataforma
def calcularPorcentajes(tipo_1: str, valor_1: int, tipo_2: str, valor_2: int, tipo_3: str, valor_3: int, tipo_4: str, valor_4: int, tipo_5: str, valor_5: int) -> str:
    total = valor_1 + valor_2 + valor_3 + valor_4 + valor_5
    p_1 = (valor_1 / total) * 100
    p_2 = (valor_2 / total) * 100
    p_3 = (valor_3 / total) * 100
    p_4 = (valor_4 / total) * 100
    p_5 = (valor_5 / total) * 100
    return f"{tipo_1}: {p_1}% - {tipo_2}: {p_2}%  - {tipo_3}: {p_3}%  - {tipo_4}: {p_4}%  - {tipo_5}: {p_5}%"

#Llamados a la función para generar la salida esperada
print('-----Salidas Esperadas-----')
print (calcularPorcentajes("Vehículo particular", 76, "Transporte público bus", 150, "Taxi", 96, "App de transporte", 31, "A pie", 47))
print (calcularPorcentajes("Motocicleta", 90, "Transporte público bus", 79, "Bicicleta", 69, "App de transporte", 80, "Caballo", 82))
print (calcularPorcentajes("Vehículo particular", 99, "Burro", 86, "Taxi", 13, "Caballo", 77, "Jeep", 125))
print (calcularPorcentajes("Camioneta", 120, "Transporte público bus", 100, "Tren", 40, "App de transporte", 15, "Motocicleta", 125))
print (calcularPorcentajes("Elefante", 77, "Tractomula", 66, "Taxi", 150, "App de transporte", 33, "A pie", 74))
