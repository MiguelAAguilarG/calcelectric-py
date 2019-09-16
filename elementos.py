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

        self.datos_a_buscar_para_tabla_ampacidad_lista = ['datos', 'material_conductor', self.material_conductor, 'Taislante',  self.Taislante]
        self.datos_a_buscar_para_parte_adecuada_de_tabla_ampacidad_dict = {
        'Tambiente': self.Tambiente,
        'Taislante': self.Taislante,
        'material_conductor': self.material_conductor}

        import tablas
        t = tablas.Tablas()

        self.tabla_ampacidad_dict = t.buscar_variable_adecuada(self.datos_a_buscar_para_parte_adecuada_de_tabla_ampacidad_dict)

        self.parte_adecuada_tabla_ampacidad_dict = t.buscar_tupla_adecuada(self.tabla_ampacidad_dict, self.datos_a_buscar_para_tabla_ampacidad_lista)

        self.calculo_factor_temperatura(self.tabla_ampacidad_dict)
        self.calculo_factor_agrupamiento(tablas.Tablas.factor_agrupamiento_tabla)
        self.calculo_cable_ampacidad(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_ampacidad_dict)

        self.datos_a_buscar_para_tabla_caida_lista = ['datos', 'material_conductor', self.material_conductor, 'Taislante',  self.Taislante]
        self.datos_a_buscar_para_parte_adecuada_de_tabla_caida_dict = {
        'Tambiente': self.Tambiente,
        'Taislante': self.Taislante,
        'material_conductor': self.material_conductor}

        self.tabla_caida_dict = t.buscar_variable_adecuada(self.datos_a_buscar_para_parte_adecuada_de_tabla_caida_dict)

        self.parte_adecuada_tabla_caida_dict = t.buscar_tupla_adecuada(self.tabla_caida_dict, self.datos_a_buscar_para_tabla_caida_lista)

        self.calculo_cable_caida_de_tension(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, tabla_de_impedancias)
        self.calculo_cable_tierra_fisica(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, tablas.Tablas.calibre_tierra_fisica_tabla_250_122, tierra_fisica_tabla)

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
        'Ampacidad_corregida': self.Ampacidad_corregida
        }

        print(datos_salida_dict)

        

