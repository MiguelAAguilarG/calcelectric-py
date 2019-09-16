from math import sqrt, pi
import calculos
import elementos
import tablas
import datos

if __name__ == "__main__":
    datos = datos.datos_entrada_dict
    Carga = elementos.Carga(datos)

    Carga.calculo_basico()