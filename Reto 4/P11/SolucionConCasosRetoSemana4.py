# Solución del reto en la plataforma
import numpy as np

def generarResultados(datos):
    datos_ajustados = []

    for participante in datos:
        participante = list(map(lambda puntaje: 3 if puntaje < 4 else puntaje, participante))
        datos_ajustados.append(participante)

    matriz = np.array(datos_ajustados)
    promedio = round(matriz.mean(), 2)
    calificacion = np.sum(matriz, axis = 1)
    ganador = calificacion.argmax() + 1

    resultados = { 'puntaje promedio': promedio, 'puntaje participante 1': calificacion[0], 'puntaje participante 2': calificacion[1],'puntaje participante 3': calificacion[2], 'participante ganador': ganador}

    return resultados

#Llamados a la función para generar la salida esperada
# print('-----Salidas Esperadas-----')
# print(generarResultados([[2,5,4], [7,6,5], [9,7,5]]))
# print(generarResultados([[7,3,5], [2,2,3], [4,2,5]]))
# print(generarResultados([[6,8,9], [4,2,8], [2,1,5]]))
# print(generarResultados([[9,7,4], [10,9,7], [5,5,5]]))
# print(generarResultados([[1,2,3], [4,5,6], [7,8,9]]))

