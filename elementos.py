import datos
import calculos
import tablas
import validacion

class Carga(calculos.Calculos, validacion.Validacion):

    def __init__(self, datos_entrada, datos_por_defecto_Calculos_dict=None):
        super().__init__(datos_por_defecto_Calculos_dict)

        self.datos_entrada = datos_entrada

        self.parametro_validacion_datos_entrada = self.validacion_datos_entrada(self.datos_entrada)

    def calculo_basico(self, *args, **kargs):

        if self.parametro_validacion_datos_entrada:
            pass
        else:
            return dict()
            
        ####################
        self.Carga_corregida_factor_utilizacion_carga = self.calculo_Carga_corregida_factor_utilizacion_carga(self.Carga, self.factor_utilizacion_carga)

        self.Carga_corregida_factor_simultaneidad_carga = self.calculo_Carga_corregida_factor_simultaneidad_carga(self.Carga, self.factor_simultaneidad_carga)

        self.Carga = self.Carga*self.factor_simultaneidad_carga*self.factor_utilizacion_carga

        self.Inominal_fase, self.Inominal_neutro, self.factor_Inominal_fase_aplicado_neutro = self.calculo_Inominal(self.Sistema, self.lineas, self.numero_conductores_neutro, self.Carga, self.Voltaje, self.fp, self.factor_Inominal_fase_aplicado_neutro)

        ''' FASE '''

        self.Icorregida_factor_ampacidad_cable_fase = self.calculo_Icorregida_factor_ampacidad_cable(self.Inominal_fase, self.factor_ampacidad_cable_fase)

        self.conductores_activos_canalizacion, self.numero_conductores_por_fase, self.numero_conductores_neutro, self.neutro_activo_factor_agrupamiento = self.calculo_conductores_activos_canalizacion(self.conductores_activos_adicionales_misma_canalizacion, self.misma_canalizacion, self.lineas, self.numero_conductores_por_fase, self.neutro_activo_factor_agrupamiento, self.numero_conductores_neutro, self.Inominal_fase, self.Inominal_neutro)

        self.Interruptor, self.porcentaje_utilizacion_Interruptor = self.calculo_Interruptor(self.Inominal_fase, self.Interruptor_forzado, self.factor_utilizacion_interruptor, tablas.Tablas.Interruptores_tabla, self.factor_Inominal_Interruptor)
        ####################
        self.tabla_ampacidad_dict = tablas.Tablas.Ampacidad_tabla_310_15_b16
        self.parte_adecuada_tabla_ampacidad_dict = self.tabla_ampacidad_dict['datos']['material_conductor'][self.material_conductor]['Taislante']
        self.Tambiente_tabla_factor_temperatura = self.tabla_ampacidad_dict['parametros']['Tambiente']
        ####################
        self.factor_temperatura = self.calculo_factor_temperatura(self.Tambiente_tabla_factor_temperatura, self.Taislante, self.Tambiente)

        self.factor_agrupamiento = self.calculo_factor_agrupamiento(tablas.Tablas.factor_agrupamiento_tabla, self.Longitud, self.conductores_activos_canalizacion)
        
        ''' Calculo de cable de fase'''

        self.indice_ampacidad_fase, self.calibre_ampacidad_fase, self.Area_ampacidad_fase, self.Ampacidad_fase, self.Ampacidad_corregida_fase = self.calculo_cable_ampacidad(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.parte_adecuada_tabla_ampacidad_dict, self.Taislante, self.Tterminales, self.factor_agrupamiento, self.factor_temperatura, self.Interruptor, self.numero_conductores_por_fase,self.Tambiente_tabla_factor_temperatura, self.Tambiente, self.Icorregida_factor_ampacidad_cable_fase, self.factor_Inominal_Interruptor, 'fase')
        ####################
        self.tabla_caida_resistencia_adecuada_lista = tablas.Tablas.impedancia_tabla_9['datos']['resistencia']['material_conductor'][self.material_conductor]['material_canalizacion'][self.material_canalizacion]
        self.tabla_caida_reactancia_adecuada_lista = tablas.Tablas.impedancia_tabla_9['datos']['reactancia']['material_conductor'][self.material_conductor]['material_canalizacion'][self.material_canalizacion]
        ####################
        self.indice_caida_fase, self.calibre_caida_fase, self.Area_caida_fase, self.caida_tension_calculada = self.calculo_cable_caida_de_tension(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_caida_resistencia_adecuada_lista, self.tabla_caida_reactancia_adecuada_lista, self.caida_tension, self.Sistema, self.lineas, self.fp, self.Longitud, self.Inominal_fase, self.Voltaje, self.numero_conductores_por_fase)

        ''' Elección de cable de fase'''

        self.indice_cable_fase, self.calibre_cable_fase, self.Area_cable_fase = self.calculo_eleccion_cable_ampacidad_VS_caida(self.indice_ampacidad_fase, self.calibre_ampacidad_fase, self.Area_ampacidad_fase, self.indice_caida_fase, self.calibre_caida_fase, self.Area_caida_fase, self.canalizacion, self.numero_conductores_por_fase)

        ''' Calculo de tierra fisica'''

        if self.tipo_circuito == 'acometida':
            ####################
            self.tabla_conductor_entrada_adecuada_dict = tablas.Tablas.conductor_electrodo_tabla_250_66['datos']['conductor_entrada']['material_conductor'][self.material_conductor]
            self.tabla_conductor_electrodo_adecuada_lista = tablas.Tablas.conductor_electrodo_tabla_250_66['datos']['conductor_electrodo']['material_conductor'][self.material_conductor]
            ####################
            self.indice_tierra_fisica, self.calibre_tierra_fisica, self.Area_tierra_fisica = self.calculo_conductor_electrodo(self.numero_conductores_por_fase, self.Area_cable_fase, tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_conductor_entrada_adecuada_dict, self.tabla_conductor_electrodo_adecuada_lista)    
        else:
            ####################
            self.tabla_interruptor_tierra_fisica_adecuada_lista = tablas.Tablas.calibre_tierra_fisica_tabla_250_122['datos']['interruptor']
            self.tabla_tierra_fisica_adecuada_lista = tablas.Tablas.calibre_tierra_fisica_tabla_250_122['datos']['material_conductor'][self.material_conductor]
            ####################
            self.indice_tierra_fisica, self.calibre_tierra_fisica, self.Area_tierra_fisica = self.calculo_cable_tierra_fisica(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_interruptor_tierra_fisica_adecuada_lista, self.tabla_tierra_fisica_adecuada_lista, self.Interruptor, self.canalizacion, self.Area_caida_fase, self.Area_ampacidad_fase)

        self.factor_correccion_cable_tierra_fisica, self.Area_tierra_fisica_corregida_caida_ideal, self.indice_tierra_fisica_corregida, self.calibre_tierra_fisica_corregida_caida, self.Area_tierra_fisica_corregida_caida = self.calculo_cable_tierra_fisica_corregida(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.Area_caida_fase, self.Area_ampacidad_fase, self.Area_tierra_fisica, self.tipo_circuito)

        ''' Elección de cable de tierra fisica'''

        self.indice_tierra_fisica_final, self.calibre_tierra_fisica_final, self.Area_tierra_fisica_final, self.indice_tierra_fisica_aislada, self.calibre_tierra_fisica_aislada, self.Area_tierra_fisica_aislada = self.calculo_eleccion_cable_tierra_fisica(self.indice_tierra_fisica, self.calibre_tierra_fisica, self.Area_tierra_fisica, self.indice_tierra_fisica_corregida, self.calibre_tierra_fisica_corregida_caida, self.Area_tierra_fisica_corregida_caida, self.indice_cable_fase, self.calibre_cable_fase, self.Area_cable_fase, self.canalizacion, self.adicionar_tierra_fisica_aislada)

        ''' NEUTRO '''
        self.Icorregida_factor_ampacidad_cable_neutro = self.calculo_Icorregida_factor_ampacidad_cable(self.Inominal_neutro, self.factor_ampacidad_cable_neutro)
        
        ''' Calculo de cable neutro '''

        self.indice_ampacidad_neutro, self.calibre_ampacidad_neutro, self.Area_ampacidad_neutro, self.Ampacidad_neutro, self.Ampacidad_corregida_neutro = self.calculo_cable_ampacidad(tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.parte_adecuada_tabla_ampacidad_dict, self.Taislante, self.Tterminales, self.factor_agrupamiento, self.factor_temperatura, self.Interruptor, self.numero_conductores_neutro,self.Tambiente_tabla_factor_temperatura, self.Tambiente, self.Icorregida_factor_ampacidad_cable_neutro, self.factor_Inominal_Interruptor, 'neutro')

        ''' Elección de cable de neutro'''

        self.indice_cable_neutro, self.calibre_cable_neutro, self.Area_cable_neutro = self.calculo_eleccion_cable_neutro(self.indice_cable_fase, self.calibre_cable_fase, self.Area_cable_fase, self.indice_ampacidad_neutro, self.calibre_ampacidad_neutro, self.Area_ampacidad_neutro, self.indice_tierra_fisica_final, self.calibre_tierra_fisica_final, self.Area_tierra_fisica_final,self.Inominal_fase, self.Inominal_neutro, self.factor_ampacidad_cable_neutro, self.tipo_circuito, self.numero_conductores_neutro)

        ''' Elección canalización conduit'''

        self.conductores_circuito = self.calculo_conductores_circuito(self.lineas, self.numero_conductores_por_fase, self.calibre_cable_fase, self.numero_conductores_neutro, self.calibre_cable_neutro, self.calibre_tierra_fisica_final, self.adicionar_tierra_fisica_aislada, self.calibre_tierra_fisica_aislada, self.misma_canalizacion)

        self.conductores_canalizacion = self.calculo_conductores_canalizacion(self.lineas, self.numero_conductores_por_fase, self.calibre_cable_fase, self.numero_conductores_neutro, self.calibre_cable_neutro, self.tierra_fisica_forrada, self.calibre_tierra_fisica_final, self.adicionar_tierra_fisica_aislada, self.calibre_tierra_fisica_aislada, self.misma_canalizacion, self.conductores_activos_adicionales_misma_canalizacion, self.conductores_no_activos_adicionales_misma_canalizacion)

        ####################
        for key, value in tablas.Tablas.dimensiones_cables_tabla_5['datos']['aislante_condutor'].items():
            lista_key_aislante_conductor = key.split(',')
            lista_key_aislante_conductor = [x.strip() for x in lista_key_aislante_conductor]
            if self.aislante_conductor in lista_key_aislante_conductor:
                self.tabla_dimensiones_cables_adecuada_lista = tablas.Tablas.dimensiones_cables_tabla_5['datos']['aislante_condutor'][key]
                break
        ####################

        self.Area_conductores = self.calculo_Area_conductores(self.conductores_canalizacion, tablas.Tablas.calibres_tabla, tablas.Tablas.Area_conductor_tabla, self.tabla_dimensiones_cables_adecuada_lista)

        ####################
        self.conductores_canalizacion_totales = 0
        for numero_conductores in self.conductores_canalizacion['forrados'].values():
            self.conductores_canalizacion_totales = self.conductores_canalizacion_totales + numero_conductores
        for numero_conductores in self.conductores_canalizacion['desnudos'].values():
            self.conductores_canalizacion_totales = self.conductores_canalizacion_totales + numero_conductores
        ####################

        self.porcentaje_llenado_conduit, self.medida_conduit_in, self.medida_conduit_mm, self.Area_conduit = self.calculo_conduit(self.Area_conductores, self.conductores_canalizacion_totales, self.tipo_conduit, tablas.Tablas.dimensiones_tubo_conduit_tabla_4, tablas.Tablas.porcentaje_llenado_conduit_tabla_1, self.conduit_pulg_forzado)

        self.datos_salida_dict = {
        'Carga': self.Carga,
        'Inominal_fase': self.Inominal_fase,
        'Inominal_neutro': self.Inominal_neutro,
        'Icorregida_factor_ampacidad_cable_fase': self.Icorregida_factor_ampacidad_cable_fase,
        'Icorregida_factor_ampacidad_cable_neutro': self.Icorregida_factor_ampacidad_cable_neutro,
        'Carga_corregida_factor_utilizacion_carga': self.Carga_corregida_factor_utilizacion_carga,
        'Carga_corregida_factor_simultaneidad_carga': self.Carga_corregida_factor_simultaneidad_carga,
        'numero_conductores_por_fase': self.numero_conductores_por_fase,
        'numero_conductores_neutro': self.numero_conductores_neutro,
        'factor_Inominal_fase_aplicado_neutro': self.factor_Inominal_fase_aplicado_neutro,
        'conductores_activos_canalizacion': self.conductores_activos_canalizacion,
        'Interruptor': self.Interruptor,
        'porcentaje_utilizacion_Interruptor': self.porcentaje_utilizacion_Interruptor,
        'factor_temperatura': self.factor_temperatura,
        'factor_agrupamiento': self.factor_agrupamiento,
        'calibre_ampacidad_fase': self.calibre_ampacidad_fase, 
        'Area_ampacidad_fase': self.Area_ampacidad_fase, 
        'Ampacidad_fase': self.Ampacidad_fase, 
        'Ampacidad_corregida_fase': self.Ampacidad_corregida_fase,
        'calibre_caida_fase': self.calibre_caida_fase,
        'Area_caida_fase': self.Area_caida_fase,
        'caida_tension_calculada': self.caida_tension_calculada,
        'calibre_cable_fase': self.calibre_cable_fase,
        'Area_cable_fase': self.Area_cable_fase,
        'calibre_tierra_fisica': self.calibre_tierra_fisica, 
        'Area_tierra_fisica': self.Area_tierra_fisica,
        'factor_correccion_cable_tierra_fisica': self.factor_correccion_cable_tierra_fisica,
        'Area_tierra_fisica_corregida_caida_ideal': self.Area_tierra_fisica_corregida_caida_ideal,
        'calibre_tierra_fisica_corregida_caida': self.calibre_tierra_fisica_corregida_caida,
        'Area_tierra_fisica_corregida_caida': self.Area_tierra_fisica_corregida_caida,
        'calibre_tierra_fisica_final': self.calibre_tierra_fisica_final,
        'Area_tierra_fisica_final': self.Area_tierra_fisica_final,
        'calibre_tierra_fisica_aislada': self.calibre_tierra_fisica_aislada,
        'Area_tierra_fisica_aislada': self.Area_tierra_fisica_aislada,
        'calibre_ampacidad_neutro': self.calibre_ampacidad_neutro, 
        'Area_ampacidad_neutro': self.Area_ampacidad_neutro, 
        'Ampacidad_neutro': self.Ampacidad_neutro, 
        'Ampacidad_corregida_neutro': self.Ampacidad_corregida_neutro,
        'calibre_cable_neutro': self.calibre_cable_neutro, 
        'Area_cable_neutro': self.Area_cable_neutro,
        'conductores_circuito': self.conductores_circuito,
        'conductores_canalizacion': self.conductores_canalizacion,
        'Area_conductores': self.Area_conductores,
        'porcentaje_llenado_conduit': self.porcentaje_llenado_conduit,
        'medida_conduit_in': self.medida_conduit_in,
        'medida_conduit_mm': self.medida_conduit_mm,
        'Area_conduit': self.Area_conduit,
        }
        
        return self.datos_por_defecto_Calculos_dict, self.datos_entrada, self.datos_salida_dict

