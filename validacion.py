class Validacion():
    """docstring for ClassName"""

    def __init__(self):
        pass

    def validacion_datos_entrada(self, datos_entrada):
        
        if isinstance(datos_entrada, dict):
            pass
        else:
            print('!ERROR¡ Los datos de entrada no son un diccionario')
            return False

        self.Sistema = self.datos_entrada['Sistema']
        self.lineas = self.datos_entrada['lineas']
        self.Voltaje = self.datos_entrada['Voltaje']
        self.Carga = self.datos_entrada['Carga']
        self.fp = self.datos_entrada['fp']
        self.factor_utilizacion_carga = self.datos_entrada['factor_utilizacion_carga']
        self.factor_simultaneidad_carga = self.datos_entrada['factor_simultaneidad_carga']
        self.Interruptor_forzado = self.datos_entrada['Interruptor_forzado']
        self.factor_Inominal_Interruptor = self.datos_entrada['factor_Inominal_Interruptor']
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
        self.factor_Inominal_fase_aplicado_neutro = self.datos_entrada['factor_Inominal_fase_aplicado_neutro']
        self.neutro_activo_factor_agrupamiento = self.datos_entrada['neutro_activo_factor_agrupamiento']
        self.tierra_fisica_forrada = self.datos_entrada['tierra_fisica_forrada']
        self.adicionar_tierra_fisica_aislada = self.datos_entrada['adicionar_tierra_fisica_aislada']
        self.canalizacion = self.datos_entrada['canalizacion']
        self.tipo_conduit = self.datos_entrada['tipo_conduit']
        self.conduit_pulg_forzado = self.datos_entrada['conduit_pulg_forzado']
        self.material_canalizacion = self.datos_entrada['material_canalizacion']
        self.misma_canalizacion = self.datos_entrada['misma_canalizacion']
        self.conductores_activos_adicionales_misma_canalizacion = self.datos_entrada['conductores_activos_adicionales_misma_canalizacion']
        self.conductores_no_activos_adicionales_misma_canalizacion = self.datos_entrada['conductores_no_activos_adicionales_misma_canalizacion']

    