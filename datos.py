from math import sqrt

def descripcion():

	datos_entrada_descripcion_dict = {}
	datos_entrada_descripcion_dict['nombre'] = 'Nombre del elemento (nombre único)'
	datos_entrada_descripcion_dict['coneccion'] = 'Conecciones con otros elementos eléctricos'
	datos_entrada_descripcion_dict['Sistema'] = 'Sistema (\'monofásico\',  \'trifásico\')'
	datos_entrada_descripcion_dict['Voltaje'] = 'Voltaje (V)'
	datos_entrada_descripcion_dict['Carga'] = 'Carga (W)'
	datos_entrada_descripcion_dict['factor_carga'] = 'Factor de carga (nueva carga = Carga*factor de carga)'
	datos_entrada_descripcion_dict['fp'] = 'factor de potencia (>0-1)'
	datos_entrada_descripcion_dict['caida_tension'] = 'Caída de tensión (%)'
	datos_entrada_descripcion_dict['Longitud'] = 'Longitud (m)'
	datos_entrada_descripcion_dict['conductores_activos_adicionales'] = 'Conductores activos adicionales en la misma canalización aparte del circuito calculado. El programa no considera los neutros (sistemas trifásicos) y tierras fisicas del circuito calculado'
	datos_entrada_descripcion_dict['Tambiente'] = 'Temperatura ambiente (°C)'
	datos_entrada_descripcion_dict['aislante_conductor'] = 'Aislante del conductor NOTA: todo en mayusculas'
	datos_entrada_descripcion_dict['Tconductor'] = 'Temperatura del aislante del conductor (°C)'
	datos_entrada_descripcion_dict['material_conductor'] = 'Material del conductor (\'cobre\', \'aluminio\')'
	datos_entrada_descripcion_dict['numero_conductores_por_fase'] = 'Número de conductores por fase, si hay neutro, sera el mismo número de conductores para el neutro'
	datos_entrada_descripcion_dict['mismo'] = 'Colocar el total de los conductores de fase y neutro en la misma canalización?: (\'si\' Nada recomendable cuando es mas de un conductor por fase,\'no\')'
	datos_entrada_descripcion_dict['ajuste_factor_carga'] = 'Ajuste hacia abajo en caso de no encontrar interruptor cercano con Factor de carga establecido (nuevo factor = factor de carga-Ajuste) (%)'
	datos_entrada_descripcion_dict['porcentaje_Irating_1'] = 'Ajuste Irating interruptor 1 (%) (Se calcula un ajuste Irating 1 \no se deja el asignado en el caso de que se haya puesto un interruptor forzado 1 \ny que si cumpla tanto el intarruptor forzado 2 y su ajuste Irating 1)'
	datos_entrada_descripcion_dict['Interruptor_forzado_1'] = 'Interruptor 1 forzado (A) (No aplicar = False, \nAplicar  = True (Se calcula un Interruptor 1 forzado y un porcentaje I rating 1), \nNúmero = Interruptor 1 forzado (Se verifica si cumple Interruptor 1 forzado, \nsino se procede como si fuera True) \n(Se verifica si cumple porcentaje I rating 1, \nsino se calcula un I rating 1 nuevo)'
	datos_entrada_descripcion_dict['porcentaje_Irating_2'] = 'Ajuste Irating interruptor 2 (%) (Se calcula un ajuste Irating 2 \no se deja el asignado en el caso de que se haya puesto un interruptor forzado 2 \ny que si cumpla tanto el intarruptor forzado 2 y su ajuste Irating 2)'
	datos_entrada_descripcion_dict['Interruptor_forzado_2'] = 'Interruptor 1 forzado (A) (No aplicar = False, \nAplicar  = True (Se calcula un Interruptor 2 forzado y un porcentaje I rating 2), \nNúmero = Interruptor 1 forzado (Se verifica si cumple Interruptor 2 forzado, \nsino se procede como si fuera True) \n(Se verifica si cumple porcentaje I rating 2, \nsino se calcula un I rating 2 nuevo)'
	datos_entrada_descripcion_dict['mismo_amperaje'] = 'Interruptor 1 e interruptor 2 con el mismo amperaje'
	datos_entrada_descripcion_dict['canalizacion'] = 'Canalizacion (\'conduit\',\'charola\')'
	datos_entrada_descripcion_dict['material_canalizacion'] = 'Material de la canalizacion (\'acero\', \'pvc\', \'aluminio\')'
	datos_entrada_descripcion_dict['tipo_conduit'] = 'Tipo de canalización'
	datos_entrada_descripcion_dict['neutro'] = 'Colocar neutro en el sistema trifásico: (\'si\',\'no\')'

	return datos_entrada_descripcion_dict


