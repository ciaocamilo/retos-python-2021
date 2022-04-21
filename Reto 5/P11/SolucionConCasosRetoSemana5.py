# Solución del reto en la plataforma
import pandas as pd

def analizarDatos(archivo, porcentaje):
    df = pd.read_csv(archivo, sep=';')
    precios = df.groupby(['PRECIO']).size()
    precio_seleccionado = precios.idxmax()
    veces_precio_seleccionado = precios.max()
    proyeccion = precio_seleccionado * (1 + porcentaje)

    return { 'Precio seleccionado': precio_seleccionado, 'Veces seleccionado': veces_precio_seleccionado, 'proyección': proyeccion }


# Llamados a la función para generar la salida esperada
# print('-----Salidas Esperadas-----')
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.053))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.012))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.041))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.025))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', 0.033))

