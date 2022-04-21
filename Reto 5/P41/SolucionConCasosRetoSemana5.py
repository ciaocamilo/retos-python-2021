# Solución del reto en la plataforma
import pandas as pd

def analizarDatos(archivo, porcentaje):
    df = pd.read_csv(archivo, sep=';')
    ventas = df.groupby(['MES']).size()
    mes_mayor = ventas.idxmax()
    valor_mes_mayor = ventas.max()
    proyeccion = valor_mes_mayor * (1 + porcentaje)

    return { 'Mes mayor venta': mes_mayor, 'Cantidad de ventas': valor_mes_mayor, 'proyección': proyeccion }


# Llamados a la función para generar la salida esperada
# print('-----Salidas Esperadas-----')
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/ventas2021.csv', 0.056))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/ventas2021.csv', 0.041))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/ventas2021.csv', 0.048))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/ventas2021.csv', 0.034))
# print(analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/ventas2021.csv', 0.029))
