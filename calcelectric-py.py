from math import sqrt, pi
import calculos
import elementos
import tablas
import datos
from pprint import pprint

if __name__ == "__main__":

    #Se crea un objeto Carga que se encuentra en el módulo elementos.py
    #Por el momento no hay verificación de los datos introducidos en la Carga

    #Carga = elementos.Carga(datos.datos_entrada_dict, datos.datos_por_defecto_Calculos_dict)
    Carga = elementos.Carga(datos.datos_entrada_dict)

    #Se procede a hacer el cálculo que se desea hacer para la carga, un cálculo completo es calculo_basico, por el momento, solo hay ese cálculo completo, este esta compuesto por cálculos que se encuentran en el módulo calculos.py. calculo_basico es un método en la Clase Carga
    datos_por_defecto_Calculos_dict, datos_entrada, datos_salida_dict = Carga.calculo_basico()

    pprint(datos_por_defecto_Calculos_dict, sort_dicts = False) #sort_dicts solo disponible en python 3.8
    print('')
    pprint(datos_entrada, sort_dicts = False)
    print('')
    pprint(datos_salida_dict, sort_dicts = False)