def datos():

	datos_entrada_dict = {}
	
	identificador = '0'
	datos_entrada_dict[identificador] = {}
	datos_entrada_dict[identificador]['nombre'] = 'Carga 0'
	datos_entrada_dict[identificador]['coneccion'] = ['0.0']
	datos_entrada_dict[identificador]['Sistema'] = 'trifásico'
	datos_entrada_dict[identificador]['Voltaje'] = 220
	datos_entrada_dict[identificador]['Carga'] = 1000
	datos_entrada_dict[identificador]['factor_carga'] = 1
	datos_entrada_dict[identificador]['fp'] = 0.9
	datos_entrada_dict[identificador]['caida_tension'] = 3
	datos_entrada_dict[identificador]['Longitud'] = 30
	datos_entrada_dict[identificador]['Tambiente'] = 30
	datos_entrada_dict[identificador]['aislante_conductor'] = 'THHW'
	datos_entrada_dict[identificador]['Tconductor'] = 75
	datos_entrada_dict[identificador]['material_conductor'] = 'cobre'
	datos_entrada_dict[identificador]['numero_conductores_por_fase'] = 1
	datos_entrada_dict[identificador]['mismo'] ='no'
	datos_entrada_dict[identificador]['ajuste_factor_carga'] = 0
	datos_entrada_dict[identificador]['porcentaje_Irating_1'] = 0
	datos_entrada_dict[identificador]['Interruptor_forzado_1'] = False
	datos_entrada_dict[identificador]['porcentaje_Irating_2'] = 0
	datos_entrada_dict[identificador]['Interruptor_forzado_2'] = False
	datos_entrada_dict[identificador]['mismo_amperaje'] = False
	datos_entrada_dict[identificador]['canalizacion'] = 'conduit'
	datos_entrada_dict[identificador]['material_canalizacion'] = 'acero'
	datos_entrada_dict[identificador]['tipo_conduit'] = 'EMT'
	datos_entrada_dict[identificador]['neutro'] = 'no'

	'''identificador = '1'
	datos_entrada_dict[identificador] = {}
	datos_entrada_dict[identificador]['nombre'] = 'Carga 1'
	datos_entrada_dict[identificador]['coneccion'] = ['0.0']
	datos_entrada_dict[identificador]['Sistema'] = 'trifásico'
	datos_entrada_dict[identificador]['Voltaje'] = 220
	datos_entrada_dict[identificador]['Carga'] = 520000
	datos_entrada_dict[identificador]['factor_carga'] = 1.25
	datos_entrada_dict[identificador]['fp'] = 0.9
	datos_entrada_dict[identificador]['caida_tension'] = 3
	datos_entrada_dict[identificador]['Longitud'] = 10
	datos_entrada_dict[identificador]['Tambiente'] = 30
	datos_entrada_dict[identificador]['aislante_conductor'] = 'THHW'
	datos_entrada_dict[identificador]['Tconductor'] = 75
	datos_entrada_dict[identificador]['material_conductor'] = 'cobre'
	datos_entrada_dict[identificador]['numero_conductores_por_fase'] = 5
	datos_entrada_dict[identificador]['mismo'] ='no'
	datos_entrada_dict[identificador]['ajuste_factor_carga'] = 0
	datos_entrada_dict[identificador]['porcentaje_Irating_1'] = 1
	datos_entrada_dict[identificador]['Interruptor_forzado_1'] = True
	datos_entrada_dict[identificador]['porcentaje_Irating_2'] = 1
	datos_entrada_dict[identificador]['Interruptor_forzado_2'] = True
	datos_entrada_dict[identificador]['mismo_amperaje'] = False
	datos_entrada_dict[identificador]['canalizacion'] = 'conduit'
	datos_entrada_dict[identificador]['material_canalizacion'] = 'pvc'
	datos_entrada_dict[identificador]['tipo_conduit'] = 'EMT'
	datos_entrada_dict[identificador]['neutro'] = 'no'

	identificador = '2'
	datos_entrada_dict[identificador] = {}
	datos_entrada_dict[identificador]['nombre'] = 'Carga 2'
	datos_entrada_dict[identificador]['coneccion'] = ['0.0']
	datos_entrada_dict[identificador]['Sistema'] = 'trifásico'
	datos_entrada_dict[identificador]['Voltaje'] = 220
	datos_entrada_dict[identificador]['Carga'] = 45000*0.9
	datos_entrada_dict[identificador]['factor_carga'] = 1
	datos_entrada_dict[identificador]['fp'] = 0.9
	datos_entrada_dict[identificador]['caida_tension'] = 3
	datos_entrada_dict[identificador]['Longitud'] = 50
	datos_entrada_dict[identificador]['Tambiente'] = 40
	datos_entrada_dict[identificador]['aislante_conductor'] = 'THHW'
	datos_entrada_dict[identificador]['Tconductor'] = 75
	datos_entrada_dict[identificador]['material_conductor'] = 'cobre'
	datos_entrada_dict[identificador]['numero_conductores_por_fase'] = 1
	datos_entrada_dict[identificador]['mismo'] ='no'
	datos_entrada_dict[identificador]['ajuste_factor_carga'] = 0
	datos_entrada_dict[identificador]['porcentaje_Irating_1'] = 1
	datos_entrada_dict[identificador]['Interruptor_forzado_1'] = True
	datos_entrada_dict[identificador]['porcentaje_Irating_2'] = 1
	datos_entrada_dict[identificador]['Interruptor_forzado_2'] = True
	datos_entrada_dict[identificador]['mismo_amperaje'] = False
	datos_entrada_dict[identificador]['canalizacion'] = 'conduit'
	datos_entrada_dict[identificador]['material_canalizacion'] = 'acero'
	datos_entrada_dict[identificador]['tipo_conduit'] = 'EMT'
	datos_entrada_dict[identificador]['neutro'] = 'si' '''

	return datos_entrada_dict