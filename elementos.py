import calculos
import tablas

class Carga(calculos.Calculos):

    def __init__(self, datos_entrada, *args, **kargs):
        super().__init__()

        self.datos_entrada = datos_entrada

        self.Sistema = self.datos_entrada['Sistema']
        self.Voltaje = self.datos_entrada['Voltaje']
        self.Carga = self.datos_entrada['Carga']
        self.factor_carga = self.datos_entrada['factor_carga']
        self.fp =self.datos_entrada['fp']
        self.caida_tension = self.datos_entrada['caida_tension']
        self.Longitud = self.datos_entrada['Longitud']
        self.Tambiente = self.datos_entrada['Tambiente']
        self.aislante_conductor = self.datos_entrada['aislante_conductor']
        self.Taislante = self.datos_entrada['Taislante']
        self.Tterminales = self.datos_entrada['Tterminales']
        self.material_conductor = self.datos_entrada['material_conductor']
        self.numero_conductores_por_fase = self.datos_entrada['numero_conductores_por_fase']
        self.misma_canalizacion = self.datos_entrada['misma_canalizacion']
        self.porcentaje_utilizacion_Interruptor = self.datos_entrada['porcentaje_utilizacion_Interruptor']
        self.Interruptor_forzado = self.datos_entrada['Interruptor_forzado']
        self.canalizacion = self.datos_entrada['canalizacion']
        self.material_canalizacion = self.datos_entrada['material_canalizacion']
        self.tipo_conduit = self.datos_entrada['tipo_conduit']
        self.neutro_presente = self.datos_entrada['neutro_presente']
        self.factor_utilizacion_carga = self.datos_entrada['factor_utilizacion_carga']
        self.factor_simultaneidad_carga = self.datos_entrada['factor_simultaneidad_carga']

    def calculo_basico(self, *args, **kargs):
        self.calculo_Inominal()
        self.calculo_Icorregida_factor_ampacidad_cable()
        self.calculo_Carga_corregida_factor_utilizacion_carga()
        self.calculo_Carga_corregida_factor_simultaneidad_carga()
        self.calculo_conductores_canalizacion()
        self.calculo_Interruptor()

        self.tabla_ampacidad_dict = tablas.Tablas.Ampacidad_tabla_310_15_b16
        self.parte_adecuada_tabla_ampacidad_dict = tablas.Tablas.Ampacidad_tabla_310_15_b16['datos']['material_conductor'][self.material_conductor]['Taislante'][self.Taislante]

        self.calculo_factor_temperatura(self.tabla_ampacidad_dict)
        self.calculo_factor_agrupamiento(tablas.Tablas.factor_agrupamiento_tabla)
        self.calculo_cable_ampacidad(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_ampacidad_dict)

        self.tabla_caida_resistencia_adecuada_lista = tabla.Tabla.impedancia_tabla_9['datos']['resistencia']['material_conductor'][self.material_conductor]['material_canalizacion'][self.material_canalizacion]
        self.tabla_caida_resistencia_adecuada_lista = tabla.Tabla.impedancia_tabla_9['datos']['reactancia']['material_conductor'][self.material_conductor]['material_canalizacion'][self.material_canalizacion]

        self.calculo_cable_caida_de_tension(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_caida_resistencia_adecuada_lista, self.tabla_caida_reactancia_adecuada_lista)

        datos_salida_dict = {
        'Inominal': self.Inominal,
        'Icorregida_factor_ampacidad_cable': self.Icorregida_factor_ampacidad_cable,
        'Carga_corregida_factor_utilizacion_carga': self.Carga_corregida_factor_utilizacion_carga,
        'Carga_corregida_factor_simultaneidad_carga': self.Carga_corregida_factor_simultaneidad_carga,
        'conductores_canalizacion': self.conductores_canalizacion,
        'Interruptor': self.Interruptor,
        'factor_temperatura': self.factor_temperatura,
        'factor_agrupamiento': self.factor_agrupamiento,
        'indice_ampacidad': self.indice_ampacidad,
        'calibre_ampacidad': self.calibre_ampacidad, 
        'Area_ampacidad': self.Area_ampacidad, 
        'Ampacidad': self.Ampacidad, 
        'Ampacidad_corregida': self.Ampacidad_corregida,
        'indice_caida': self.indice_caida,
        'calibre_caida': self.calibre_caida,
        'Area_caida': self.Area_caida,
        'caida_tension_calculada': self.caida_tension_calculada,
        }

        print(datos_salida_dict)

        

