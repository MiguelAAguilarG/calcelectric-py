from math import sqrt, pi
import calculos
import elementos
import tablas
import datos

if __name__ == "__main__":

    #Carga = elementos.Carga(datos.datos_entrada_dict, datos.datos_por_defecto_Calculos_dict)
    Carga = elementos.Carga(datos.datos_entrada_dict)

    Carga.calculo_basico()