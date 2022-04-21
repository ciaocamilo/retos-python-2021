# Solución del reto en la plataforma
import numpy as np

def generarResultados(datos):
    datos_ajustados = []

    for participante in datos:
        participante = list(map(lambda puntaje: 4 if puntaje < 5 else puntaje, participante))
        datos_ajustados.append(participante)

    matriz = np.array(datos_ajustados)
    promedio = round(matriz.mean(), 2)
    calificacion = np.sum(matriz, axis = 1)
    ganador = calificacion.argmax() + 1

    resultados = { 'puntaje promedio': promedio, 'puntaje participante 1': calificacion[0], 'puntaje participante 2': calificacion[1],'puntaje participante 3': calificacion[2], 'participante ganador': ganador}

    return resultados

#Llamados a la función para generar la salida esperada
# print('-----Salidas Esperadas-----')
# print(generarResultados([[4,6,8], [1,2,3], [6,5,5]]))
# print(generarResultados([[8,4,6], [3,3,4], [5,3,6]]))
# print(generarResultados([[8,7,5], [1,2,3], [10,9,11]]))
# print(generarResultados([[10,8,5], [11,10,8], [7,6,6]]))
# print(generarResultados([[10,12,9], [5,6,7], [10,8,9]]))

