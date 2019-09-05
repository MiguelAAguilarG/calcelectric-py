from math import sqrt, pi

datos_entrada_dict = {
'Sistema': 'trifasico',
'Voltaje': 220,
'Carga': 1000,
'factor_carga': 1,
'fp': 0.9,
'caida_tension': 3,
'Longitud': 30,
'Tambiente': 30,
'aislante_conductor': 'THHW',
'Taislante': 75,
'Tterminales': 75,
'material_conductor': 'cobre',
'numero_conductores_por_fase': 1,
'misma_canalizacion': True,
'ajuste_factor_carga': 0,
'porcentaje_Irating': 0,
'Interruptor_forzado': False,
'canalizacion': 'conduit',
'material_canalizacion': 'acero',
'tipo_conduit': 'EMT',
'neutro_presente': True
}

def descripcion():
	datos_entrada_descripcion_dict = {}
	datos_entrada_descripcion_dict['nombre': 'Nombre del elemento (nombre único)'
	datos_entrada_descripcion_dict['coneccion': 'Conecciones con otros elementos eléctricos'
	datos_entrada_descripcion_dict['Sistema': 'Sistema (\'monofásico\',  \'trifásico\')'
	datos_entrada_descripcion_dict['Voltaje': 'Voltaje (V)'
	datos_entrada_descripcion_dict['Carga': 'Carga (W)'
	datos_entrada_descripcion_dict['factor_carga': 'Factor de carga (nueva carga = Carga*factor de carga)'
	datos_entrada_descripcion_dict['fp': 'factor de potencia (>0-1)'
	datos_entrada_descripcion_dict['caida_tension': 'Caída de tensión (%)'
	datos_entrada_descripcion_dict['Longitud': 'Longitud (m)'
	datos_entrada_descripcion_dict['conductores_activos_adicionales': 'Conductores activos adicionales en la misma canalización aparte del circuito calculado. El programa no considera los neutros (sistemas trifásicos) y tierras fisicas del circuito calculado'
	datos_entrada_descripcion_dict['Tambiente': 'Temperatura ambiente (°C)'
	datos_entrada_descripcion_dict['aislante_conductor': 'Aislante del conductor NOTA: todo en mayusculas'
	datos_entrada_descripcion_dict['Tconductor': 'Temperatura del aislante del conductor (°C)'
	datos_entrada_descripcion_dict['material_conductor': 'Material del conductor (\'cobre\', \'aluminio\')'
	datos_entrada_descripcion_dict['numero_conductores_por_fase': 'Número de conductores por fase, si hay neutro, sera el misma_canalizacion número de conductores para el neutro'
	datos_entrada_descripcion_dict['misma_canalizacion': 'Colocar el total de los conductores de fase y neutro en la misma canalización?: (\'si\' Nada recomendable cuando es mas de un conductor por fase,\'no\')'
	datos_entrada_descripcion_dict['ajuste_factor_carga': 'Ajuste hacia abajo en caso de no encontrar interruptor cercano con Factor de carga establecido (nuevo factor = factor de carga-Ajuste) (%)'
	datos_entrada_descripcion_dict['porcentaje_Irating_1': 'Ajuste Irating interruptor 1 (%) (Se calcula un ajuste Irating 1 \no se deja el asignado en el caso de que se haya puesto un interruptor forzado 1 \ny que si cumpla tanto el intarruptor forzado 2 y su ajuste Irating 1)'
	datos_entrada_descripcion_dict['Interruptor_forzado_1': 'Interruptor 1 forzado (A) (No aplicar = False, \nAplicar  = True (Se calcula un Interruptor 1 forzado y un porcentaje I rating 1), \nNúmero = Interruptor 1 forzado (Se verifica si cumple Interruptor 1 forzado, \nsino se procede como si fuera True) \n(Se verifica si cumple porcentaje I rating 1, \nsino se calcula un I rating 1 nuevo)'
	datos_entrada_descripcion_dict['porcentaje_Irating_2': 'Ajuste Irating interruptor 2 (%) (Se calcula un ajuste Irating 2 \no se deja el asignado en el caso de que se haya puesto un interruptor forzado 2 \ny que si cumpla tanto el intarruptor forzado 2 y su ajuste Irating 2)'
	datos_entrada_descripcion_dict['Interruptor_forzado_2': 'Interruptor 1 forzado (A) (No aplicar = False, \nAplicar  = True (Se calcula un Interruptor 2 forzado y un porcentaje I rating 2), \nNúmero = Interruptor 1 forzado (Se verifica si cumple Interruptor 2 forzado, \nsino se procede como si fuera True) \n(Se verifica si cumple porcentaje I rating 2, \nsino se calcula un I rating 2 nuevo)'
	datos_entrada_descripcion_dict['misma_canalizacion_amperaje': 'Interruptor 1 e interruptor 2 con el misma_canalizacion amperaje'
	datos_entrada_descripcion_dict['canalizacion': 'Canalizacion (\'conduit\',\'charola\')'
	datos_entrada_descripcion_dict['material_canalizacion': 'Material de la canalizacion (\'acero\', \'pvc\', \'aluminio\')'
	datos_entrada_descripcion_dict['tipo_conduit': 'Tipo de canalización'
	datos_entrada_descripcion_dict['neutro': 'Colocar neutro en el sistema trifásico: (\'si\',\'no\')'

	return datos_entrada_descripcion_dict