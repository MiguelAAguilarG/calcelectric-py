import datos
import calculos
import tablas

class Carga(calculos.Calculos):

    def __init__(self, datos_entrada, *args, **kargs):
        super().__init__()

        self.datos_entrada = datos_entrada

        self.Sistema = self.datos_entrada['Sistema']
        self.lineas = self.datos_entrada['lineas']
        self.Voltaje = self.datos_entrada['Voltaje']
        self.Carga = self.datos_entrada['Carga']
        self.fp = self.datos_entrada['fp']
        self.factor_utilizacion_carga = self.datos_entrada['factor_utilizacion_carga']
        self.factor_simultaneidad_carga = self.datos_entrada['factor_simultaneidad_carga']
        self.Interruptor_forzado = self.datos_entrada['Interruptor_forzado']
        self.tipo_circuito = self.datos_entrada['tipo_circuito']
        self.caida_tension = self.datos_entrada['caida_tension']
        self.Longitud = self.datos_entrada['Longitud']
        self.Tambiente = self.datos_entrada['Tambiente']
        self.aislante_conductor = self.datos_entrada['aislante_conductor']
        self.Taislante = self.datos_entrada['Taislante']
        self.Tterminales = self.datos_entrada['Tterminales']
        self.material_conductor = self.datos_entrada['material_conductor']
        self.numero_conductores_por_fase = self.datos_entrada['numero_conductores_por_fase']
        self.numero_conductores_neutro = self.datos_entrada['numero_conductores_neutro']
        self.tamano_neutro_porcentaje_Inominal = self.datos_entrada['tamano_neutro_porcentaje_Inominal']
        self.neutro_activo = self.datos_entrada['neutro_activo']
        self.tierra_fisica_forrada = self.datos_entrada['tierra_fisica_forrada']
        self.adicionar_tierra_fisica_aislada = self.datos_entrada['adicionar_tierra_fisica_aislada']
        self.canalizacion = self.datos_entrada['canalizacion']
        self.tipo_conduit = self.datos_entrada['tipo_conduit']
        self.material_canalizacion = self.datos_entrada['material_canalizacion']
        self.misma_canalizacion = self.datos_entrada['misma_canalizacion']
        self.conductores_activos_adicionales_misma_canalizacion = self.datos_entrada['conductores_activos_adicionales_misma_canalizacion']
        self.conductores_no_activos_adicionales_misma_canalizacion = self.datos_entrada['conductores_no_activos_adicionales_misma_canalizacion']

    def calculo_basico(self, *args, **kargs):
        ####################
        self.Inominal = self.calculo_Inominal(self.Sistema, self.Carga, self.Voltaje, self.fp)

        self.Icorregida_factor_ampacidad_cable = self.calculo_Icorregida_factor_ampacidad_cable(self.Inominal, self.factor_ampacidad_cable_fase)

        self.Carga_corregida_factor_utilizacion_carga = self.calculo_Carga_corregida_factor_utilizacion_carga(self.Carga, self.factor_utilizacion_carga)

        self.Carga_corregida_factor_simultaneidad_carga = self.calculo_Carga_corregida_factor_simultaneidad_carga(self.Carga, self.factor_simultaneidad_carga)

        self.conductores_activos_canalizacion = self.calculo_conductores_activos_canalizacion(self.conductores_activos_adicionales_misma_canalizacion, self.misma_canalizacion, self.lineas, self.numero_conductores_por_fase, self.neutro_activo, self.numero_conductores_neutro)

        self.Interruptor, self.porcentaje_utilizacion_Interruptor = self.calculo_Interruptor(self.Inominal, self.Interruptor_forzado, self.factor_utilizacion_interruptor, tablas.Tablas.Interruptores_tabla)
        ####################
        self.tabla_ampacidad_dict = tablas.Tablas.Ampacidad_tabla_310_15_b16
        self.parte_adecuada_tabla_ampacidad_dict = self.tabla_ampacidad_dict['datos']['material_conductor'][self.material_conductor]['Taislante']
        self.Tambiente_tabla_factor_temperatura = self.tabla_ampacidad_dict['parametros']['Tambiente']
        ####################
        self.factor_temperatura = self.calculo_factor_temperatura(self.Tambiente_tabla_factor_temperatura, self.Taislante, self.Tambiente)

        self.factor_agrupamiento = self.calculo_factor_agrupamiento(tablas.Tablas.factor_agrupamiento_tabla, self.Longitud, self.conductores_activos_canalizacion)

        self.indice_ampacidad, self.calibre_ampacidad, self.Area_ampacidad, self.Ampacidad, self.Ampacidad_corregida = self.calculo_cable_ampacidad(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.parte_adecuada_tabla_ampacidad_dict, self.Taislante, self.Tterminales, self.factor_agrupamiento, self.factor_temperatura, self.Interruptor, self.numero_conductores_por_fase,self.Tambiente_tabla_factor_temperatura, self.Tambiente)
        ####################
        self.tabla_caida_resistencia_adecuada_lista = tablas.Tablas.impedancia_tabla_9['datos']['resistencia']['material_conductor'][self.material_conductor]['material_canalizacion'][self.material_canalizacion]
        self.tabla_caida_reactancia_adecuada_lista = tablas.Tablas.impedancia_tabla_9['datos']['reactancia']['material_conductor'][self.material_conductor]['material_canalizacion'][self.material_canalizacion]
        ####################
        self.indice_caida, self.calibre_caida, self.Area_caida, self.caida_tension_calculada = self.calculo_cable_caida_de_tension(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_caida_resistencia_adecuada_lista, self.tabla_caida_reactancia_adecuada_lista, self.caida_tension, self.Sistema, self.fp, self.Longitud, self.Inominal, self.Voltaje, self.numero_conductores_por_fase)
        ####################
        self.tabla_interruptor_tierra_fisica_adecuada_lista = tablas.Tablas.calibre_tierra_fisica_tabla_250_122['datos']['interruptor']
        self.tabla_tierra_fisica_adecuada_lista = tablas.Tablas.calibre_tierra_fisica_tabla_250_122['datos']['material_conductor'][self.material_conductor]
        ####################
        self.indice_tierra_fisica, self.calibre_tierra_fisica, self.Area_tierra_fisica = self.calculo_cable_tierra_fisica(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_interruptor_tierra_fisica_adecuada_lista, self.tabla_tierra_fisica_adecuada_lista, self.Interruptor, self.canalizacion, self.Area_caida, self.Area_ampacidad)

        self.factor_correccion_cable_tierra_fisica, self.Area_tierra_fisica_corregida_ideal, self.indice_tierra_fisica_corregida, self.calibre_tierra_fisica_corregida, self.Area_tierra_fisica_corregida = self.calculo_cable_tierra_fisica_corregida(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.Area_caida, self.Area_ampacidad, self.Area_tierra_fisica)

        self.indice_cable, self.calibre_cable, self.Area_cable = self.calculo_eleccion_cable_ampacidad_caida(self.indice_ampacidad, self.calibre_ampacidad, self.Area_ampacidad, self.indice_caida, self.calibre_caida, self.Area_caida)

        '''self.indice_cable, self.calibre_cable, self.Area_cable = self.calculo_eleccion_cable_tierra_fisica(self.indice_ampacidad, self.calibre_ampacidad, self.Area_ampacidad, self.indice_caida, self.calibre_caida, self.Area_caida)'''
        ####################
        self.tabla_conduit_adecuada_lista = tablas.Tablas.dimensiones_tubo_conduit_tabla_4['datos']['tipo_conduit'][self.tipo_conduit]
        ####################

        self.datos_salida_dict = {
        'Inominal': self.Inominal,
        'Icorregida_factor_ampacidad_cable': self.Icorregida_factor_ampacidad_cable,
        'Carga_corregida_factor_utilizacion_carga': self.Carga_corregida_factor_utilizacion_carga,
        'Carga_corregida_factor_simultaneidad_carga': self.Carga_corregida_factor_simultaneidad_carga,
        'conductores_activos_canalizacion': self.conductores_activos_canalizacion,
        'Interruptor': self.Interruptor,
        'porcentaje_utilizacion_Interruptor': self.porcentaje_utilizacion_Interruptor,
        'factor_temperatura': self.factor_temperatura,
        'factor_agrupamiento': self.factor_agrupamiento,
        'calibre_ampacidad': self.calibre_ampacidad, 
        'Area_ampacidad': self.Area_ampacidad, 
        'Ampacidad': self.Ampacidad, 
        'Ampacidad_corregida': self.Ampacidad_corregida,
        'calibre_caida': self.calibre_caida,
        'Area_caida': self.Area_caida,
        'caida_tension_calculada': self.caida_tension_calculada,
        'calibre_tierra_fisica': self.calibre_tierra_fisica, 
        'Area_tierra_fisica': self.Area_tierra_fisica,
        'factor_correccion_cable_tierra_fisica': self.factor_correccion_cable_tierra_fisica,
        'Area_tierra_fisica_corregida_ideal': self.Area_tierra_fisica_corregida_ideal,
        'calibre_tierra_fisica_corregida': self.calibre_tierra_fisica_corregida,
        'Area_tierra_fisica_corregida': self.Area_tierra_fisica_corregida,
        'calibre_cable_fase': self.calibre_cable,
        'Area_cable_fase': self.Area_cable,}
        ''''calibre_tierra_fisica_final': self.calibre_tierra_fisica_final,
        'Area_tierra_fisica_final': self.Area_tierra_fisica_final,'''
        

        print(self.datos_por_defecto_Calculos_dict)
        print(self.datos_entrada)
        print(self.datos_salida_dict)

