# Solución del reto en la plataforma
import numpy as np

def generarResultados(datos):
    datos_ajustados = []

    for participante in datos:
        participante = list(map(lambda puntaje: 5 if puntaje < 6 else puntaje, participante))
        datos_ajustados.append(participante)

    matriz = np.array(datos_ajustados)
    promedio = round(matriz.mean(), 2)
    calificacion = np.sum(matriz, axis = 1)
    ganador = calificacion.argmax() + 1

    resultados = { 'puntaje promedio': promedio, 'puntaje participante 1': calificacion[0], 'puntaje participante 2': calificacion[1],'puntaje participante 3': calificacion[2], 'participante ganador': ganador}

    return resultados

#Llamados a la función para generar la salida esperada
# print('-----Salidas Esperadas-----')
# print(generarResultados([[6,8,9], [10,7,8], [4,5,7]])) #
# print(generarResultados([[14,10,8], [13,11,10], [8,4,5]]))
# print(generarResultados([[6,5,4], [10,12,13], [1,4,5]])) #
# print(generarResultados([[9,4,5], [12,7,7], [9,5,6]]))
# print(generarResultados([[3,2,1], [6,3,4], [9,7,5]]))

