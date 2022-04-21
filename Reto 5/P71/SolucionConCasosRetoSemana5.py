# Solución del reto en la plataforma
import pandas as pd

def analizarDatos(archivo, porcentaje):
    df = pd.read_csv(archivo, sep=';')
    usos = df.groupby(['HORA']).size()
    hora_pico = usos.idxmax()
    valor_hora_pico = usos.max()
    proyeccion = valor_hora_pico * (1 + porcentaje)

    return { 'Hora pico': hora_pico, 'valor': valor_hora_pico, 'proyección': proyeccion }


# Llamados a la función para generar la salida esperada
# print('-----Salidas Esperadas-----')
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/usos_1206.csv', 0.085))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/usos_1206.csv', 0.15))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/usos_1206.csv', 0.1))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/usos_1206.csv', 0.095))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/usos_1206.csv', 0.12))